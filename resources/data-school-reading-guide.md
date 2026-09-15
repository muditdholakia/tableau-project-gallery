# The Data School UK reading guide

Use [The Data School UK](https://www.thedataschool.co.uk/) blog search to find the
titles below. This directory contains original learning exercises and bibliographic
references; it does not reproduce the articles, screenshots, or site assets.

| Reading title | Author | Pair with this repository |
| --- | --- | --- |
| How to access the data source of a packaged workbook. | Shahbaz Khan | Inspect the attributed TWBX with `examples/inspect_workbook.py` |
| Tableau File Formats | Joe Beaven | Compare a workbook definition, packaged workbook, and embedded extract |
| Tableau server permissions part 1 – Assigning permissions | Robert Headington | Create development groups and follow the permission matrix in `server/permissions-lab.md` |
| Tableau server permissions part 2 – Overlapping and Default permissions | Robert Headington | Test two-group membership and inherited content permissions |
| Tableau Server Permissions | Giorgia Astheimer | Compare declared permission rules with effective access in the current UI |
| Keeping things regular: how to use schedules on Tableau Server | Gwilym Lockwood | Follow the refresh runbook and document the server time zone |
| Downloading data from Tableau Server | Ryan Lowers | Compare workbook, summary-data, and full-data download permissions |
| TOP 10 TIPS for Performance in a Workbook | Tobias Colmer | Measure a fixed interaction sequence before and after one optimization |
| Performance Tips for Tableau Dashboards | Salome Grasland | Use the current Tableau performance-recording documentation to validate a hypothesis |

Some articles describe older Tableau releases. Treat screenshots, role names, menu
paths, and scheduling behavior as version-specific. Current Tableau documentation
is the authority for supported APIs and administration procedures.

## Workbook used in Data School teaching

[Andy Kriebel's author page](https://www.vizwiz.com/2019/12/the-great-workbook-of-calcs.html)
describes the advanced-calculation workbook used in his Data School teaching and
permits reuse with attribution. See `workbooks/andy-kriebel/README.md` for the actual
packaged workbook, its permission notice, provenance, and inspection limits.

## Reuse boundaries

The Data School website's terms restrict copying articles/assets and deep linking.
Accordingly the article references here link to its home page and identify readings
by title and author. No general open-source license for its blog content was found.
The separately published Andy Kriebel workbook uses its author's specific reuse
permission; it is not covered by this repository's MIT license.
