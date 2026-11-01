-- Advanced Olympic Data Analysis - all eight tasks (PostgreSQL)
-- Requires the Database Star Olympic dataset in the olympics or public schema.
-- Run the entire file in ONE pgAdmin Query Tool session.
-- Source tables are read only; UPDATE/DELETE operate on temporary copies.
BEGIN;
SET LOCAL search_path TO olympics, public;

-- E1 TASK 1: Average age of medal-winning competitors by medal type.
-- Age belongs to a games_competitor (person + Games), not to person.
-- Each person/Games appearance counts once per medal type: winning several
-- Golds at one Games must not give that same age extra weight.
-- The correlated EXISTS links each medal type to each appearance.
SELECT m.medal_name,
       (SELECT AVG(NULLIF(gc.age, 0))
        FROM games_competitor AS gc
        WHERE EXISTS (
            SELECT 1 FROM competitor_event AS ce
            WHERE ce.competitor_id = gc.id AND ce.medal_id = m.id
        )) AS average_age
FROM medal AS m
WHERE m.medal_name IN ('Gold', 'Silver', 'Bronze')
ORDER BY CASE m.medal_name WHEN 'Gold' THEN 1 WHEN 'Silver' THEN 2 ELSE 3 END;
-- NULL/zero ages are treated as unknown. A person appearing in multiple
-- Games contributes the recorded age for each appearance; no single lifetime
-- age exists. See README for the distinction from medal-result weighting.

-- E1 TASK 2: Top five regions by unique athletes with >3 different events.
-- Distinct event IDs are counted across the athlete's entire career.
SELECT nr.id AS region_id, nr.region_name,
       COUNT(DISTINCT pr.person_id) AS unique_competitors
FROM noc_region AS nr
JOIN person_region AS pr ON pr.region_id = nr.id
WHERE pr.person_id IN (
    SELECT eligible.person_id
    FROM (
        SELECT gc.person_id
        FROM games_competitor AS gc
        JOIN competitor_event AS ce ON ce.competitor_id = gc.id
        GROUP BY gc.person_id
        HAVING COUNT(DISTINCT ce.event_id) > 3
    ) AS eligible
)
GROUP BY nr.id, nr.region_name
ORDER BY unique_competitors DESC, nr.region_name, nr.id
LIMIT 5;
-- person_region records career region membership, not region per event.
-- A multi-region athlete is counted once in EACH associated region.

-- E1 TASK 3: Total medals for EVERY person, including zero-medal athletes.
-- Preaggregate before joining to prevent multiplication through other tables.
CREATE TEMP TABLE xp_medal_totals ON COMMIT PRESERVE ROWS AS
SELECT p.id AS person_id, p.full_name,
       COALESCE(mt.total_medals, 0) AS total_medals
FROM person AS p
LEFT JOIN (
    SELECT gc.person_id, COUNT(*) AS total_medals
    FROM games_competitor AS gc
    JOIN competitor_event AS ce ON ce.competitor_id = gc.id
    JOIN medal AS m ON m.id = ce.medal_id
    WHERE m.medal_name IN ('Gold', 'Silver', 'Bronze')
    GROUP BY gc.person_id
) AS mt ON mt.person_id = p.id;
CREATE UNIQUE INDEX ON xp_medal_totals (person_id);
SELECT * FROM xp_medal_totals
WHERE total_medals > 2
ORDER BY total_medals DESC, person_id;
-- Each medal-winning competitor_event row counts as an athlete medal.
-- Team-event medals count once per athlete, not once per national team.

-- E1 TASK 4: Remove non-medal winners from a temporary analysis table.
CREATE TEMP TABLE xp_medallists ON COMMIT PRESERVE ROWS AS
SELECT * FROM xp_medal_totals;
DELETE FROM xp_medallists AS a
WHERE NOT EXISTS (
    SELECT 1
    FROM games_competitor AS gc
    JOIN competitor_event AS ce ON ce.competitor_id = gc.id
    JOIN medal AS m ON m.id = ce.medal_id
    WHERE gc.person_id = a.person_id
      AND m.medal_name IN ('Gold', 'Silver', 'Bronze')
);
SELECT * FROM xp_medallists ORDER BY total_medals DESC, person_id;

