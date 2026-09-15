# tableau-project-gallery

An original synthetic-sales dashboard blueprint and Tableau Embedding API v3 example.

## Architecture

Synthetic CSV → Tableau workbook → Tableau Public or development Cloud site → browser embedding. The local example contains no authentication secrets.

## Prerequisites

Python 3.12; Tableau Desktop/Public authoring; a published visualization; a modern browser. Private embedding requires a backend-issued connected-app JWT and additional setup.

## Setup

1. Run `python examples/generate_sales.py` and connect Tableau to `data/sales.csv`.
2. Follow `examples/dashboard.md` to build and publish a synthetic-data workbook.
3. Replace the placeholder `src` in `examples/index.html` with your published visualization URL.
4. Run `python -m http.server 8000 --directory examples` and open http://localhost:8000.
5. Check region filtering, revenue totals, and keyboard navigation. Never put a connected-app secret into HTML.

## Sample workflow

CSV generation → calculated fields → KPI, trend, and region views → publish → embed. The workbook must be authored using the provided blueprint; no finished .twbx is included.

## Security

Read [SECURITY.md](SECURITY.md). Environment examples contain placeholders only.
Never commit local environment values or production exports. No deployment is automated.

## Troubleshooting

Blank embed: check the published URL and access settings. Private view login: configure connected apps on a server-side backend. Incorrect revenue: use Quantity × Unit Price and check field types.

## License and attribution

Original implementations and documentation by Mudit Dholakia, licensed under MIT.
No upstream code was imported. These references informed the learning scope:
- https://github.com/tableau/embedding-api-v3-samples
- https://github.com/tableau/hyper-api-samples
Platform services, SDK distributions, and third-party content retain their own terms.

## Updating

This is an original repository and has no upstream remote. Run `git pull --ff-only origin main`.
Review Dependabot changes and current platform documentation before upgrading.

## Validation limits

Python syntax and local smoke tests are checked before publication. Cloud execution,
tenant integrations, Tableau workbook authoring, and live agent evaluation require
your development environments and have not been verified by local checks.
