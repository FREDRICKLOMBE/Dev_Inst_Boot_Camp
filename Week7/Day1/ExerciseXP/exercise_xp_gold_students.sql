-- Exercises XP Gold: Students table #2 (PostgreSQL)
-- Connect to bootcamp and use the students table from Exercise XP+.
-- Each query returns only first_name, last_name, and birth_date.

-- Question 1: Fetch the first four students alphabetically by last name.
-- First name and id break ties so the result order is consistent.
SELECT first_name, last_name, birth_date
FROM students
ORDER BY last_name ASC, first_name ASC, id ASC
LIMIT 4;

-- Question 2: Fetch the youngest student (the latest birth date).
-- If birth dates tie, return the student with the smallest id.
SELECT first_name, last_name, birth_date
FROM students
ORDER BY birth_date DESC, id ASC
LIMIT 1;

-- Question 3: Skip the first two students and fetch the next three.
-- Use id order to make the skipped and returned rows predictable.
SELECT first_name, last_name, birth_date
FROM students
ORDER BY id ASC
LIMIT 3 OFFSET 2;
