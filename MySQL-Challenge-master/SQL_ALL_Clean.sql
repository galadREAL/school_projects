-- 1a. Display the first and last names of all actors from the table actor.

SELECT 
    first_name AS 'Actor First Name',
    last_name AS 'Actor Last Name'
FROM
    sakila.actor;
    
    
    
-- 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.

SELECT 
    CONCAT(UPPER(first_name), ' ', UPPER(last_name)) AS 'Full Actor Name in Upper Case'
FROM
    sakila.actor;



-- 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." What is one query would you use to
-- obtain this information?

SELECT 
    actor_id AS 'Actor ID Number',
    first_name AS 'Actor First Name',
    last_name AS 'Actor Last Name'
FROM
    sakila.actor
WHERE
    first_name = 'Joe';



-- 2b. Find all actors whose last name contain the letters GEN:

SELECT 
    *
FROM
    sakila.actor
WHERE
    last_name LIKE '%GEN%';



-- 2c. Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:

SELECT 
    actor_id AS 'Actor ID Number',
    first_name AS 'Actor First Name',
    last_name AS 'Actor Last Name'
FROM
    sakila.actor
WHERE
    last_name LIKE '%LI%'
ORDER BY last_name , first_name;



-- 2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:

SELECT 
    country_id AS 'Country ID Number', country AS 'Country Name'
FROM
    sakila.country
WHERE
    country IN ('Afghanistan' , 'Bangladesh', 'China');



-- 3a. You want to keep a description of each actor. You don't think you will be performing queries on a description, so create a column in the table actor
-- named description and use the data type BLOB (Make sure to research the type BLOB, as the difference between it and VARCHAR are significant).

ALTER TABLE 
	sakila.actor 
ADD 
	description blob;



-- 3b. Very quickly you realize that entering descriptions for each actor is too much effort. Delete the description column.

ALTER TABLE
	sakila.actor 
DROP COLUMN 
	description;



-- 4a. List the last names of actors, as well as how many actors have that last name.

SELECT 
    last_name AS 'Actor Last Name',
    COUNT(last_name) AS 'Count of Actors with Same Last Name'
FROM
    sakila.actor
GROUP BY last_name;



-- 4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors.

SELECT 
    last_name AS 'Actor Last Name',
    COUNT(last_name) AS 'Count of Actors with Same Last Name (Minimum 2)'
FROM
    sakila.actor
GROUP BY last_name
HAVING COUNT(last_name) >= 2;



-- 4c. The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS. Write a query to fix the record.

UPDATE sakila.actor 
SET 
    first_name = 'HARPO',
    last_name = 'WILLIAMS'
WHERE
    first_name = 'GROUCHO'
        AND last_name = 'WILLIAMS';



-- 4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! In a single query, if the first name
-- of the actor is currently HARPO, change it to GROUCHO.

UPDATE sakila.actor 
SET 
    first_name = 'GROUCHO'
WHERE
    first_name = 'HARPO';



-- ! is this right?
-- 5a. You cannot locate the schema of the address table. Which query would you use to re-create it?

SELECT 
    *
FROM
    information_schema.tables
WHERE
    table_name = 'address';
-- !


-- ! maybe add the country also
-- 6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:

SELECT 
    s.first_name AS 'Manager First Name',
    s.last_name AS 'Manager Last Name',
    CONCAT(a.address, ', ', a.district) AS 'Manager Home Address'
FROM
    sakila.staff s
        LEFT JOIN
    sakila.address a ON (s.address_id = a.address_id);



-- ! should I add sales' revenue also?
-- ! maybe add a USD baseline here also
-- 6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.

SELECT 
    first_name AS 'Manager First Nae',
    last_name AS 'Manager Last Name',
    SUM(amount) AS 'Total Amount Rung Up in Rentals ($)'
FROM
    sakila.staff s
        LEFT JOIN
    sakila.payment p ON (s.staff_id = p.staff_id)
WHERE
    payment_date BETWEEN '2005-08-01%' AND '2005-08-31%'
GROUP BY s.last_name , s.first_name;



-- 6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.

SELECT 
    title AS 'Film Title',
    COUNT(actor_id) AS 'Number of Actors Listed'
