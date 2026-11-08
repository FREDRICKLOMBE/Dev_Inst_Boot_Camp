-- Exercises XP: Database Concepts #2 - DVD Rental - Exercise 1
-- Source: https://octopus.developers.institute/courses/collection/229/course/1006/section/1658/chapter/395
-- Run in pgAdmin Query Tool connected to the PostgreSQL dvdrental database.
-- Dependency: restore dvdrental_backup.tar first if dvdrental is not already loaded.
-- Run Exercise 1 before Exercise 2, using the same database and schema.
-- This exercise creates new_film and customer_review, which Exercise 2 uses.
-- Run with Auto commit enabled, or commit Exercise 1 before running Exercise 2.

-- 1. All languages.
SELECT * FROM language ORDER BY language_id;

-- 2. Films with their languages.
SELECT f.title, f.description, l.name AS language_name
FROM film AS f
JOIN language AS l ON l.language_id = f.language_id
ORDER BY f.title;

-- 3. Preserve all languages, including those without films.
SELECT f.title, f.description, l.name AS language_name
FROM language AS l
LEFT JOIN film AS f ON f.language_id = l.language_id
ORDER BY l.name, f.title;

-- 4. Create a table and add films. These example tables must not already exist.
CREATE TABLE new_film (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);
INSERT INTO new_film (name)
VALUES ('The SQL Adventure'), ('Beyond the Database'), ('A Query to Remember');

-- 5. Reviews. Deleting a film automatically deletes its reviews.
CREATE TABLE customer_review (
    review_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    film_id INTEGER NOT NULL REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INTEGER NOT NULL REFERENCES language(language_id),
    title VARCHAR(255) NOT NULL,
    score INTEGER NOT NULL CHECK (score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
-- The default initializes last_update; future UPDATE statements should set
-- last_update = CURRENT_TIMESTAMP explicitly (the default is not an update trigger).

-- 6. Use existing IDs rather than assuming generated IDs or language IDs.
INSERT INTO customer_review (film_id, language_id, title, score, review_text)
SELECT f.id, l.language_id, 'An engaging adventure', 9,
       'A fun story with memorable characters.'
FROM new_film AS f
CROSS JOIN (SELECT language_id FROM language ORDER BY language_id LIMIT 1) AS l
WHERE f.name = 'The SQL Adventure';

INSERT INTO customer_review (film_id, language_id, title, score, review_text)
SELECT f.id, l.language_id, 'Worth watching', 8,
       'An imaginative film with a satisfying ending.'
FROM new_film AS f
CROSS JOIN (SELECT language_id FROM language ORDER BY language_id LIMIT 1) AS l
WHERE f.name = 'Beyond the Database';

-- 7. Inspect reviews before and after deleting a reviewed film.
SELECT * FROM customer_review ORDER BY review_id;
DELETE FROM new_film WHERE name = 'The SQL Adventure';
SELECT * FROM customer_review ORDER BY review_id;
-- Answer: the deleted film's review disappears automatically because of
-- ON DELETE CASCADE. Reviews for the remaining films stay in the table.

