"""Inspect a TWBX without extracting files or executing Tableau content."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import zipfile
from defusedxml import ElementTree

MAX_TOTAL = 100 * 1024 * 1024
TOKEN = re.compile(rb"(?:gh[pousr]_[A-Za-z0-9]{30,}|AKIA[A-Z0-9]{16}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)")

def inspect(path):
    path = Path(path)
    if path.stat().st_size > MAX_TOTAL:
        raise ValueError("Archive exceeds the inspection size limit")
    with zipfile.ZipFile(path) as archive:
        entries = archive.infolist()
        if len(entries) > 1000 or sum(e.file_size for e in entries) > MAX_TOTAL:
            raise ValueError("Archive exceeds the inspection limits")
        for entry in entries:
            name = PurePosixPath(entry.filename.replace('\\', '/'))
            if name.is_absolute() or '..' in name.parts or ':' in entry.filename:
                raise ValueError("Unsafe archive member path")
            if name.suffix.lower() in {'.exe', '.dll', '.bat', '.cmd', '.ps1', '.py', '.js', '.vbs'}:
                raise ValueError("Executable or script asset in workbook")
            if TOKEN.search(archive.read(entry)):
                raise ValueError("Credential pattern detected inside workbook")
        workbooks = [e for e in entries if e.filename.lower().endswith('.twb')]
        if len(workbooks) != 1:
            raise ValueError("Expected exactly one workbook definition")
        tree = ElementTree.fromstring(archive.read(workbooks[0]))
        for node in tree.iter():
            if node.tag.lower() in {'extension', 'dashboard-extension'}:
                raise ValueError("Dashboard extension requires separate review")
            for key, value in node.attrib.items():
                if value and any(term in key.lower() for term in ('password', 'secret', 'access-token', 'refresh-token')):
                    raise ValueError("Credential attribute requires separate review")
            if node.tag == 'calculation' and re.search(r'\bSCRIPT_(?:REAL|INT|BOOL|STR)\s*\(', node.get('formula', ''), re.I):
                raise ValueError("Analytics-extension calculation requires separate review")
        return {
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'bytes': path.stat().st_size,
            'tableau_source_build': tree.get('source-build'),
            'worksheets': len(tree.findall('./worksheets/worksheet')),
            'dashboards': len(tree.findall('./dashboards/dashboard')),
            'hyper_extracts': len([e for e in entries if e.filename.endswith('.hyper')]),
            'calculated_fields': len(tree.findall('.//column/calculation')),
            'datasource_captions': sorted({d.get('caption') for d in tree.findall('./datasources/datasource') if d.get('caption')}),
            'checks': 'No unsafe member paths, executable assets, selected credential patterns, credential attributes, or detected analytics/dashboard extensions',
            'limits': 'Structural checks only. No Tableau rendering, complete data-content review, or security certification.',
        }

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('workbook', type=Path)
    args = parser.parse_args()
    print(json.dumps(inspect(args.workbook), indent=2))
