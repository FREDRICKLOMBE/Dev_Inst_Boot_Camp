-- Daily Challenge: Tables Relationships
-- PostgreSQL solution. Run the entire file in pgAdmin's Query Tool.
-- A dedicated schema avoids conflicts with existing customer/book tables.
-- Run once; if this schema already exists, choose a new schema name below.
BEGIN;
CREATE SCHEMA daily_challenge_relationships;
SET LOCAL search_path TO daily_challenge_relationships;

-- PART I.1: A customer has zero or one profile; each profile has one customer.
-- UNIQUE prevents multiple profiles for one customer. NOT NULL prevents
-- profiles without an owner. A customer may have no profile (as Lea does).
CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL
);
CREATE TABLE customer_profile (
    id SERIAL PRIMARY KEY,
    "isLoggedIn" BOOLEAN NOT NULL DEFAULT FALSE,
    customer_id INTEGER NOT NULL UNIQUE REFERENCES customer(id)
);
-- Quoting preserves the exact mixed-case column name requested by the page.

-- PART I.2: Insert the three requested customers.
INSERT INTO customer (first_name, last_name)
VALUES ('John', 'Doe'), ('Jerome', 'Lalu'), ('Lea', 'Rive');

-- PART I.3: Scalar subqueries find IDs instead of assuming sequence values.
INSERT INTO customer_profile ("isLoggedIn", customer_id)
VALUES (TRUE, (SELECT id FROM customer
               WHERE first_name = 'John' AND last_name = 'Doe'));
-- Omit isLoggedIn to demonstrate its DEFAULT FALSE value for Jerome.
INSERT INTO customer_profile (customer_id)
VALUES ((SELECT id FROM customer
         WHERE first_name = 'Jerome' AND last_name = 'Lalu'));

-- PART I.4.a: Only logged-in customers. Expected: John.
SELECT c.first_name
FROM customer AS c
JOIN customer_profile AS cp ON cp.customer_id = c.id
WHERE cp."isLoggedIn" IS TRUE
ORDER BY c.id;

-- PART I.4.b: LEFT JOIN retains Lea even though she has no profile.
-- Expected: John/true, Jerome/false, Lea/NULL.
-- Leave NULL visible here so an absent profile is distinguishable from false.
SELECT c.first_name, cp."isLoggedIn"
FROM customer AS c
LEFT JOIN customer_profile AS cp ON cp.customer_id = c.id
ORDER BY c.id;

-- PART I.4.c: Treat absence of a profile as not logged in. Expected: 2.
-- IS NOT TRUE includes both FALSE (Jerome) and NULL (Lea).
SELECT COUNT(*) AS customers_not_logged_in
FROM customer AS c
LEFT JOIN customer_profile AS cp ON cp.customer_id = c.id
WHERE cp."isLoggedIn" IS NOT TRUE;
-- If counting only profiles explicitly marked FALSE, the result is 1:
SELECT COUNT(*) AS profiles_explicitly_logged_out
FROM customer AS c
JOIN customer_profile AS cp ON cp.customer_id = c.id
WHERE cp."isLoggedIn" IS FALSE;

-- PART II.1-2: Books and the supplied sample data.
CREATE TABLE book (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL
);
INSERT INTO book (title, author) VALUES
    ('Alice In Wonderland', 'Lewis Carroll'),
    ('Harry Potter', 'J.K Rowling'),
    ('To kill a mockingbird', 'Harper Lee');

-- PART II.3-4: CHECK enforces age <= 15; the lower bound rejects negative ages.
-- NOT NULL also prevents an unknown age from bypassing the CHECK.
CREATE TABLE student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    age INTEGER NOT NULL CHECK (age BETWEEN 0 AND 15)
);
INSERT INTO student (name, age) VALUES
    ('John', 12), ('Lera', 11), ('Patrick', 10), ('Bob', 14);

