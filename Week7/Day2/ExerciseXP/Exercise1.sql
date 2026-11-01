-- 1. All items, cheapest first.
SELECT *
FROM items
ORDER BY item_price ASC;

-- 2. Items costing at least 80, most expensive first.
SELECT *
FROM items
WHERE item_price >= 80
ORDER BY item_price DESC;

-- 3. First three customers alphabetically, excluding the primary key.
SELECT first_name, last_name
FROM customers
ORDER BY first_name ASC, last_name ASC
LIMIT 3;

-- 4. Only last names, in reverse alphabetical order.
SELECT last_name
FROM customers
ORDER BY last_name DESC;