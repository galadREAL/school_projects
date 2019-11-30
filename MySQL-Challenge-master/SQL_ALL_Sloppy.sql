-- 1a. Display the first and last names of all actors from the table actor.

-- SELECT first_name, last_name FROM sakila.actor
    
    
    
-- 1b. Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.

-- select concat(upper(first_name), ' ', upper(last_name)) as 'Actor Name' from sakila.actor



-- 2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." What is one query would you use to
-- obtain this information?

-- select actor_id, first_name, last_name from sakila.actor where first_name = 'Joe'



-- 2b. Find all actors whose last name contain the letters GEN:

-- select * from sakila.actor where last_name like '%GEN%'



-- 2c. Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:

-- select * from sakila.actor where last_name like '%LI%' order by last_name, first_name



-- 2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:

-- select country_id, country from sakila.country where country in ('Afghanistan', 'Bangladesh', 'China')



-- 3a. You want to keep a description of each actor. You don't think you will be performing queries on a description, so create a column in the table actor
-- named description and use the data type BLOB (Make sure to research the type BLOB, as the difference between it and VARCHAR are significant).

-- alter table sakila.actor add description blob



-- 3b. Very quickly you realize that entering descriptions for each actor is too much effort. Delete the description column.

-- alter table sakila.actor drop column description



-- 4a. List the last names of actors, as well as how many actors have that last name.

-- select last_name, count(last_name) from sakila.actor group by last_name



-- 4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors.

-- select last_name, count(last_name) from sakila.actor group by last_name having count(last_name) >= 2



-- 4c. The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS. Write a query to fix the record.

-- update sakila.actor set first_name = 'HARPO', last_name = 'WILLIAMS' where first_name = 'GROUCHO' and last_name = 'WILLIAMS'



-- 4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! In a single query, if the first name
-- of the actor is currently HARPO, change it to GROUCHO.

-- update sakila.actor set first_name = 'GROUCHO' where first_name = 'HARPO'



-- ! not finding much with google-fu
-- 5a. You cannot locate the schema of the address table. Which query would you use to re-create it?

-- select * from information_schema.tables where table_name = 'address'
-- !



-- 6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:

-- select s.first_name, s.last_name, a.address from sakila.staff s left join sakila.address a on (s.address_id = a.address_id)


-- ! add sales also?
-- 6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.

-- select first_name, last_name, sum(amount) from sakila.staff s left join sakila.payment p on (s.staff_id = p.staff_id) where payment_date between '2005-08-01%' and '2005-08-31%' group by s.last_name, s.first_name



-- 6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.

-- select title, count(actor_id) from sakila.film f inner join sakila.film_actor fa on (f.film_id = fa.film_id) group by f.title



-- 6d. How many copies of the film Hunchback Impossible exist in the inventory system?

-- select count(film_id) as 'Copies of Hunchback Impossible in Inventory System' from inventory where film_id in (select film_id from sakila.film where title = 'Hunchback Impossible')



-- 6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name:

-- select last_name, first_name, sum(amount) from sakila.customer c join sakila.payment p on (c.customer_id = p.customer_id) group by c.customer_id order by c.last_name



-- 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, films starting with the letters K and Q
-- have also soared in popularity. Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.

-- select title as 'English Language Movies Starting with K or Q' from sakila.film where language_id = (select language_id from sakila.language where name = 'English') and title like "K%" or title like "Q%"



-- 7b. Use subqueries to display all actors who appear in the film Alone Trip.

-- select last_name, first_name from sakila.actor where actor_id in (select actor_id from sakila.film_actor where film_id = (select film_id from sakila.film where title = 'Alone Trip')) 



-- 7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to
-- retrieve this information.

-- select last_name, first_name, email from sakila.customer c join sakila.customer_list cl on (c.customer_id = cl.ID) where cl.country = 'Canada'



-- 7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as family films.

-- select * from sakila.film where film_id in (select film_id from sakila.film_category where category_id = (select category_id from sakila.category where name = 'Family'))



-- 7e. Display the most frequently rented movies in descending order.

-- select count(i.film_id) as 'Number of Rentals', f.* from sakila.rental r left join sakila.inventory i on (r.inventory_id = i.inventory_id) left join sakila.film f on (i.film_id = f.film_id) group by i.film_id order by count(i.film_id) desc



-- 7f. Write a query to display how much business, in dollars, each store brought in.

-- This works but an easier way prob is exist:
-- create view store_aus as select store as 'Store Location', (total_sales * .72) + (select (sum(amount) * .72) from sakila.payment where staff_id = (select ID from sakila.staff_list where name = 'Jon Stephens')) as 'Total Business ($USD)' from sakila.sales_by_store where manager = 'Jon Stephens'; create view store_can as select store as 'Store Location', (total_sales * .75) + (select (sum(amount) * .75) from sakila.payment where staff_id = (select ID from sakila.staff_list where name = 'Mike Hillyer')) as 'Total Business ($USD)' from sakila.sales_by_store where manager = 'Mike Hillyer'; select * from store_aus union select * from store_can

