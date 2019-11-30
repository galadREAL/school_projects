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



-- ! am I supposed to group by ID to make it dynamic?
-- 7f. Write a query to display how much business, in dollars, each store brought in.

-- remember to add sales to rental amounts, and convert dollars (as of 4/19 >> 1 CAD = .75 USD and 1 AUD = .72 USD)

-- working version of rental amt by staffID::: select p.staff_id, sum(amount) from sakila.customer c join sakila.payment p on (c.customer_id = p.customer_id) group by p.staff_id

-- working version of Jon Stephen's store's total rev::: 
-- select store as 'Store Location', (total_sales * .72) + (select (sum(amount) * .72) from sakila.payment where staff_id = (select ID from sakila.staff_list where name = 'Jon Stephens')) as 'Total Business ($USD)' from sakila.sales_by_store where manager = 'Jon Stephens' 

-- working version of Mike Hillyer's sotre's total rev::: 
-- select store as 'Store Location', (total_sales * .75) + (select (sum(amount) * .75) from sakila.payment where staff_id = (select ID from sakila.staff_list where name = 'Mike Hillyer')) as 'Total Business ($USD)' from sakila.sales_by_store where manager = 'Mike Hillyer'



