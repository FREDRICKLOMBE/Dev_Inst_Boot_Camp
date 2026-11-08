-- Day 2, Exercise 2: DVD Rental
-- Questions 8 and 9 use Inception as an example favorite movie.

-- 1. All customer columns.
SELECT * FROM customer;

-- 2. Full name.
SELECT first_name || ' ' || last_name AS full_name FROM customer;

-- 3. Distinct creation dates.
SELECT DISTINCT create_date FROM customer ORDER BY create_date;

-- 4. Customers by descending first name.
SELECT * FROM customer ORDER BY first_name DESC, customer_id;

-- 5. Films by ascending rental rate.
SELECT film_id, title, description, release_year, rental_rate
FROM film ORDER BY rental_rate, film_id;

-- 6. Addresses and phones of customers in Texas.
SELECT a.address, a.phone
FROM customer AS c JOIN address AS a ON a.address_id = c.address_id
WHERE a.district = 'Texas' ORDER BY c.customer_id;

-- 7. Films 15 and 150.
SELECT * FROM film WHERE film_id IN (15, 150) ORDER BY film_id;

-- 8. Favorite movie (replace Inception with your choice).
SELECT film_id, title, description, length, rental_rate
FROM film WHERE title ILIKE 'Inception';

-- 9. Match the first two letters of the same movie.
SELECT film_id, title, description, length, rental_rate
FROM film WHERE title ILIKE 'In%' ORDER BY title;

-- 10. First ten cheapest films; film_id breaks price ties.
SELECT film_id, title, rental_rate FROM film
ORDER BY rental_rate, film_id LIMIT 10;

-- 11. Next ten cheapest films.
SELECT film_id, title, rental_rate FROM film
ORDER BY rental_rate, film_id LIMIT 10 OFFSET 10;

-- 11 bonus. Same page without LIMIT.
SELECT film_id, title, rental_rate FROM film
ORDER BY rental_rate, film_id OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY;

-- 12. Every payment with customer names, ordered by customer ID.
SELECT c.first_name, c.last_name, p.amount, p.payment_date
FROM customer AS c JOIN payment AS p ON p.customer_id = c.customer_id
ORDER BY c.customer_id, p.payment_date, p.payment_id;

-- 13. Films with no inventory records.
SELECT f.* FROM film AS f
WHERE NOT EXISTS (SELECT 1 FROM inventory AS i WHERE i.film_id = f.film_id)
ORDER BY f.film_id;

-- 14. Cities and their countries.
SELECT ci.city, co.country
FROM city AS ci JOIN country AS co ON co.country_id = ci.country_id
ORDER BY co.country, ci.city;

-- 15 bonus. Customer payments ordered by staff ID.
SELECT p.staff_id, c.customer_id, c.first_name, c.last_name,
       p.amount, p.payment_date
FROM customer AS c JOIN payment AS p ON p.customer_id = c.customer_id
ORDER BY p.staff_id, c.customer_id, p.payment_date, p.payment_id;
