SELECT c.customer_id, c.first_name, r.rental
FROM sakila.customer c
JOIN
		( SELECT DISTINCT
        customer_id,
        COUNT(customer_id) OVER (PARTITION BY customer_id) AS 'rental'
		FROM sakila.rental)

r ON c.customer_id = r.customer_id
