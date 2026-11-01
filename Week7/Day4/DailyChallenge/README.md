# Olympic Data Exploration — complete solution

The SQL file answers all four tasks from the current daily challenge and includes comments explaining each query.

## Running the file

Import the Database Star Olympic PostgreSQL dataset, open a fresh pgAdmin Query Tool connected to that database, and execute `olympic_exploration.sql` in full. The script searches `olympics` and then `public`; adjust `search_path` if your tables are elsewhere. Keep the same session open to inspect the temporary tables. Open a fresh session for a rerun.

This is PostgreSQL SQL, including FILTER aggregates and PostgreSQL temporary-table syntax. It does not modify the imported source tables.

## Answers and reasoning

### Exercise 1, Task 1

Group genuine medal results by athlete and count Summer and Winter medals separately. Retain athletes with at least one medal in each season. The temporary table contains athlete ID, full name, both season counts, and total medals. Participation without a medal in one season does not qualify.

### Exercise 1, Task 2

Group medal results by athlete and require exactly two distinct sport IDs. Count all their medal results and store every qualifying athlete in a temporary table. Display that table, then use a subquery to select the top three by total medals. An athlete may have participated without winning a medal in other sports. Ties are resolved by athlete ID to return at most three people.

### Exercise 2, Task 1

The wording is ambiguous. This solution interprets it as: find each athlete's highest career medal count in any one event, then sum those best-event counts by associated region and return the top five regions. It does not sum all career medals after identifying a best event, because that would discard the single-event restriction.

A correlated MAX subquery finds the best event tally. If several events tie for one athlete, the smallest event ID is chosen deterministically; their tally contributes only once per region. Event IDs identify specific events across editions of the Games.

The region table records career associations without a Games/event date. Athletes associated with several regions therefore contribute once to each associated region. The resulting ranking describes the best-event careers of associated athletes, not official medals won on behalf of a particular nation. The schema cannot resolve the latter precisely.

### Exercise 2, Task 2

Count distinct Games IDs per athlete, keep counts greater than three, and use NOT EXISTS to exclude anyone with a career medal. Store the result in a temporary table with full names and Games counts. Distinct Games prevent several event entries at the same Games from inflating the count.

## Counting rules

- Competitors are identified by person ID across their career, not by Games appearance ID or name.
- Only Gold, Silver, and Bronze are medals. N/A never counts.
- Each medal-winning athlete/event result counts as one athlete medal, including a team-event medal for each winning athlete.
- Sport and event are different levels: exactly two medal-winning sports is not the same as exactly two medal-winning events.
- Empty results remain valid if no athletes satisfy a condition in the imported version of the data.

## Validation status

Reviewed against all four prompts and the dataset structure used in the preceding assignment. The full dataset queries have not been executed: local PostgreSQL authentication still requires credentials. Numerical rankings and names are intentionally left to the queries rather than invented.

Assignment: https://octopus.developers.institute/courses/collection/229/course/1006/section/1527/chapter/3872
Dataset description: https://www.databasestar.com/sample-database-olympic-games/
