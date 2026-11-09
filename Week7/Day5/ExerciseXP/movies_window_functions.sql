-- Movies Database | Window Functions | Exercises XP (PostgreSQL)
-- Open in pgAdmin's Query Tool connected to the database with the movies schema.
-- Run one statement at a time to see each result in Data Output.
-- Source: https://octopus.developers.institute/courses/collection/229/course/1006/section/1528/chapter/3876

-- Exercise 1.1: Popularity rank by genre. Equal scores share a rank.
WITH genre_movies AS (
    SELECT DISTINCT genre_id, movie_id FROM movies.movie_genres
)
SELECT g.genre_name, m.title, m.popularity,
       RANK() OVER (
           PARTITION BY g.genre_id ORDER BY m.popularity DESC NULLS LAST
       ) AS popularity_rank
FROM genre_movies AS gm
JOIN movies.genre AS g USING (genre_id)
JOIN movies.movie AS m USING (movie_id)
WHERE m.popularity IS NOT NULL
ORDER BY g.genre_name, popularity_rank, m.movie_id;

-- Exercise 1.2: The heading asks for the top three. The instructions ask
-- for quartiles. Compute both over all company films, then show the top three.
-- Revenue zero is kept as recorded. A movie ID breaks ties for exactly 3 rows.
WITH company_movies AS (
    SELECT DISTINCT company_id, movie_id FROM movies.movie_company
), ranked AS (
    SELECT pc.company_id, pc.company_name, m.movie_id, m.title, m.revenue,
           NTILE(4) OVER company_revenue AS revenue_quartile,
           ROW_NUMBER() OVER company_revenue AS revenue_position
    FROM company_movies AS cm
    JOIN movies.production_company AS pc USING (company_id)
    JOIN movies.movie AS m USING (movie_id)
    WINDOW company_revenue AS (
        PARTITION BY pc.company_id ORDER BY m.revenue DESC NULLS LAST, m.movie_id
    )
)
SELECT company_name, title, revenue, revenue_quartile, revenue_position
FROM ranked
WHERE revenue_position <= 3 AND revenue IS NOT NULL
ORDER BY company_name, company_id, revenue_position;

-- Exercise 1.3: Running budgets by genre, in release order.
-- Same-day releases are ordered by movie ID. Null budgets add zero.
WITH genre_movies AS (
    SELECT DISTINCT genre_id, movie_id FROM movies.movie_genres
)
SELECT g.genre_name, m.title, m.release_date, m.budget,
       SUM(COALESCE(m.budget, 0)) OVER (
           PARTITION BY g.genre_id
           ORDER BY m.release_date NULLS LAST, m.movie_id
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_total_budget
FROM genre_movies AS gm
JOIN movies.genre AS g USING (genre_id)
JOIN movies.movie AS m USING (movie_id)
ORDER BY g.genre_name, m.release_date NULLS LAST, m.movie_id;

-- Exercise 1.4: Latest dated release per genre. Movie ID breaks date ties.
WITH latest AS (
    SELECT DISTINCT g.genre_id, g.genre_name,
           FIRST_VALUE(m.title) OVER by_release AS title,
           FIRST_VALUE(m.release_date) OVER by_release AS release_date
    FROM movies.movie_genres AS gm
    JOIN movies.genre AS g USING (genre_id)
    JOIN movies.movie AS m USING (movie_id)
    WHERE m.release_date IS NOT NULL
    WINDOW by_release AS (
        PARTITION BY g.genre_id ORDER BY m.release_date DESC, m.movie_id
    )
)
SELECT genre_name, title, release_date FROM latest ORDER BY genre_name, genre_id;

-- Exercise 2.1: Rank actors by number of distinct films. Count one film
-- even if the actor has multiple cast credits for it.
WITH appearances AS (
    SELECT person_id, COUNT(DISTINCT movie_id) AS movie_count
    FROM movies.movie_cast
    WHERE person_id IS NOT NULL AND movie_id IS NOT NULL
    GROUP BY person_id
)
SELECT p.person_name, a.movie_count,
       DENSE_RANK() OVER (ORDER BY a.movie_count DESC) AS appearance_rank
FROM appearances AS a
JOIN movies.person AS p USING (person_id)
ORDER BY appearance_rank, p.person_name, p.person_id;

-- Exercise 2.2: Highest mean rating across each director's rated films.
-- Exclude films without votes. Each film has equal weight. Return all ties.
WITH director_films AS (
    SELECT DISTINCT person_id, movie_id
    FROM movies.movie_crew
    WHERE job = 'Director'
), director_ratings AS (
    SELECT df.person_id, AVG(m.vote_average) AS average_rating
    FROM director_films AS df
    JOIN movies.movie AS m USING (movie_id)
    WHERE m.vote_count > 0 AND m.vote_average IS NOT NULL
    GROUP BY df.person_id
), ranked AS (
    SELECT *, RANK() OVER (ORDER BY average_rating DESC) AS rating_rank
    FROM director_ratings
)
SELECT p.person_name AS director, ROUND(r.average_rating, 2) AS average_rating
FROM ranked AS r
JOIN movies.person AS p USING (person_id)
WHERE r.rating_rank = 1
ORDER BY director, p.person_id;

-- Exercise 2.3: Each actor's revenue grows in film release order.
-- A film contributes once to each credited actor, using its full revenue.
WITH actor_films AS (
    SELECT DISTINCT person_id, movie_id FROM movies.movie_cast
)
SELECT p.person_name AS actor, m.title, m.release_date, m.revenue,
       SUM(COALESCE(m.revenue, 0)) OVER (
           PARTITION BY p.person_id
           ORDER BY m.release_date NULLS LAST, m.movie_id
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS cumulative_revenue
FROM actor_films AS af
JOIN movies.person AS p USING (person_id)
JOIN movies.movie AS m USING (movie_id)
ORDER BY actor, p.person_id, m.release_date NULLS LAST, m.movie_id;

-- Exercise 2.4: Highest total budget across films directed. Return all ties.
WITH director_films AS (
    SELECT DISTINCT person_id, movie_id
    FROM movies.movie_crew
    WHERE job = 'Director'
), budgets AS (
    SELECT df.person_id, SUM(m.budget) AS total_budget
    FROM director_films AS df
    JOIN movies.movie AS m USING (movie_id)
    WHERE m.budget IS NOT NULL
    GROUP BY df.person_id
), ranked AS (
    SELECT *, RANK() OVER (ORDER BY total_budget DESC) AS budget_rank
    FROM budgets
)
SELECT p.person_name AS director, r.total_budget
FROM ranked AS r
JOIN movies.person AS p USING (person_id)
WHERE r.budget_rank = 1
ORDER BY director, p.person_id;

-- Verified with the 4,803-movie course dataset on PostgreSQL 17.
-- E1.1 and E1.3: 12,160 genre/movie rows each.
-- E1.2: 7,362 company/movie rows across the top-three lists.
-- E1.4: 20 genres with a dated release.
-- E2.1: 54,588 ranked actors.
-- E2.2: Gary Sinyor, average rating 10.00. No minimum vote count was required.
-- E2.3: 106,084 actor/movie rows with cumulative revenue.
-- E2.4: Steven Spielberg, total recorded budget 1,667,500,000.
