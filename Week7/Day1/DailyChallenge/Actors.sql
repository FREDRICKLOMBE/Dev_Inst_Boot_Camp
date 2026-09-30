--Creating an actors table
CREATE TABLE actors(
actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
);

--Inserting values in the table
INSERT INTO actors(first_name, last_name, age, number_oscars)
VALUES('Matt', 'Damon', '08/10/1970', 5);

TABLE actors;
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES
	('George','Clooney','06/05/1961', 2),
	('John','Doe','10/12/1993', 100);
	
-- 1. Count how many actors are in the table.
SELECT COUNT(*) AS total_actors
FROM actors;
-- Expected result: 3, if the inserts above ran once on a new table.


-- 2. Try adding an actor with missing fields.
-- Run this statement separately: it is expected to fail.
INSERT INTO actors (first_name, last_name)
VALUES ('Emma', 'Watson');

-- Expected outcome:
-- PostgreSQL rejects the row because age and number_oscars
-- are omitted, have no defaults, and cannot be NULL.

