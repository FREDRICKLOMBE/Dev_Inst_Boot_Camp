-- Daily Challenge: Advanced Movie Data Analysis
-- PostgreSQL 17 | Run in pgAdmin's Query Tool on the course Movies database.
-- Execute each numbered query separately to view its result.
-- Course: https://octopus.developers.institute/courses/collection/229/course/1006/section/1528/chapter/3879

-- Task 1. Average film-to-film budget growth by production company.
-- Use consecutive dated releases, breaking same-day ties by movie ID.
-- Skip transitions with a missing or zero budget. Keep companies with
-- no comparable pair in the output, with NULL for their average.
WITH company_films AS (
    SELECT DISTINCT company_id, movie_id
    FROM movies.movie_company
), budgets AS (
    SELECT cf.company_id, m.budget,
           LAG(m.budget) OVER (
               PARTITION BY cf.company_id ORDER BY m.release_date, m.movie_id
           ) AS previous_budget
    FROM company_films AS cf
    JOIN movies.movie AS m USING (movie_id)
    WHERE m.release_date IS NOT NULL
), growth_rates AS (
    SELECT company_id,
           100.0 * (budget::numeric - previous_budget) / previous_budget AS growth_pct
    FROM budgets
    WHERE budget > 0 AND previous_budget > 0
)
SELECT pc.company_name, COUNT(gr.growth_pct) AS comparable_pairs,
       ROUND(AVG(gr.growth_pct), 2) AS average_budget_growth_pct
FROM movies.production_company AS pc
LEFT JOIN growth_rates AS gr USING (company_id)
GROUP BY pc.company_id, pc.company_name
ORDER BY AVG(gr.growth_pct) DESC NULLS LAST, pc.company_name, pc.company_id;

-- Task 2. Actors with the most distinct films rated above the overall mean.
-- Only films with votes enter the mean. Count each film once per actor,
-- regardless of how many roles they played. Return all first-place ties.
WITH rated_movies AS (
    SELECT movie_id, vote_average, AVG(vote_average) OVER () AS overall_average
    FROM movies.movie
    WHERE vote_count > 0 AND vote_average IS NOT NULL
), actor_counts AS (
    SELECT mc.person_id, COUNT(DISTINCT rm.movie_id) AS above_average_movies,
           MAX(rm.overall_average) AS overall_average
    FROM rated_movies AS rm
    JOIN movies.movie_cast AS mc USING (movie_id)
    WHERE rm.vote_average > rm.overall_average AND mc.person_id IS NOT NULL
    GROUP BY mc.person_id
), ranked AS (
    SELECT *, DENSE_RANK() OVER (ORDER BY above_average_movies DESC) AS actor_rank
    FROM actor_counts
)
SELECT p.person_name AS actor, r.above_average_movies,
       ROUND(r.overall_average, 4) AS overall_average_rating
FROM ranked AS r
JOIN movies.person AS p USING (person_id)
WHERE r.actor_rank = 1
ORDER BY actor, p.person_id;

-- Task 3. Rolling average of the current release and two previous releases.
-- The first two rows of each genre use the available history. Keep revenue
-- zero as recorded. AVG skips NULL revenue without changing the 3-row frame.
WITH genre_films AS (
    SELECT DISTINCT genre_id, movie_id FROM movies.movie_genres
)
SELECT g.genre_name, m.title, m.release_date, m.revenue,
       ROUND(AVG(m.revenue) OVER (
           PARTITION BY g.genre_id
           ORDER BY m.release_date, m.movie_id
           ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
       ), 2) AS rolling_average_revenue
FROM genre_films AS gf
JOIN movies.genre AS g USING (genre_id)
JOIN movies.movie AS m USING (movie_id)
WHERE m.release_date IS NOT NULL
ORDER BY g.genre_name, g.genre_id, m.release_date, m.movie_id;

-- Task 4. Highest total revenue by shared keyword.
-- A keyword needs at least two distinct films. Generic tags can win this
-- ranking because the schema has no series field. Show the overall winner
-- and, separately, the explicitly named franchise found in the course tags.
WITH keyword_films AS (
    SELECT DISTINCT keyword_id, movie_id FROM movies.movie_keywords
), window_totals AS (
    SELECT kf.keyword_id, k.keyword_name,
           COUNT(*) OVER by_keyword AS film_count,
           SUM(m.revenue) OVER by_keyword AS total_revenue
    FROM keyword_films AS kf
    JOIN movies.keyword AS k USING (keyword_id)
    JOIN movies.movie AS m USING (movie_id)
    WINDOW by_keyword AS (PARTITION BY kf.keyword_id)
), keyword_totals AS (
    SELECT DISTINCT keyword_id, keyword_name, film_count, total_revenue
    FROM window_totals
    WHERE film_count >= 2 AND total_revenue IS NOT NULL
), ranked AS (
    SELECT *, DENSE_RANK() OVER (ORDER BY total_revenue DESC) AS revenue_rank
    FROM keyword_totals
)
SELECT 'Top shared keyword' AS result_type, keyword_name, film_count, total_revenue
FROM ranked
WHERE revenue_rank = 1
UNION ALL
SELECT 'Named franchise in dataset', keyword_name, film_count, total_revenue
FROM keyword_totals
WHERE LOWER(keyword_name) = 'marvel cinematic universe'
ORDER BY result_type DESC, total_revenue DESC, keyword_name;

-- Results verified against the 4,803-film course dataset:
-- 1. 5,047 companies. APG has the highest computed growth, 142,857,058.48%
--    over two pairs. Its source budgets are 28, 80,000,000 and 25,000,000.
--    The unusually small starting budget drives the result.
-- 2. Samuel L. Jackson, 41 films above the overall mean of 6.1718.
-- 3. 12,160 genre/film rows with rolling averages.
-- 4. Top shared tag: duringcreditsstinger, 307 films, 57,827,617,707.
--    Named franchise tag: marvel cinematic universe, 13 films, 10,138,400,680.
