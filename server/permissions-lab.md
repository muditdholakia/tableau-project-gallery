# Development permissions lab

Create a dedicated learning project and two non-admin test identities. Assign appropriate
site roles, create Readers and Authors groups, and use synthetic content only. Confirm
your version's capability names in the official permissions UI.

| Test identity | Membership | Intended access |
| --- | --- | --- |
| Reader | Readers | View and filter the learning workbook; no publish, delete, or workbook/full-data download |
| Author | Authors | Publish and edit learning workbooks; no site/server administration |
| Overlap test | Readers plus a temporary restricted group | Observe effective access when relevant capability rules conflict |

1. Decide whether content permissions should be locked to the project. Record that choice.
2. Configure explicit development rules for groups rather than broad individual exceptions.
3. Test workbook viewing and data-source connection separately; configure dependencies.
4. Sign in as each non-admin identity and test view, filter, publish, download, and delete.
5. Add the overlap membership, inspect effective permissions, and document the explanation.
6. Remove temporary memberships and test again. Never test restrictive rules as an admin
   and assume ordinary users have the same results.

Exporting declared project rules with the Python recipe is supplementary evidence.
It does not calculate the effective permissions of a user. Site roles place a maximum
on capabilities; a content allow does not elevate the site's role.

Reference: [Current Tableau permissions](https://help.tableau.com/current/server/en-us/permissions.htm).
