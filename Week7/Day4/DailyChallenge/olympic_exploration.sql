-- Daily Challenge: Olympic Data Exploration (PostgreSQL)
-- Source: chapter 3872, Developers Institute.
-- Requires Database Star tables: person, person_region, noc_region, games,
-- games_competitor, competitor_event, event, sport, medal.
-- Run the whole script in a fresh pgAdmin session after importing the dataset.
BEGIN;
SET LOCAL search_path TO olympics, public;

-- Materialize genuine medal results once for reuse. N/A is NOT a medal.
-- person_id identifies an athlete across Games; competitor_id identifies an
-- appearance at one Games. Team medals count once for each winning athlete.
CREATE TEMP TABLE exploration_medal_results ON COMMIT PRESERVE ROWS AS
SELECT gc.person_id, gc.games_id, ce.event_id, e.sport_id,
       g.season, m.medal_name
FROM games_competitor AS gc
JOIN competitor_event AS ce ON ce.competitor_id = gc.id
JOIN medal AS m ON m.id = ce.medal_id
JOIN games AS g ON g.id = gc.games_id
JOIN event AS e ON e.id = ce.event_id
WHERE m.medal_name IN ('Gold', 'Silver', 'Bronze');
CREATE INDEX ON exploration_medal_results (person_id, event_id);
ANALYZE exploration_medal_results;

-- EXERCISE 1, TASK 1: Medal winners in BOTH Summer and Winter.
-- Merely participating in both seasons does not satisfy this task.
CREATE TEMP TABLE exploration_dual_season_medallists
ON COMMIT PRESERVE ROWS AS
SELECT p.id AS person_id, p.full_name,
       counts.summer_medals, counts.winter_medals,
       counts.summer_medals + counts.winter_medals AS total_medals
FROM person AS p
JOIN (
    SELECT person_id,
           COUNT(*) FILTER (WHERE season = 'Summer') AS summer_medals,
           COUNT(*) FILTER (WHERE season = 'Winter') AS winter_medals
    FROM exploration_medal_results
    GROUP BY person_id
    HAVING COUNT(*) FILTER (WHERE season = 'Summer') > 0
       AND COUNT(*) FILTER (WHERE season = 'Winter') > 0
) AS counts ON counts.person_id = p.id;
SELECT * FROM exploration_dual_season_medallists
ORDER BY total_medals DESC, person_id;

-- EXERCISE 1, TASK 2: Exactly TWO sports with medals, not two events.
-- Only medal-winning sports count; participation in additional sports is allowed.
CREATE TEMP TABLE exploration_two_sport_medallists
ON COMMIT PRESERVE ROWS AS
SELECT p.id AS person_id, p.full_name, totals.medal_sports, totals.total_medals
FROM person AS p
JOIN (
    SELECT person_id, COUNT(DISTINCT sport_id) AS medal_sports,
           COUNT(*) AS total_medals
    FROM exploration_medal_results
    GROUP BY person_id
    HAVING COUNT(DISTINCT sport_id) = 2
) AS totals ON totals.person_id = p.id;
-- Display the complete requested temporary table.
SELECT * FROM exploration_two_sport_medallists
ORDER BY total_medals DESC, person_id;
-- Subquery chooses the top three QUALIFYING athletes, not the global top three.
-- person_id deterministically breaks medal-count ties, giving at most 3 rows.
SELECT *
FROM exploration_two_sport_medallists
WHERE person_id IN (
    SELECT person_id FROM exploration_two_sport_medallists
    ORDER BY total_medals DESC, person_id
    LIMIT 3
)
ORDER BY total_medals DESC, person_id;

-- EXERCISE 2, TASK 1: Best single-event career medal tally for each athlete.
-- An event is an event_id (e.g. a particular swimming distance), not a sport
-- or a single Games edition. Aggregate across all Games for that event.
CREATE TEMP TABLE exploration_event_medal_counts
ON COMMIT PRESERVE ROWS AS
SELECT person_id, event_id, COUNT(*) AS event_medals
FROM exploration_medal_results
GROUP BY person_id, event_id;
CREATE UNIQUE INDEX ON exploration_event_medal_counts (person_id, event_id);

-- Correlated subquery finds each athlete's highest event medal count.
-- A second subquery chooses the lowest event_id if several events tie.
-- This prevents multiplying an athlete's contribution to the region total.
CREATE TEMP TABLE exploration_best_events ON COMMIT PRESERVE ROWS AS
SELECT c.person_id, c.event_id, c.event_medals
FROM exploration_event_medal_counts AS c
WHERE c.event_medals = (
    SELECT MAX(other.event_medals)
    FROM exploration_event_medal_counts AS other
    WHERE other.person_id = c.person_id
)
AND c.event_id = (
    SELECT MIN(tied.event_id)
    FROM exploration_event_medal_counts AS tied
    WHERE tied.person_id = c.person_id AND tied.event_medals = c.event_medals
);

-- Sum ONE best-event total per associated athlete for each region.
-- DISTINCT protects against duplicate career-region association rows.
SELECT nr.id AS region_id, nr.region_name,
       SUM(best.event_medals) AS total_best_event_medals,
       COUNT(*) AS contributing_competitors
FROM noc_region AS nr
JOIN (SELECT DISTINCT person_id, region_id FROM person_region) AS pr
  ON pr.region_id = nr.id
JOIN exploration_best_events AS best ON best.person_id = pr.person_id
GROUP BY nr.id, nr.region_name
ORDER BY total_best_event_medals DESC, nr.region_name, nr.id
LIMIT 5;
-- Limitation: person_region gives career memberships, not region per Games.
-- A multi-region athlete contributes to EACH associated region. These are
-- regional athlete-career statistics, not an official national medal table.

-- EXERCISE 2, TASK 2: More than THREE distinct Games and ZERO career medals.
-- Count Games before joining to event results to avoid inflating appearances.
CREATE TEMP TABLE exploration_frequent_non_medallists
ON COMMIT PRESERVE ROWS AS
SELECT p.id AS person_id, p.full_name, appearances.number_of_games
FROM person AS p
JOIN (
    SELECT person_id, COUNT(DISTINCT games_id) AS number_of_games
    FROM games_competitor
    GROUP BY person_id
    HAVING COUNT(DISTINCT games_id) > 3
) AS appearances ON appearances.person_id = p.id
WHERE NOT EXISTS (
    SELECT 1 FROM exploration_medal_results AS mr
    WHERE mr.person_id = p.id
);
SELECT * FROM exploration_frequent_non_medallists
ORDER BY number_of_games DESC, person_id;

COMMIT;
-- All created objects are temporary; source data is unchanged.
-- Temporary tables persist in this session and disappear on disconnect.
-- Open a new session to rerun this file without table-name conflicts.