FROM
    sakila.film f
        INNER JOIN
    sakila.film_actor fa ON (f.film_id = fa.film_id)
GROUP BY f.title;



-- 6d. How many copies of the film Hunchback Impossible exist in the inventory system?

SELECT 
    COUNT(film_id) AS 'Copies of Hunchback Impossible in Inventory System'
FROM
    inventory
WHERE
    film_id IN (SELECT 
            film_id
        FROM
            sakila.film
        WHERE
            title = 'Hunchback Impossible');



-- ! maybe add USD baseline here
-- 6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name:

SELECT 
    last_name AS 'Customer Last Name',
    first_name AS 'Customer First Name',
    SUM(amount) AS 'Amount Spent ($)'
FROM
    sakila.customer c
        JOIN
    sakila.payment p ON (c.customer_id = p.customer_id)
GROUP BY c.customer_id
ORDER BY c.last_name;



-- 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, films starting with the letters K and Q
-- have also soared in popularity. Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.

SELECT 
    title AS 'English Language Movies Starting with K or Q'
FROM
    sakila.film
WHERE
    language_id = (SELECT 
            language_id
        FROM
            sakila.language
        WHERE
            name = 'English')
        AND title LIKE 'K%'
        OR title LIKE 'Q%';



-- 7b. Use subqueries to display all actors who appear in the film Alone Trip.

SELECT 
    last_name AS 'Actor Last Name',
    first_name AS 'Actor First Name'
FROM
    sakila.actor
WHERE
    actor_id IN (SELECT 
            actor_id
        FROM
            sakila.film_actor
        WHERE
            film_id = (SELECT 
                    film_id
                FROM
                    sakila.film
                WHERE
                    title = 'Alone Trip'));



-- 7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to
-- retrieve this information.

SELECT 
    last_name AS 'Canadian Customer Last Name',
    first_name AS 'Canadian Customer First Name',
    email AS 'Canadian Customer Email'
FROM
    sakila.customer c
        JOIN
    sakila.customer_list cl ON (c.customer_id = cl.ID)
WHERE
    cl.country = 'Canada';



-- 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as family films.

SELECT 
    film_id AS 'Family Film ID Number',
    title AS 'Family Film Title',
    description AS 'Family Film Description',
    release_year AS 'Family Film Release Year',
    rental_duration AS 'Family Film Rental Duration',
    rental_rate AS 'Family Film Rental Rate',
    length AS 'Family Film Length (Minutes)',
    rating AS 'Family Film Rating',
    special_features AS 'Family Film Special Features'
FROM
    sakila.film
WHERE
    film_id IN (SELECT 
            film_id
        FROM
            sakila.film_category
        WHERE
            category_id = (SELECT 
                    category_id
                FROM
                    sakila.category
                WHERE
                    name = 'Family'));



-- 7e. Display the most frequently rented movies in descending order.

SELECT 
    COUNT(i.film_id) AS 'Number of Rentals (DSC)',
    f.film_id AS 'Film ID Number',
    f.title AS 'Film Title',
    f.description AS 'Film Description',
    f.release_year AS 'Film Release Year',
    f.rental_duration AS 'Film Rental Duration',
    f.rental_rate AS 'Film Rental Rate',
    f.length AS 'Film Length (Minutes)',
    f.rating AS 'Film Rating',
    f.special_features AS 'Film Special Features'
FROM
    sakila.rental r
        LEFT JOIN
    sakila.inventory i ON (r.inventory_id = i.inventory_id)
        LEFT JOIN
    sakila.film f ON (i.film_id = f.film_id)
GROUP BY i.film_id
ORDER BY COUNT(i.film_id) DESC;



