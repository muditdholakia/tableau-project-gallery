# Original Tableau Server operations runbook

## Refresh reliability

Use a development data source reachable from the Server environment. Verify its
authentication separately from PAT authentication to the REST API. Run one manual
refresh, check its completion, then assign an appropriate schedule. Document the server
time zone, source update time, dependency order, run duration, and freshness target.
Cloud and Server scheduling controls differ; consult the documentation for your product.
Investigate failures before retrying. Avoid overlapping expensive refreshes.

## Performance investigation

Choose a reproducible interaction sequence: initial load, one region filter, and a sheet
navigation. Record data volume, connection type, cache state, and timings. Change one
factor at a time and repeat the same sequence. Separate query time from rendering time.
Use the current Desktop/Server performance-recording instructions and confirm any
administrator enablement required by your Server version.

## Backup and recovery planning — Server only

Tableau Server recovery requires more than exporting workbooks. Use the supported TSM
backup process and capture the configuration/topology separately according to current
documentation. Keep backups encrypted with restricted access, outside this public repo.
They may contain extracts, user information, connection information, and secrets.
Plan storage capacity, retention, supported version compatibility, and a restoration test
in an isolated environment. Do not run restore commands on a production server as a lab.
This repository does not contain or execute backup/restore commands.

## Content lifecycle

Collect inventory using a development read-only identity. Agree with content owners on
freshness and retention rules. Review stale content and dependencies before archiving or
deleting; an old modified date does not establish that a workbook is unused. Do not store
production inventories or user activity exports in Git. This repo makes no deletion calls.

References:
- [Performance recording](https://help.tableau.com/current/pro/desktop/en-us/perf_record_create_desktop.htm)
- [Server backup and configuration considerations](https://help.tableau.com/current/server/en-us/db_backup.htm)
