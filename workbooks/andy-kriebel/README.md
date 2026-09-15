# Andy Kriebel's Data School teaching workbook

Open [great-workbook.twbx](great-workbook.twbx) in a compatible Tableau Desktop
installation. This imported workbook contains 130 worksheets, five dashboards,
nine Hyper extracts, and 603 calculated-field definitions in the inspected snapshot.
Its source build is Tableau 2020.2; validate behavior in your current release.

Author: **Andy Kriebel**. Source: [author's workbook page](https://www.vizwiz.com/2019/12/the-great-workbook-of-calcs.html).
Published visualization: [Tableau Public](https://public.tableau.com/views/TheGreatBookofTableCalcs-LODCalcs-Actions/YoYTableCalc).
The author explains that he used the collection for teaching at The Data School.
This is third-party educational material, not a workbook authored by Mudit Dholakia.

## Permission and attribution

The author's page dated 13 December 2019 expressly allows reuse and requests
attribution. The permission includes the statement:

> You are welcome to use this in any way you please.

This is an author-specific permission, **not an MIT or other SPDX-classified license**.
Preserve Andy Kriebel attribution when using or adapting these examples. The repository
MIT license applies only to our original code and documentation; it does not relicense
this workbook, its embedded extracts, or its assets. The author's permission cannot
override rights held by others in bundled material. Review the dataset/asset terms
before repurposing or distributing them separately. No blog article or screenshot is copied.

The imported package is byte-for-byte the publicly downloadable author snapshot.
No copyright notices, formulas, data, or workbook assets were changed. Provenance and
the SHA-256 checksum are recorded in `provenance.json`.

## Suggested learning sequence

1. Work through `../../labs/advanced-calculations.md` with synthetic sales.
2. Study one table-calculation example, inspect Compute Using and partitioning,
   and rebuild it using your own fields.
3. Inspect a FIXED LOD example and compare dimension/context filter behavior.
4. Study a parameter or set action and document its clearing-selection behavior.
5. Save your newly authored synthetic-data workbook separately with explicit attribution
   if you adapted any of the imported examples.

## Inspection and limits

```powershell
python examples/inspect_workbook.py workbooks/andy-kriebel/great-workbook.twbx
```

The check reads ZIP members without extraction, validates size/path boundaries, parses
XML defensively, and checks for selected credential patterns and executable/extension
assets. It found no issues covered by those checks. Hyper extracts and query caches
are bundled in the source; `.key` members in those caches are Tableau cache artifacts,
not identified private-key blocks. This is not a full data or security audit.

Tableau Desktop rendering has not been tested in this environment. A GitHub file link
downloads the workbook; GitHub does not render an interactive Tableau dashboard.
Original data-source files are not all included, so source refresh is not a supported
use of this imported snapshot. Do not publish it as your own work.