-- PART II.5: Junction table for the many-to-many relationship.
-- The page alternates between student_id and student_fk_id; this solution
-- uses student_fk_id, as specified in its foreign-key explanation.
-- The composite PK permits each student/book pair only once.
CREATE TABLE library (
    book_fk_id INTEGER REFERENCES book(book_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    student_fk_id INTEGER REFERENCES student(student_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    borrowed_date DATE NOT NULL,
    PRIMARY KEY (book_fk_id, student_fk_id)
);
-- A composite PK implicitly makes both foreign-key columns NOT NULL.

-- PART II.6: Subqueries resolve the IDs. ISO dates avoid locale ambiguity.
INSERT INTO library (book_fk_id, student_fk_id, borrowed_date) VALUES
    ((SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
     (SELECT student_id FROM student WHERE name = 'John'), DATE '2022-02-15'),
    ((SELECT book_id FROM book WHERE title = 'To kill a mockingbird'),
     (SELECT student_id FROM student WHERE name = 'Bob'), DATE '2021-03-03'),
    ((SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
     (SELECT student_id FROM student WHERE name = 'Lera'), DATE '2021-05-23'),
    ((SELECT book_id FROM book WHERE title = 'Harry Potter'),
     (SELECT student_id FROM student WHERE name = 'Bob'), DATE '2021-08-12');

-- PART II.7.a: All columns from the junction table. Expected: four rows.
SELECT * FROM library ORDER BY student_fk_id, book_fk_id;

-- PART II.7.b: Display student names with borrowed book titles.
SELECT s.name AS student_name, b.title AS book_title
FROM library AS l
JOIN student AS s ON s.student_id = l.student_fk_id
JOIN book AS b ON b.book_id = l.book_fk_id
ORDER BY s.name, b.title;
-- Expected: Bob/Harry Potter; Bob/To kill a mockingbird;
-- John/Alice In Wonderland; Lera/Alice In Wonderland.

-- PART II.7.c: Alice borrowers are John (12) and Lera (11). Average: 11.5.
SELECT AVG(s.age) AS average_age
FROM library AS l
JOIN student AS s ON s.student_id = l.student_fk_id
JOIN book AS b ON b.book_id = l.book_fk_id
WHERE b.title = 'Alice In Wonderland';

-- Validate the main expected results. Any mismatch aborts the transaction.
DO $$
BEGIN
    IF (SELECT COUNT(*) FROM library) <> 4 THEN
        RAISE EXCEPTION 'Expected four borrowing records';
    END IF;
    IF (SELECT COUNT(*) FROM customer AS c
        LEFT JOIN customer_profile AS cp ON cp.customer_id = c.id
        WHERE cp."isLoggedIn" IS NOT TRUE) <> 2 THEN
        RAISE EXCEPTION 'Expected two customers not logged in';
    END IF;
    IF (SELECT AVG(s.age) FROM library AS l
        JOIN student AS s ON s.student_id = l.student_fk_id
        JOIN book AS b ON b.book_id = l.book_fk_id
        WHERE b.title = 'Alice In Wonderland') IS DISTINCT FROM 11.5 THEN
        RAISE EXCEPTION 'Expected average age of 11.5';
    END IF;
END $$;

-- PART II.7.d: Delete Bob to demonstrate ON DELETE CASCADE.
-- SAVEPOINT lets us demonstrate the deletion, then restore Bob and his loans.
SAVEPOINT cascade_demo;
DELETE FROM student WHERE name = 'Bob' RETURNING student_id, name;
SELECT l.*, s.name, b.title
FROM library AS l
JOIN student AS s ON s.student_id = l.student_fk_id
JOIN book AS b ON b.book_id = l.book_fk_id
ORDER BY s.name, b.title;
-- Expected: only John's and Lera's rows remain. Bob's two borrowing rows
-- were automatically deleted; the book records themselves remain unchanged.
DO $$
BEGIN
    IF (SELECT COUNT(*) FROM library) <> 2 THEN
        RAISE EXCEPTION 'Cascade should leave two borrowing records';
    END IF;
    IF (SELECT COUNT(*) FROM book) <> 3 THEN
        RAISE EXCEPTION 'Deleting a student must not delete books';
    END IF;
END $$;
ROLLBACK TO SAVEPOINT cascade_demo;
RELEASE SAVEPOINT cascade_demo;
-- Bob and all four borrowing records are restored before saving the solution.
COMMIT;
-- For later queries, qualify tables with daily_challenge_relationships,
-- or run SET search_path TO daily_challenge_relationships;
