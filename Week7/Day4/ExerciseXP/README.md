# Advanced Olympic Data Analysis

All eight assignment tasks are answered in `olympic_analysis.sql`, with comments explaining joins, subqueries, counting rules, and temporary tables.

## Run

1. Load the Database Star Olympic dataset into a PostgreSQL database using its PostgreSQL import scripts.
2. Open a fresh pgAdmin Query Tool session connected to that database.
3. Run the entire solution in the same session. The script searches the `olympics` schema, then `public`; change its `search_path` if your import uses another schema.
4. Review each SELECT result in pgAdmin. Temporary tables remain until the session closes. Use a fresh session for reruns.

This file targets PostgreSQL, not SQLite. The assignment links both engines, but their syntax and dataset import files differ.

## Interpretation decisions

- **Age:** stored on `games_competitor`, so an athlete's age varies between Games. Exercise 1 Task 1 averages one appearance per medal type, rather than repeating an appearance for every medal won. A person appearing at several Games contributes several recorded ages. A single career-wide age would require an arbitrary rule; this choice avoids inventing one. NULL and zero ages are treated as unknown.
- **Medals:** only Gold, Silver, and Bronze count. The N/A medal entry does not count. One medal-winning event result counts as one athlete medal, including team events.
- **Events:** “different events” means distinct event IDs. Exercise 1 counts across a career; Exercise 2 counts within each Games.
- **Region:** `person_region` links a person to career regions, without an event/Games date. Multi-region athletes contribute once to each region. Regional medal statistics therefore describe the careers of associated athletes, not an exact national medal tally. This limitation cannot be resolved from the schema alone.
- **Height update:** executed on `xp_competitor_heights`, a temporary competitor copy, leaving the imported source unchanged. It updates all competitors with usable regional data. An athlete associated with several regions gets the mean of all distinct peers sharing any of those regions; each peer counts once. A snapshot prevents update-order effects. Missing/zero heights are excluded; original values are retained if no valid regional mean exists.
- **Average medals:** includes zero-medal athletes. Only actual Games participants enter the regional and global averages. The global average counts each person once, regardless of region membership.

## Task map

| Task | Result |
|---|---|
| E1.1 | Correlated subquery returning average age for each medal type |
| E1.2 | Nested subqueries returning the top five regions by qualifying unique athletes |
| E1.3 | Temporary per-person medal totals, filtered to totals above two |
| E1.4 | DELETE with NOT EXISTS removing non-medallists from a temporary copy |
| E2.1 | Correlated UPDATE of regional average heights on a temporary competitor copy |
| E2.2 | INSERT from nested aggregation for athletes with multiple events in one Games |
| E2.3 | Regional medal averages exceeding the overall competitor average |
| E2.4 | Temporary season tracking and athletes appearing in both Summer and Winter |

## Verification and limitations

The queries were reviewed against all eight prompts and the dataset author's schema description. They have not been executed against the full Olympic dataset: the local PostgreSQL server requires credentials that have not been supplied. No numerical findings are invented. Exact results will appear when the script runs against your imported data.

## Sources

- Assignment: https://octopus.developers.institute/courses/collection/229/course/1006/section/1527/chapter/3869
- Dataset author's table descriptions: https://www.databasestar.com/sample-database-olympic-games/
- PostgreSQL dataset scripts: https://github.com/bbrumm/databasestar/tree/main/sample_databases/sample_db_olympics/postgres
