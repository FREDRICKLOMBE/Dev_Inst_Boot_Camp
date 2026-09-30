--Creating the items and customers tables

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