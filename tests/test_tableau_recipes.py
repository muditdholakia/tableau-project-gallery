import contextlib
import csv
import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'examples'))
import inspect_workbook
import server_admin

class WorkbookChecks(unittest.TestCase):
    def package(self, folder, name='demo.twb', text='<workbook><worksheets><worksheet name="Demo"/></worksheets></workbook>'):
        path=Path(folder)/'demo.twbx'
        with zipfile.ZipFile(path,'w') as archive:
            archive.writestr(name,text)
        return path

    def test_safe_package(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertEqual(inspect_workbook.inspect(self.package(folder))['worksheets'],1)

    def test_path_traversal_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(ValueError): inspect_workbook.inspect(self.package(folder,'../demo.twb'))

    def test_password_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(ValueError): inspect_workbook.inspect(self.package(folder,text='<workbook><connection password="fake-test-value"/></workbook>'))

    def test_analytics_extension_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(ValueError): inspect_workbook.inspect(self.package(folder,text='<workbook><calculation formula="SCRIPT_REAL(test)"/></workbook>'))

class ServerChecks(unittest.TestCase):
    def test_preview_never_connects(self):
        with patch.object(server_admin,'session',side_effect=AssertionError('Network forbidden')):
            with contextlib.redirect_stdout(io.StringIO()): server_admin.main(['inventory'])

    def test_csv_formula_escaping(self):
        for value in ('=1+1','  @demo','+123','-42'):
            self.assertTrue(server_admin.safe_cell(value).startswith("'"))
        self.assertEqual(server_admin.safe_cell('Synthetic'),'Synthetic')

    def test_paginated_inventory_fields(self):
        workbooks=[SimpleNamespace(id='test-id',name='=test',project_name='Learning',updated_at=None)]
        with tempfile.TemporaryDirectory() as folder, patch('tableauserverclient.Pager',return_value=workbooks):
            output=Path(folder)/'inventory.csv'
            self.assertEqual(server_admin.inventory(SimpleNamespace(workbooks=object()),output),1)
            with output.open(newline='') as handle: rows=list(csv.DictReader(handle))
            self.assertEqual(rows[0]['name'],"'=test")
            self.assertNotIn('owner_email',rows[0])

    def test_invalid_server_url_rejected(self):
        with patch.dict('os.environ',{'TABLEAU_SERVER_URL':'http://example.invalid'}):
            with self.assertRaises(ValueError):
                with server_admin.session(): pass

if __name__=='__main__': unittest.main()
