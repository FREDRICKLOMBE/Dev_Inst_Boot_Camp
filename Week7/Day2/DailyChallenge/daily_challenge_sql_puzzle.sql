-- Daily Challenge: SQL Puzzle
-- Predictions before execution: Q1 = 0, Q2 = 2, Q3 = 0, Q4 = 2.
-- Temporary tables keep this puzzle separate from permanent database tables.
BEGIN;
CREATE TABLE FirstTab (id integer, name varchar(10));
INSERT INTO FirstTab VALUES
    (5, 'Pawan'), (6, 'Sharlee'), (7, 'Krish'), (NULL, 'Avtaar');
CREATE TABLE SecondTab (id integer);
INSERT INTO SecondTab VALUES (5), (NULL);
SELECT * FROM FirstTab;
SELECT * FROM SecondTab;

-- Q1: 0. The subquery returns NULL. NOT IN yields UNKNOWN for every row.
SELECT COUNT(*) FROM FirstTab AS ft
WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id IS NULL);

-- Q2: 2. The subquery returns 5. IDs 6 and 7 pass;
-- ID 5 fails, and NULL yields UNKNOWN.
SELECT COUNT(*) FROM FirstTab AS ft
WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id = 5);

-- Q3: 0. The subquery returns 5 and NULL.
-- ID 5 yields FALSE; all other IDs yield UNKNOWN.
SELECT COUNT(*) FROM FirstTab AS ft
WHERE ft.id NOT IN (SELECT id FROM SecondTab);

-- Q4: 2. Filtering out NULL leaves 5, so IDs 6 and 7 pass.
SELECT COUNT(*) FROM FirstTab AS ft
WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id IS NOT NULL);
ROLLBACK;
