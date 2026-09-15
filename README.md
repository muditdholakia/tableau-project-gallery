# tableau-project-gallery

Synthetic-sales labs, an attributed Andy Kriebel Data School teaching workbook,
Tableau Embedding API v3, and original Tableau Server/Cloud automation recipes.

## Collection

| Content | Start here |
| --- | --- |
| Packaged workbook: 130 worksheets and five dashboards | [Andy Kriebel workbook and permission notice](workbooks/andy-kriebel/README.md) |
| The Data School UK readings | [Reading guide](resources/data-school-reading-guide.md) |
| Original LOD, table calculation, and parameter exercises | [Advanced-calculation labs](labs/advanced-calculations.md) |
| Inventory, project rules, publishing, and refresh scripts | [Server recipes](server/README.md) |
| Effective permissions testing | [Permissions lab](server/permissions-lab.md) |
| Refresh, performance, backup, and content lifecycle | [Operations runbook](server/operations-runbook.md) |

## Architecture

Synthetic CSV → Tableau workbook → Tableau Public or development Cloud site → browser embedding.
Server recipes: local environment PAT → official TSC REST client → paginated inventory,
permission-rule export, CreateNew publishing, or extract refresh. Private outputs are ignored.

## Prerequisites

Python 3.12; Tableau Desktop/Public authoring; a published visualization; a modern browser. Private embedding requires a backend-issued connected-app JWT and additional setup.

## Setup

1. Run `python examples/generate_sales.py` and connect Tableau to `data/sales.csv`.
2. Follow `examples/dashboard.md` to build and publish a synthetic-data workbook.
3. Replace the placeholder `src` in `examples/index.html` with your published visualization URL.
4. Run `python -m http.server 8000 --directory examples` and open http://localhost:8000.
5. Check region filtering, revenue totals, and keyboard navigation. Never put a connected-app secret into HTML.

## Sample workflow

CSV generation → calculated fields → KPI, trend, and region views → publish → embed.
The original sales workbook must be authored using the blueprint. An unchanged,
third-party `.twbx` teaching collection is included separately with explicit attribution.
Install `requirements.txt` for the workbook inspection and Server scripts; follow
[Server setup](server/README.md). Script commands preview by default.

## Security

Read [SECURITY.md](SECURITY.md). Environment examples contain placeholders only.
Never commit local environment values or production exports. No deployment is automated.

## Troubleshooting

Blank embed: check the published URL and access settings. Private view login: configure connected apps on a server-side backend. Incorrect revenue: use Quantity × Unit Price and check field types.

## License and attribution

Original implementations and documentation by Mudit Dholakia, licensed under MIT.
The imported Andy Kriebel workbook uses author-specific reuse permission and is **not
MIT-licensed**. See [third-party notices](THIRD_PARTY_NOTICES.md) and its adjacent permission
notice. The Data School articles/assets are not copied. These references informed the learning scope:
- https://github.com/tableau/embedding-api-v3-samples
- https://github.com/tableau/hyper-api-samples
Platform services, SDK distributions, and third-party content retain their own terms.

## Updating

This is an original repository and has no upstream remote. Run `git pull --ff-only origin main`.
Review Dependabot changes and current platform documentation before upgrading.

## Validation limits

Run `python -m unittest discover -s tests -v` after installing requirements. Checks cover
safe ZIP/XML handling, credential attributes, preview behavior, HTTPS enforcement, and
CSV formula escaping. GitHub Actions also inspects the included workbook. The source
workbook was created in Tableau 2020.2 and has not been rendered in Tableau Desktop here.
No live Server/Cloud connection, deployment, or refresh was performed.