-- This works and did not end up being easier (way more dynamic and informative though!):
-- select s.store_id as 'Store ID', (select case when s.store_id = '1' then (select concat(address, ', ', city, ', ', country) from sakila.staff_list where SID = '1') when s.store_id = '2' then (select concat(address, ', ', city, ', ', country) from sakila.staff_list where SID = '2') else 'Error (Unknown Locale)' end as locale) as 'Store Location', s.staff_id as 'Manager ID', concat(s.first_name, ' ', s.last_name) as 'Manager Name', sum(amount) as 'Rentals Revenue ($)', (select total_sales from sakila.sales_by_store where manager = concat(s.first_name, ' ', s.last_name)) as 'Sales Revenue ($)', (sum(amount) + (select total_sales from sakila.sales_by_store where manager = concat(s.first_name, ' ', s.last_name))) as 'Total Business ($)', (select case when s.store_id = '1' then '$1 CAD = $0.75 USD' when s.store_id = '2' then '$1 AUD = $0.72 USD' else 'Error (Unknown Locale Currency >> USD Exchange Rate)' end as locale) as 'Exchange Rate', round(((sum(amount) + (select total_sales from sakila.sales_by_store where manager = concat(s.first_name, ' ', s.last_name))) * (select case when s.store_id = '1' then '.75' when s.store_id = '2' then '.72' else 'Error (Unknown Country)' end as locale)), 2) as 'Total Business ($USD)' from sakila.customer c join sakila.payment p on (c.customer_id = p.customer_id) join sakila.staff s on (p.staff_id = s.staff_id) group by s.staff_id



-- 7g. Write a query to display for each store its store ID, city, and country.

-- -- -- -- -- using code from above -- -- -- -- --
-- select store_id as 'Store ID', (select case when store_id = '1' then (select concat(address, ', ', city, ', ', country) from sakila.staff_list where SID = '1') when store_id = '2' then (select concat(address, ', ', city, ', ', country) from sakila.staff_list where SID = '2') else 'Error (Unknown Locale)' end as locale) as 'Store Location' from sakila.staff group by staff_id



-- 7h. List the top five genres in gross revenue in descending order. (Hint: you may need to use the following tables: category, film_category, inventory,
-- payment, and rental.)

-- This works
-- create view genres_aus as select c.name, r.staff_id, sum(p.amount) as 'Gross_Rev_Raw', round(sum(p.amount) * (select case when r.staff_id = '1' then '.75' end as locale), 2) as 'Gross_Rev_USD' from sakila.rental r join sakila.payment p on (r.rental_id = p.rental_id) join sakila.inventory i on (r.inventory_id = i.inventory_id) join sakila.film_category fc on (i.film_id = fc.film_id) join category c on (fc.category_id = c.category_id) group by c.name, r.staff_id having Gross_Rev_USD >= 1 order by round(sum(p.amount) * (select case when r.staff_id = '1' then '.75' else 'Error (Unknown Country)' end as locale), 2) desc;
-- create view genres_can as select c.name, r.staff_id, sum(p.amount) as 'Gross_Rev_Raw', round(sum(p.amount) * (select case when r.staff_id = '2' then '.72' end as locale), 2) as 'Gross_Rev_USD' from sakila.rental r join sakila.payment p on (r.rental_id = p.rental_id) join sakila.inventory i on (r.inventory_id = i.inventory_id) join sakila.film_category fc on (i.film_id = fc.film_id) join category c on (fc.category_id = c.category_id) group by c.name, r.staff_id having Gross_Rev_USD >= 1 order by round(sum(p.amount) * (select case when r.staff_id = '2' then '.72' else 'Error (Unknown Country)' end as locale), 2) desc;
-- select (select case when ga.name = gc.name then ga.name else '' end as locale) as 'Validated_Genre', (ga.Gross_Rev_USD + gc.Gross_Rev_USD) as 'Total_Gross_Rev_USD' from genres_aus ga join genres_can gc on (ga.name = gc.name) where (select case when ga.name = gc.name then ga.name else '' end as locale) is not null order by Total_Gross_Rev_USD desc limit 5



-- 8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. Use the solution from the problem 
-- above to create a view. If you haven't solved 7h, you can substitute another query to create a view.

-- -- -- -- -- using code from above -- -- -- -- --
-- create view Top_5_Earners as select (select case when ga.name = gc.name then ga.name else '' end as locale) as 'Validated_Genre', (ga.Gross_Rev_USD + gc.Gross_Rev_USD) as 'Total_Gross_Rev_USD' from genres_aus ga join genres_can gc on (ga.name = gc.name) where (select case when ga.name = gc.name then ga.name else '' end as locale) is not null order by Total_Gross_Rev_USD desc limit 5
-- select * from Top_5_Earners



-- 8b. How would you display the view that you created in 8a?

-- -- -- -- -- using code from above -- -- -- -- --
-- select * from Top_5_Earners



-- 8c. You find that you no longer need the view top_five_genres. Write a query to delete it.
-- drop view Top_5_Earners