-- E2 TASK 1: Correlated UPDATE based on the same region's average height.
-- Snapshot the original heights so the result never depends on update order.
-- Use NUMERIC to retain fractional means even if source heights are integers.
CREATE TEMP TABLE xp_original_heights ON COMMIT PRESERVE ROWS AS
SELECT id, NULLIF(height, 0)::NUMERIC AS height FROM person;
CREATE UNIQUE INDEX ON xp_original_heights (id);
CREATE TEMP TABLE xp_competitor_heights ON COMMIT PRESERVE ROWS AS
SELECT id AS person_id, full_name, height FROM person;
ALTER TABLE xp_competitor_heights ALTER COLUMN height TYPE NUMERIC;
UPDATE xp_competitor_heights AS target
SET height = (
    SELECT AVG(h.height)
    FROM xp_original_heights AS h
    WHERE EXISTS (
        SELECT 1
        FROM person_region AS peer_region
        JOIN person_region AS own_region
          ON own_region.region_id = peer_region.region_id
        WHERE own_region.person_id = target.person_id
          AND peer_region.person_id = h.id
    )
)
WHERE EXISTS (
    SELECT 1 FROM xp_original_heights AS h
    WHERE h.height IS NOT NULL AND EXISTS (
        SELECT 1
        FROM person_region AS peer_region
        JOIN person_region AS own_region
          ON own_region.region_id = peer_region.region_id
        WHERE own_region.person_id = target.person_id
          AND peer_region.person_id = h.id
    )
);
-- All heights are updated as requested, not only missing heights.
-- For multiple regions, average the UNION of peers once per person.
-- Include the athlete's own valid height. Unknown/zero heights are excluded.
-- Preserve the original value if no valid regional height can be found.
SELECT target.person_id, target.full_name,
       p.height AS original_height, target.height AS regional_average_height
FROM xp_competitor_heights AS target
JOIN person AS p ON p.id = target.person_id
ORDER BY target.person_id;

-- E2 TASK 2: Insert athletes with >1 distinct event within the SAME Games.
-- Group by person AND Games so different Olympic appearances are not mixed.
CREATE TEMP TABLE xp_multiple_events (
    person_id INTEGER NOT NULL,
    games_id INTEGER NOT NULL,
    total_events BIGINT NOT NULL CHECK (total_events > 1),
    PRIMARY KEY (person_id, games_id)
) ON COMMIT PRESERVE ROWS;
INSERT INTO xp_multiple_events (person_id, games_id, total_events)
SELECT eligible.person_id, eligible.games_id, eligible.total_events
FROM (
    SELECT gc.person_id, gc.games_id,
           COUNT(DISTINCT ce.event_id) AS total_events
    FROM games_competitor AS gc
    JOIN competitor_event AS ce ON ce.competitor_id = gc.id
    GROUP BY gc.person_id, gc.games_id
) AS eligible
WHERE eligible.total_events > 1;
SELECT p.full_name, g.games_name, x.total_events
FROM xp_multiple_events AS x
JOIN person AS p ON p.id = x.person_id
JOIN games AS g ON g.id = x.games_id
ORDER BY x.total_events DESC, x.person_id, x.games_id;

-- E2 TASK 3: Regional average medals/person greater than global average.
-- Both averages include zero-medal competitors. Global denominator includes
-- all people who actually appeared in games_competitor, even without a region.
SELECT r.region_id, r.region_name, r.average_medals_per_competitor,
       (SELECT AVG(t.total_medals::NUMERIC)
        FROM xp_medal_totals AS t
        WHERE EXISTS (SELECT 1 FROM games_competitor AS gc
                      WHERE gc.person_id = t.person_id)) AS overall_average
FROM (
    SELECT nr.id AS region_id, nr.region_name,
           AVG(t.total_medals::NUMERIC) AS average_medals_per_competitor
    FROM noc_region AS nr
    JOIN (SELECT DISTINCT person_id, region_id FROM person_region) AS pr
      ON pr.region_id = nr.id
    JOIN xp_medal_totals AS t ON t.person_id = pr.person_id
    WHERE EXISTS (SELECT 1 FROM games_competitor AS gc
                  WHERE gc.person_id = t.person_id)
    GROUP BY nr.id, nr.region_name
) AS r
WHERE r.average_medals_per_competitor > (
    SELECT AVG(t.total_medals::NUMERIC)
    FROM xp_medal_totals AS t
    WHERE EXISTS (SELECT 1 FROM games_competitor AS gc
                  WHERE gc.person_id = t.person_id)
)
ORDER BY r.average_medals_per_competitor DESC, r.region_id;
-- Career medals are associated with every career region membership; this
-- schema cannot assign individual medals precisely to a represented region.

-- E2 TASK 4: Track seasons and find people participating in both seasons.
CREATE TEMP TABLE xp_season_participation ON COMMIT PRESERVE ROWS AS
SELECT DISTINCT gc.person_id, g.season
FROM games_competitor AS gc
JOIN games AS g ON g.id = gc.games_id;
CREATE UNIQUE INDEX ON xp_season_participation (person_id, season);
SELECT p.id AS person_id, p.full_name
FROM person AS p
WHERE EXISTS (
    SELECT 1 FROM xp_season_participation AS s
    WHERE s.person_id = p.id AND s.season = 'Summer'
) AND EXISTS (
    SELECT 1 FROM xp_season_participation AS s
    WHERE s.person_id = p.id AND s.season = 'Winter'
)
ORDER BY p.full_name, p.id;

COMMIT;
-- Temporary tables stay available in this session and disappear on disconnect.
-- Rerun in a NEW session, since temporary table names already exist here.
