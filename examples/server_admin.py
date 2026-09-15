"""Original Tableau Server/Cloud recipes. Commands preview unless --execute is supplied."""
import argparse
from contextlib import contextmanager
import csv
import json
import os
from pathlib import Path
from urllib.parse import urlsplit
import uuid

def safe_cell(value):
    text = str(value or '')
    return "'" + text if text.lstrip().startswith(('=', '+', '-', '@')) else text

def identifier(value):
    try:
        return str(uuid.UUID(value))
    except ValueError as error:
        raise argparse.ArgumentTypeError('Expected a UUID; supply private IDs locally') from error

@contextmanager
def session():
    import tableauserverclient as TSC
    url = os.environ.get('TABLEAU_SERVER_URL', '')
    parts = urlsplit(url)
    if parts.scheme != 'https' or not parts.hostname or parts.username or parts.password or parts.query or parts.fragment:
        raise ValueError('Set TABLEAU_SERVER_URL to a trusted HTTPS server base URL')
    token_name = os.environ.get('TABLEAU_PAT_NAME', '')
    token_secret = os.environ.get('TABLEAU_PAT_SECRET', '')
    if not token_name or not token_secret or token_name.startswith('REPLACE') or token_secret.startswith('REPLACE'):
        raise ValueError('Set PAT name and secret locally; never commit them')
    auth = TSC.PersonalAccessTokenAuth(token_name, token_secret, site_id=os.environ.get('TABLEAU_SITE_CONTENT_URL', ''))
    server = TSC.Server(url, use_server_version=True)
    server.add_http_options({'timeout': 60})
    with server.auth.sign_in(auth):
        yield server

def inventory(server, destination):
    import tableauserverclient as TSC
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.writer(handle)
        writer.writerow(['workbook_id', 'name', 'project', 'updated_at'])
        count = 0
        for workbook in TSC.Pager(server.workbooks):
            writer.writerow([safe_cell(workbook.id), safe_cell(workbook.name), safe_cell(workbook.project_name), safe_cell(workbook.updated_at)])
            count += 1
    return count

def permissions(server, project_id, destination):
    import tableauserverclient as TSC
    project = next((p for p in TSC.Pager(server.projects) if p.id == project_id), None)
    if project is None:
        raise ValueError('Project not found or not accessible')
    server.projects.populate_permissions(project)
    records = [{'grantee_type': rule.grantee.tag_name, 'grantee_id': rule.grantee.id, 'capabilities': dict(rule.capabilities)} for rule in project.permissions]
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(records, indent=2), encoding='utf-8')
    return len(records)

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--execute', action='store_true', help='Connect to the configured development server and perform the selected operation')
    subs = parser.add_subparsers(dest='operation', required=True)
    subs.add_parser('inventory', help='Read workbook inventory to untracked output/server-inventory.csv')
    permission = subs.add_parser('permissions', help='Read project permission rules, not effective user permissions')
    permission.add_argument('--project-id', type=identifier, required=True)
    publish = subs.add_parser('publish', help='Create a new development workbook; never overwrite')
    publish.add_argument('--project-id', type=identifier, required=True)
    publish.add_argument('--workbook', type=Path, required=True)
    publish.add_argument('--name', required=True)
    refresh = subs.add_parser('refresh', help='Submit an extract refresh job')
    refresh.add_argument('--workbook-id', type=identifier, required=True)
    args = parser.parse_args(argv)
    if args.operation == 'publish':
        if not args.workbook.is_file() or args.workbook.suffix.lower() != '.twbx':
            parser.error('Provide an existing packaged .twbx workbook')
        if not 1 <= len(args.name.strip()) <= 100:
            parser.error('Provide a workbook name of 1–100 characters')
        from inspect_workbook import inspect
        inspect(args.workbook)
    if not args.execute:
        print(f'PREVIEW: {args.operation}; no authentication, network calls, or server changes. Use --execute against a development environment to run.')
        return
    import tableauserverclient as TSC
    try:
        with session() as server:
            if args.operation == 'inventory':
                print(f'Exported {inventory(server, Path("output/server-inventory.csv"))} workbooks to private local output')
            elif args.operation == 'permissions':
                print(f'Exported {permissions(server, args.project_id, Path("output/project-permissions.json"))} permission rules to private local output')
            elif args.operation == 'publish':
                workbook = TSC.WorkbookItem(project_id=args.project_id, name=args.name)
                server.workbooks.publish(workbook, str(args.workbook), TSC.Server.PublishMode.CreateNew)
                print('Created development workbook; no existing workbook overwritten')
            else:
                workbook = server.workbooks.get_by_id(args.workbook_id)
                job = server.workbooks.refresh(workbook)
                if job is not None:
                    print(f'Refresh submitted; job ID: {job.id}. Submission does not establish successful completion.')
                else:
                    print('Refresh request returned no job object; check completion privately in the server UI.')
    except ValueError as error:
        raise SystemExit(str(error))
    except Exception as error:
        # SDK/network exception bodies can contain private server information.
        raise SystemExit(f'Tableau operation failed ({type(error).__name__}); check authentication, permissions, and connectivity privately')

if __name__ == '__main__':
    main()