-- 7f. Write a query to display how much business, in dollars, each store brought in.
-- This works but an easier way prob is exist:
CREATE VIEW store_aus AS
    SELECT 
        store AS 'Store Location',
        (total_sales * .72) + (SELECT 
                (SUM(amount) * .72)
            FROM
                sakila.payment
            WHERE
                staff_id = (SELECT 
                        ID
                    FROM
                        sakila.staff_list
                    WHERE
                        name = 'Jon Stephens')) AS 'Total Business ($USD)'
    FROM
        sakila.sales_by_store
    WHERE
        manager = 'Jon Stephens';CREATE VIEW store_can AS
    SELECT 
        store AS 'Store Location',
        (total_sales * .75) + (SELECT 
                (SUM(amount) * .75)
            FROM
                sakila.payment
            WHERE
                staff_id = (SELECT 
                        ID
                    FROM
                        sakila.staff_list
                    WHERE
                        name = 'Mike Hillyer')) AS 'Total Business ($USD)'
    FROM
        sakila.sales_by_store
    WHERE
        manager = 'Mike Hillyer';SELECT 
    *
FROM
    store_aus 
UNION SELECT 
    *
FROM
    store_can;

-- ! maybe add:: case when address.city_id = city.city_id then address.city_id else '' end as locale) :: and country
-- This works and did not end up being easier (way more dynamic and informative though!):
SELECT 
    s.store_id AS 'Store ID Number',
    (SELECT 
            CASE
                    WHEN
                        s.store_id = '1'
                    THEN
                        (SELECT 
                                CONCAT(address, ', ', district)
                            FROM
                                sakila.address
                            WHERE
                                address_id = '1')
                    WHEN
                        s.store_id = '2'
                    THEN
                        (SELECT 
                                CONCAT(address, ', ', district)
                            FROM
                                sakila.address
                            WHERE
                                address_id = '2')
                    ELSE 'Error (Unknown Locale)'
                END AS locale
        ) AS 'Store Address',
    s.staff_id AS 'Manager ID Number',
    CONCAT(s.first_name, ' ', s.last_name) AS 'Manager Full Name',
    SUM(amount) AS 'Rentals Revenue ($)',
    (SELECT 
            total_sales
        FROM
            sakila.sales_by_store
        WHERE
            manager = CONCAT(s.first_name, ' ', s.last_name)) AS 'Sales Revenue ($)',
    (SUM(amount) + (SELECT 
            total_sales
        FROM
            sakila.sales_by_store
        WHERE
            manager = CONCAT(s.first_name, ' ', s.last_name))) AS 'Total Business ($)',
    (SELECT 
            CASE
                    WHEN s.store_id = '1' THEN '$1 CAD = $0.75 USD'
                    WHEN s.store_id = '2' THEN '$1 AUD = $0.72 USD'
                    ELSE 'Error (Unknown Locale Currency >> USD Exchange Rate)'
                END AS locale
        ) AS 'Exchange Rate',
    ROUND(((SUM(amount) + (SELECT 
                    total_sales
                FROM
                    sakila.sales_by_store
                WHERE
                    manager = CONCAT(s.first_name, ' ', s.last_name))) * (SELECT 
                    CASE
                            WHEN s.store_id = '1' THEN '.75'
                            WHEN s.store_id = '2' THEN '.72'
                            ELSE 'Error (Unknown Country)'
                        END AS locale
                )),
            2) AS 'Total Business ($USD)'
FROM
    sakila.customer c
        JOIN
    sakila.payment p ON (c.customer_id = p.customer_id)
        JOIN
    sakila.staff s ON (p.staff_id = s.staff_id)
GROUP BY s.staff_id;



-- ! maybe add:: case when address.city_id = city.city_id then address.city_id else '' end as locale) :: and country
-- 7g. Write a query to display for each store its store ID, city, and country.
-- -- -- -- -- using code from above -- -- -- -- --
SELECT 
    store_id AS 'Store ID Number',
    (SELECT 
            CASE
                    WHEN
                        store_id = '1'
                    THEN
                        (SELECT 
                                CONCAT(address, ', ', district)
                            FROM
                                sakila.address
                            WHERE
                                address_id = '1')
                    WHEN
                        store_id = '2'
                    THEN
                        (SELECT 
                                CONCAT(address, ', ', district)
                            FROM
                                sakila.address
                            WHERE
                                address_id = '2')
                    ELSE 'Error (Unknown Locale)'
                END AS locale
        ) AS 'Store Address'
FROM
    sakila.staff
GROUP BY staff_id;



-- 7h. List the top five genres in gross revenue in descending order. (Hint: you may need to use the following tables: category, film_category, inventory,
-- payment, and rental.)

