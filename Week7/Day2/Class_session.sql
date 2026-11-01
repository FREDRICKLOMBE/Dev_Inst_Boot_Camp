-- Create the students table with a unique ID
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INTEGER,
    country VARCHAR(100)
);

-- Insert students; IDs are generated automatically
INSERT INTO students (first_name, last_name, age, country)
VALUES--Creating the items and customers tables

CREATE TABLE items(
	item_id BIGINT GENERATED ALWAYS AS
	IDENTITY PRIMARY KEY,
	item_name VARCHAR(100),
	price NUMERIC(10, 2)
);

CREATE TABLE customers(
	customer_id BIGINT GENERATED ALWAYS AS
	IDENTITY PRIMARY KEY,
	first_name VARCHAR(50),
	last_name VARCHAR(50)
);

--Insert the following in the items table
INSERT INTO items (item_name, price)
VALUES ('Small Desk', 100),
	   ('Large Desk', 300),
	   ('Fan', 80);

--Insert the following in the customers table
INSERT INTO customers (first_name, last_name)
VALUES ('Greg', 'Jones'),
	   ('Sandra', 'Jones'),
	   ('Scott', 'Scott'),
	   ('Trevor', 'Green'),
	   ('Melanie', 'Johnson');

-- Use SQL to fetch the following data from the database:
-- 1. All items
SELECT * 
FROM items;

-- 2. Items priced above 80 (excluding 80)
SELECT * 
FROM items
WHERE price > 80;

-- 3. Items priced at or below 300
SELECT * 
FROM items
WHERE price <= 300;

-- 4. Customers with the last name Smith
SELECT * 
FROM customers
WHERE last_name = 'Smith';
-- Outcome: No rows, based on the customers you inserted.

-- 5. Customers with the last name Jones
SELECT * 
FROM customers
WHERE last_name = 'Jones';
-- Outcome: Greg Jones and Sandra Jones.

-- 6. Customers whose first name is not Scott
SELECT * 
FROM customers
WHERE first_name <> 'Scott';
-- Outcome: Greg, Sandra, Trevor, and Melanie.
    ('Daniel', 'Cohen', 24, 'Israel'),
    ('Anna', 'Kowalski', 29, 'Poland'),
    ('David', 'Levy', 21, 'Israel'),
    ('Maria', 'Garcia', 32, 'Spain'),
    ('Alex', 'Petrov', 27, 'Bulgaria'),
    ('Sarah', 'Miller', 35, 'USA'),
    ('Noa', 'Ben-David', 22, 'Israel'),
    ('Lucas', 'Martin', 26, 'France'),
    ('Emma', 'Schmidt', 31, 'Germany'),
    ('Yuki', 'Tanaka', 25, 'Japan');

-- Create the courses table with a unique ID
CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    hours INTEGER,
    cost NUMERIC(10, 2),
    has_certificate BOOLEAN
);

-- Insert courses; IDs are generated automatically
INSERT INTO courses (title, description, hours, cost, has_certificate)
VALUES
    ('Web Development',
     'Introduction to HTML, CSS and JavaScript',
     120, 5000.00, TRUE),

    ('Python Fundamentals',
     'Programming fundamentals using Python',
     80, 3000.00, TRUE),

    ('SQL and Databases',
     'Introduction to relational databases and SQL',
     40, 3500.00, TRUE);

-- Link students to courses through their IDs
CREATE TABLE student_courses (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(id),
    course_id INTEGER REFERENCES courses(id)
);

-- Display all courses
SELECT * FROM courses;

-- Calculate the average student age
SELECT AVG(age) FROM students;

-- Count all students
SELECT COUNT(*) FROM students;

-- Find the highest student age
SELECT MAX(age) FROM students;

-- Find the lowest student age
SELECT MIN(age) FROM students;

-- Calculate the total of student ages
SELECT SUM(age) FROM students;

-- Calculate the sample standard deviation of ages
SELECT STDDEV(age) FROM students;

-- Calculate the sample variance of ages
SELECT VARIANCE(age) FROM students;

-- Calculate the average course cost
SELECT AVG(cost) FROM courses;

-- Calculate total course hours
SELECT SUM(hours) FROM courses;

-- Calculate total course costs
SELECT SUM(cost) FROM courses;

-- Find the highest course cost
SELECT MAX(cost) FROM courses;

-- Label the highest course cost as max_cost
SELECT MAX(cost) AS max_cost FROM courses;

-- Label the highest student age as oldest
SELECT MAX(age) AS oldest FROM students;

-- Count students from Israel
SELECT COUNT(*)
FROM students
WHERE country = 'Israel';

-- Show countries with more than one student
SELECT country, COUNT(*) AS student_count
FROM students
GROUP BY country
HAVING COUNT(*) > 1;

-- For students older than 22, show country averages above 30
SELECT country, AVG(age) AS average_age
FROM students
WHERE age > 22
GROUP BY country
HAVING AVG(age) > 30
ORDER BY AVG(age) ASC;

-- Combine student first names and course titles, removing duplicates
SELECT first_name FROM students
UNION
SELECT title FROM courses;


-- Add unique IDs to existing rows and future inserts
ALTER TABLE students
ADD COLUMN id SERIAL PRIMARY KEY;

ALTER TABLE courses
ADD COLUMN id SERIAL PRIMARY KEY;

-- Run this after adding both ID columns, if the linking table does not exist
CREATE TABLE student_courses (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(id),
    course_id INTEGER REFERENCES courses(id)
);