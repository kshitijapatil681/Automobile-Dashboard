# Deploy on Vercel

The dashboard is a static HTML application with working client-side interactions. Vercel can serve the existing dashboard file directly. The checked-in `vercel.json` selects the Other preset, skips build/install commands, and publishes the `dashboards` directory. No secrets or environment variables are required.

## GitHub import

For this personally owned repository, the owner (`kshitijapatil681`) must make the GitHub-to-Vercel connection. Vercel's GitHub integration does not allow a collaborator on a personal repository to import/connect it. Collaborator write access alone is not sufficient. See [Vercel's repository permissions](https://vercel.com/docs/git/vercel-for-github#personal-account-repositories).

After the deployment configuration has been merged:

1. Sign in to Vercel with the repository owner's connected GitHub account.
2. Choose **Add New → Project**, grant access to this repository if needed, and import `kshitijapatil681/Automobile-Dashboard`.
3. Keep the root directory at the repository root. The configuration supplies **Framework: Other**, **Output Directory: dashboards**, and empty build/install commands.
4. Deploy and open the resulting Vercel URL. Verify that the initial cards show 457 records and 31.70M recorded sale value, then test filters and CSV export.

The dashboard is available at the site's root. The PDF is at `/exports/automobile-dashboard.pdf`. This repository does not record a deployment URL because a Vercel project has not yet been created as part of this change.

For direct deployment under another account, Vercel also supports its CLI without a Git integration. That account must authorize the deployment separately; it does not automatically establish GitHub-triggered updates. See [Vercel CLI deploy](https://vercel.com/docs/cli/deploy).

## What operates live

| Feature | Hosted behavior |
| --- | --- |
| Year, country, and make filters | Recalculate the displayed selection immediately in the browser |
| Charts and summary cards | Recalculate from the embedded dataset |
| CSV export and printing | Work in the visitor's browser |
| Shared URL | Opens the working dashboard rather than HTML source |
| Source data | Remains the committed 457-record snapshot until deliberately updated |
| Database updates / saved edits / user accounts | Not implemented |
| Power BI Service refresh | Not applicable: this is an HTML dashboard, not an embedded Power BI report |

## Updating the dataset

Review and update the public CSV, retaining the client-name exclusion and documenting new source coverage. Update the validator's snapshot controls only after reconciling the new data, then run:

```sh
python scripts/validate_data.py
python scripts/build_dashboard.py
```

Refresh the screenshot/PDF if required, and commit the changed CSV and generated HTML through a pull request. With a Git-connected Vercel project, changes to the configured production branch trigger a new deployment. Changing only the CSV does not refresh the embedded HTML.

Automatic refresh from a database, API, or shared sheet would be a separate enhancement requiring a chosen data source, refresh rules, and access controls.

Sources: [Vercel static build configuration](https://vercel.com/docs/builds/configure-a-build), [vercel.json reference](https://vercel.com/docs/project-configuration/vercel-json), and [GitHub integration](https://vercel.com/docs/git/vercel-for-github).
