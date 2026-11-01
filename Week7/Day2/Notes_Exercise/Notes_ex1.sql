-- Inserting more values in the table
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES
    ('James', 'Walker', '1981-03-15', 2),
    ('Emma', 'Bennett', '1994-07-22', 1),
    ('Daniel', 'Brooks', '1975-01-10', 3),
    ('Olivia', 'Hayes', '1998-05-18', 0),
    ('Michael', 'Reed', '1966-09-03', 4),
    ('Sophia', 'Collins', '1987-02-27', 2),
    ('David', 'Morgan', '1979-06-12', 1),
    ('Isabella', 'Parker', '2000-08-25', 0),
    ('Alexander', 'Scott', '1972-04-09', 3),
    ('Mia', 'Turner', '1991-11-14', 1),
    ('William', 'Carter', '1984-03-30', 0),
    ('Charlotte', 'Mitchell', '1968-12-05', 2),
    ('Benjamin', 'Phillips', '1995-01-21', 0),
    ('Amelia', 'Foster', '1982-07-08', 1),
    ('Lucas', 'Harrison', '1989-05-16', 2),
    ('Harper', 'Sullivan', '1997-09-29', 0),
    ('Henry', 'Coleman', '1963-02-11', 3),
    ('Evelyn', 'Richardson', '1977-06-24', 1),
    ('Samuel', 'Bailey', '1992-08-07', 0),
    ('Grace', 'Anderson', '1970-04-19', 2);

-- Get the average number of oscars in the table
SELECT AVG(number_oscars) AS average_oscar
FROM actors

--To get one actor for each distinct number of Oscars
SELECT DISTINCT ON (number_oscars)
       first_name, last_name, number_oscars
FROM actors
ORDER BY number_oscars, last_name, first_name;

--Get distinct actors depending on their number of oscars
SELECT DISTINCT number_oscars
FROM actors
ORDER BY number_oscars;

--Get the actors born after 01/01/1970
SELECT *
FROM actors 
WHERE age > DATE '01-01-1970'

-- Get actors whose first or last name is David, Morgan, or Will
SELECT *
FROM actors
WHERE first_name IN ('David', 'Morgan', 'Will')
   OR last_name IN ('David', 'Morgan', 'Will');
