# Daily Challenge: Tables Relationships

## Run the solution
Open `tables_relationships.sql` in pgAdmin's Query Tool connected to a PostgreSQL database, then run the whole script. It creates a dedicated schema named `daily_challenge_relationships` and commits the sample tables and rows. Use a new schema name if that schema already exists. No existing tables are dropped.

The code includes comments for every assignment step, result checks, and a reversible demonstration of cascading deletion.

## Expected answers

- Logged-in customers: **John**.
- All customers and login state: **John = true; Jerome = false; Lea = NULL**, because Lea has no profile.
- Customers not logged in, including customers without a profile: **2** (Jerome and Lea). If the instructor means only profiles explicitly set to false, that count is **1** (Jerome); both queries are included.
- Borrowings: **John → Alice In Wonderland (2022-02-15); Bob → To kill a mockingbird (2021-03-03); Lera → Alice In Wonderland (2021-05-23); Bob → Harry Potter (2021-08-12)**.
- Average age of Alice In Wonderland borrowers: **11.5**.
- Deleting Bob automatically deletes his **two library rows**, because the student foreign key has `ON DELETE CASCADE`. The three books and the other students' borrowings remain. The script rolls back this demonstration so the complete sample data is retained.

## Relationship design

`customer_profile.customer_id` is both UNIQUE and NOT NULL and references `customer.id`. This enforces at most one profile per customer and exactly one owner per profile. Customers can exist without profiles, which is required by the Lea example.

`library` uses `(book_fk_id, student_fk_id)` as its composite primary key, and both foreign keys cascade deletes and updates. This follows the requested design, which allows each student/book pair only once; a real borrowing-history system would need a different key to record repeat loans of the same book by the same student.

The page uses both `student_id` and `student_fk_id` for the junction column. The solution consistently uses `student_fk_id`, following the page's detailed foreign-key description.

## Verification status

The solution was reviewed against every requirement on the assignment page. Expected results are derived from the supplied sample rows. It has not been executed against a PostgreSQL server here; the included SQL assertions check key results when you run it.

Source: https://octopus.developers.institute/courses/collection/229/course/1006/section/1658/chapter/400
