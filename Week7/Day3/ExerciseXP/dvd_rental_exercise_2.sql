-- Exercises XP: Database Concepts #2 - DVD Rental - Exercise 2
-- Source: https://octopus.developers.institute/courses/collection/229/course/1006/section/1658/chapter/395
-- Run in pgAdmin Query Tool connected to the PostgreSQL dvdrental database.
-- Dependencies: dvdrental_backup.tar and a completed, committed Exercise 1.
-- Use the same database and schema as Exercise 1.
-- Question 3 drops the customer_review table created by Exercise 1.
-- The film-language update in question 1 is rolled back.

-- 1. Change some film languages using a language that actually exists.
-- Transaction rolled back to preserve the original dataset for later questions.
BEGIN;
UPDATE film
SET language_id = (SELECT language_id FROM language WHERE name = 'French'),
    last_update = CURRENT_TIMESTAMP
WHERE film_id IN (SELECT film_id FROM film ORDER BY film_id LIMIT 3)
  AND EXISTS (SELECT 1 FROM language WHERE name = 'French')
RETURNING film_id, title, language_id;
ROLLBACK;
-- Use COMMIT instead of ROLLBACK if you want to retain this practice change.

-- 2. Inspect the customer table's actual foreign keys.
SELECT con.conname AS constraint_name,
       pg_get_constraintdef(con.oid) AS definition
FROM pg_constraint AS con
WHERE con.conrelid = 'customer'::regclass AND con.contype = 'f'
ORDER BY con.conname;
-- In the standard DVD Rental schema, customer.address_id references
-- address.address_id and customer.store_id references store.store_id.
-- INSERTs must use existing referenced IDs; otherwise they fail. Insert the
-- address/store parent rows first when needed. Other NOT NULL constraints
-- still apply independently of foreign keys.

-- 3. Drop reviews. The outgoing FKs do not prevent dropping this child table.
-- Check incoming foreign-key references before dropping it:
SELECT con.conrelid::regclass AS referencing_table, con.conname,
       pg_get_constraintdef(con.oid) AS definition
FROM pg_constraint AS con
WHERE con.confrelid = 'customer_review'::regclass AND con.contype = 'f';
-- This deletes the table and its data. Default RESTRICT refuses the drop if
-- dependent objects exist. Avoid CASCADE unless you intend to remove them.
DROP TABLE customer_review;

-- 4. Count outstanding rental transactions.
SELECT COUNT(*) AS outstanding_rentals
FROM rental
WHERE return_date IS NULL;

-- 5. The 30 most expensive distinct films with outstanding rentals.
-- Interpret 'expensive movies' as highest DVD replacement_cost.
-- EXISTS avoids repeating a film for multiple outstanding copies.
SELECT f.film_id, f.title, f.replacement_cost, f.rental_rate
FROM film AS f
WHERE EXISTS (
    SELECT 1
    FROM inventory AS i
    JOIN rental AS r ON r.inventory_id = i.inventory_id
    WHERE i.film_id = f.film_id AND r.return_date IS NULL
)
ORDER BY f.replacement_cost DESC, f.title, f.film_id
LIMIT 30;
-- If 'expensive' means rental price, order by f.rental_rate DESC instead.

-- 6.1. Sumo wrestler film starring Penelope Monroe.
SELECT DISTINCT f.film_id, f.title, f.description
FROM film AS f
JOIN film_actor AS fa ON fa.film_id = f.film_id
JOIN actor AS a ON a.actor_id = fa.actor_id
WHERE a.first_name ILIKE 'Penelope'
  AND a.last_name ILIKE 'Monroe'
  AND f.description ILIKE '%sumo%'
ORDER BY f.title;

-- 6.2. Documentary shorter than 60 minutes, rated R.
SELECT f.film_id, f.title, f.length, f.rating
FROM film AS f
JOIN film_category AS fc ON fc.film_id = f.film_id
JOIN category AS c ON c.category_id = fc.category_id
WHERE c.name = 'Documentary' AND f.length < 60 AND f.rating = 'R'
ORDER BY f.title;

-- 6.3. Matthew Mahan paid over $4 for a rental returned July 28-August 1, 2005.
-- Half-open interval includes all of August 1. Sum payments per rental.
SELECT f.film_id, f.title, r.rental_id, r.return_date,
       SUM(p.amount) AS amount_paid
FROM customer AS c
JOIN rental AS r ON r.customer_id = c.customer_id
JOIN inventory AS i ON i.inventory_id = r.inventory_id
JOIN film AS f ON f.film_id = i.film_id
JOIN payment AS p ON p.rental_id = r.rental_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
  AND r.return_date >= TIMESTAMP '2005-07-28'
  AND r.return_date < TIMESTAMP '2005-08-02'
GROUP BY f.film_id, f.title, r.rental_id, r.return_date
HAVING SUM(p.amount) > 4.00
ORDER BY f.title, r.rental_id;

-- 6.4. Matthew rented a film containing 'boat' in its title or description.
-- Rank candidates by replacement cost; the most expensive appears first.
-- No numeric threshold is supplied, so retain all matches for comparison.
SELECT DISTINCT f.film_id, f.title, f.description, f.replacement_cost
FROM customer AS c
JOIN rental AS r ON r.customer_id = c.customer_id
JOIN inventory AS i ON i.inventory_id = r.inventory_id
JOIN film AS f ON f.film_id = i.film_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
  AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC, f.title;
