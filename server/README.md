# Tableau Server and Cloud learning recipes

The Python recipes use the official Tableau Server Client library, with API version
negotiation, verified HTTPS, paginated reads, and environment-only PAT authentication.
These implementations are original. Commands preview by default; `--execute` makes
the configured connection and may perform the selected mutation.

## Setup

From the repository root:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python examples/server_admin.py inventory
```

Set the variables described in `.env.example` in your local shell or an OS credential
store. The scripts do not load `.env` automatically. Use the site's content URL,
not its display name; the default Tableau Server site uses an empty content URL.
Create a PAT for a least-privilege development identity. Never enter credentials
into tracked files or disable TLS verification. Use separate credentials per automation.

## Read-only inventory

```powershell
python examples/server_admin.py --execute inventory
```

The CSV contains accessible workbooks only; visibility depends on the authenticated
user. It is not a complete administrator audit unless the identity can see all content.
Output goes to ignored `output/`; names and identifiers can be private. Spreadsheet
formula prefixes are escaped. No owner email addresses are requested.

## Project permission rules

```powershell
python examples/server_admin.py permissions --project-id <LOCAL_PROJECT_UUID>
python examples/server_admin.py --execute permissions --project-id <LOCAL_PROJECT_UUID>
```

The JSON records explicit project rules. It does **not** compute effective access,
site-role limits, administrator exceptions, group membership, or workbook/data-source
rules. Verify effective access with the current UI and `permissions-lab.md`.

## Publish a new learning workbook

```powershell
python examples/server_admin.py publish --project-id <LOCAL_PROJECT_UUID> --workbook "workbooks/andy-kriebel/great-workbook.twbx" --name "Learning - Andy Kriebel examples"
```

After checking the preview, use the same command with `--execute` before `publish`.
The recipe uses CreateNew and never overwrites. Maintain Andy Kriebel attribution in
the published workbook description and learning project. Only publish to a development
audience after reviewing the packaged data and its terms. A duplicate name can fail;
check whether an earlier request succeeded before retrying.

## Refresh an existing extract

```powershell
python examples/server_admin.py refresh --workbook-id <LOCAL_WORKBOOK_UUID>
```

Use `--execute` before `refresh` to submit the job. Submission is asynchronous;
verify completion in job history or with the Jobs API. The imported teaching workbook
contains static packaged extracts whose original source files are not bundled; do not
expect it to refresh from your environment. Use your own refreshable development data
source for this recipe.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| Authentication rejected | PAT expiration, site content URL, permitted sign-in policy, server URL |
| Missing inventory objects | Identity visibility, site selection, pagination, project permissions |
| Permission export rejected | Project visibility and rights to query rules |
| Publish failure | Target project, publish capability, duplicate name, workbook compatibility, packaged data |
| Refresh failed | Source reachability, saved connection authentication, Backgrounder/job history |
| TLS failure | Trusted server certificate; repair trust rather than bypassing verification |
| Throttling or timeout | Inspect server health privately; use bounded retries and avoid blindly repeating mutations |

## References

- [Official TSC API reference](https://tableau.github.io/server-client-python/docs/api-ref)
- [Current permissions documentation](https://help.tableau.com/current/server/en-us/permissions.htm)
- [Tableau Server backup documentation](https://help.tableau.com/current/server/en-us/db_backup.htm)

No live Server/Cloud connection or administrative change was made while building
these recipes. Local tests use fakes and do not establish live integration support.