CREATE VIEW genres_aus AS
    SELECT 
        c.name,
        r.staff_id,
        SUM(p.amount) AS 'Gross_Rev_Raw',
        ROUND(SUM(p.amount) * (SELECT 
                        CASE
                                WHEN r.staff_id = '1' THEN '.75'
                            END AS locale
                    ),
                2) AS 'Gross_Rev_USD'
    FROM
        sakila.rental r
            JOIN
        sakila.payment p ON (r.rental_id = p.rental_id)
            JOIN
        sakila.inventory i ON (r.inventory_id = i.inventory_id)
            JOIN
        sakila.film_category fc ON (i.film_id = fc.film_id)
            JOIN
        category c ON (fc.category_id = c.category_id)
    GROUP BY c.name , r.staff_id
    HAVING Gross_Rev_USD >= 1
    ORDER BY ROUND(SUM(p.amount) * (SELECT 
                    CASE
                            WHEN r.staff_id = '1' THEN '.75'
                            ELSE 'Error (Unknown Country)'
                        END AS locale
                ),
            2) DESC;CREATE VIEW genres_can AS
    SELECT 
        c.name,
        r.staff_id,
        SUM(p.amount) AS 'Gross_Rev_Raw',
        ROUND(SUM(p.amount) * (SELECT 
                        CASE
                                WHEN r.staff_id = '2' THEN '.72'
                            END AS locale
                    ),
                2) AS 'Gross_Rev_USD'
    FROM
        sakila.rental r
            JOIN
        sakila.payment p ON (r.rental_id = p.rental_id)
            JOIN
        sakila.inventory i ON (r.inventory_id = i.inventory_id)
            JOIN
        sakila.film_category fc ON (i.film_id = fc.film_id)
            JOIN
        category c ON (fc.category_id = c.category_id)
    GROUP BY c.name , r.staff_id
    HAVING Gross_Rev_USD >= 1
    ORDER BY ROUND(SUM(p.amount) * (SELECT 
                    CASE
                            WHEN r.staff_id = '2' THEN '.72'
                            ELSE 'Error (Unknown Country)'
                        END AS locale
                ),
            2) DESC;SELECT 
    (SELECT 
            CASE
                    WHEN ga.name = gc.name THEN ga.name
                    ELSE ''
                END AS locale
        ) AS 'Validated_Genre',
    (ga.Gross_Rev_USD + gc.Gross_Rev_USD) AS 'Total_Gross_Rev_USD'
FROM
    genres_aus ga
        JOIN
    genres_can gc ON (ga.name = gc.name)
WHERE
    (SELECT 
            CASE
                    WHEN ga.name = gc.name THEN ga.name
                    ELSE ''
                END AS locale
        ) IS NOT NULL
ORDER BY Total_Gross_Rev_USD DESC
LIMIT 5;



-- 8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. Use the solution from the problem 
-- above to create a view. If you haven't solved 7h, you can substitute another query to create a view.
-- -- -- -- -- using code from above -- -- -- -- --
CREATE VIEW Top_5_Earners AS
    SELECT 
        (SELECT 
                CASE
                        WHEN ga.name = gc.name THEN ga.name
                        ELSE ''
                    END AS locale
            ) AS 'Validated_Genre',
        (ga.Gross_Rev_USD + gc.Gross_Rev_USD) AS 'Total_Gross_Rev_USD'
    FROM
        genres_aus ga
            JOIN
        genres_can gc ON (ga.name = gc.name)
    WHERE
        (SELECT 
                CASE
                        WHEN ga.name = gc.name THEN ga.name
                        ELSE ''
                    END AS locale
            ) IS NOT NULL
    ORDER BY Total_Gross_Rev_USD DESC
    LIMIT 5;

SELECT 
    *
FROM
    Top_5_Earners;



-- 8b. How would you display the view that you created in 8a?
-- -- -- -- -- using code from above -- -- -- -- --
SELECT 
    *
FROM
    Top_5_Earners;



-- 8c. You find that you no longer need the view top_five_genres. Write a query to delete it.
DROP VIEW
	Top_5_Earners;