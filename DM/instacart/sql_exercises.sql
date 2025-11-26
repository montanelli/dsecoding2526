-- the exercises are based on the instacart case study. The database can be downloaded from:
-- http://contents.islab.di.unimi.it/datasets/instacart_small.sql.zip

-- departments(department_id, department)  
-- aisles(aisle_id, aisle)  
-- products(product_id, product_name, aisle_id, department_id)
-- orders(order_id, user_id, order_number, order_dow, order_hour_of_day, days_since_prior_order)
-- order_products(order_id, product_id, add_to_cart_order, reordered)

-- is it possible to buy a product twice in an order?
-- No it is a violation of the PK of table order_products 

-- is it possible that a customer buys the same product twice?
-- Yes, in two different orders

-- tick the statement that cannot generate an error
A. DELETE FROM aisles WHERE aisle_id = 5; -- Y 
B. DELETE FROM departments WHERE department_id = 8; -- Y
C. UPDATE aisles SET aisle_id = 4 WHERE aisle_id = 5; -- Y (for two possible motivations: due to FK and due to PK)
D. UPDATE departments SET department_id = 7 WHERE department_id = 8; -- Y (due to the possible duplication of the PK) 
E. UPDATE departments SET department = 'data science' WHERE department_id = 8; -- N

-- tick the statement that can generate an error
A. DELETE FROM order_products WHERE order_id = 5; -- no errors
B. DELETE FROM products WHERE product_id = 8292; -- no errors
C. DELETE FROM orders WHERE order_id = 4848; -- possible errors
D. DELETE FROM order_products WHERE product_id = 0494; -- no errors


-- Retrieve the order_id, product_id, and the product_name for each order submitted on Monday (order_dow = 1)
SELECT o.order_id, p.product_id, product_name 
FROM orders o INNER JOIN order_products op ON o.order_id = op.order_id INNER JOIN products p ON p.product_id = op.product_id
WHERE order_dow = 1;


-- Retrieve the order_id, product_id, and the name of products that are added as first in the cart of each order (add_to_cart_order = 1)
SELECT order_id, products.product_id, product_name
FROM order_products INNER JOIN products ON order_products.product_id = products.product_id
WHERE add_to_cart_order = 1;

-- Retrieve the order_id, product_id, and the product_name for each order submitted between the hours 15 and 17 
SELECT order_products.order_id, products.product_id, product_name
FROM order_products INNER JOIN products ON order_products.product_id = products.product_id INNER JOIN orders ON order_products.order_id = orders.order_id
WHERE order_hour_of_day >= 15 AND order_hour_of_day <= 17;

-- Retrieve the id of orders where the first product added to the cart is the same as the one in the order_id = 2411567
-- solution with subquery
SELECT order_id 
FROM order_products
WHERE add_to_cart_order = 1 and product_id = (SELECT product_id 
FROM order_products op
WHERE order_id = 2411567 and add_to_cart_order = 1)

-- alternative solution with self-join (more elegant)
SELECT op2.order_id
from order_products op1, order_products op2
WHERE op1.order_id = 2411567 and op1.add_to_cart_order = 1 and 
    op2.add_to_cart_order = 1 and op1.product_id = op2.product_id;


-- Retrieve the name of products that are ordered on Monday (order_dow = 1) from the coffee aisle. Sort the result by the product name
SELECT DISTINCT product_name
FROM products INNER JOIN order_products ON order_products.product_id = products.product_id INNER JOIN aisles ON products.aisle_id = aisles.aisle_id INNER JOIN orders ON order_products.order_id = orders.order_id
WHERE aisles.aisle = 'coffee' AND order_dow = 1
ORDER BY product_name;

-- Retrieve the id of products that are never ordered on Tuesday (order_dow = 2)
-- solution with subquery: first I get the products sold on Tue, then I remove these products from the overall set of products
select product_id
from products 
where product_id not in (
SELECT distinct product_id 
FROM order_products op INNER JOIN orders o ON o.order_id = op.order_id 
WHERE order_dow = 2 )

-- very wrong solution:
select product_id
from order_products op INNER JOIN orders o ON o.order_id = op.order_id 
where order_dow <> 2

-- alternative solution: use of except
SELECT product_id
FROM products
EXCEPT
SELECT product_id
FROM order_products INNER JOIN orders ON order_products.order_id = orders.order_id
WHERE order_dow = 2;


-- Retrieve the id of products from the coffee aisle that are never ordered on Tuesay (order_dow = 2)
SELECT product_id
FROM products INNER JOIN aisles ON products.aisle_id = aisles.aisle_id
WHERE aisle = 'coffee'
EXCEPT
SELECT product_id
FROM order_products INNER JOIN orders ON order_products.order_id = orders.order_id
WHERE order_dow = 2;

-- Retrieve the id of users that submitted orders on BOTH Monday (order_dow = 1) and Tuesday (order_dow = 2). 
SELECT user_id
FROM orders
WHERE order_dow = 1
INTERSECT
SELECT user_id
FROM orders
WHERE order_dow = 2;

-- Retrieve the average number of products for each order
-- HINT: create a view with product counts for each order as intermediate step  
CREATE VIEW order_products_counts AS (SELECT order_id, count(product_id) AS "product_count" FROM order_products GROUP BY order_id);
SELECT avg(product_count)
FROM order_products_counts;

-- solution with WITH
WITH order_products_counts as 
(SELECT order_id, count(product_id) AS "product_count" FROM order_products GROUP BY order_id)
SELECT avg(product_count)
FROM order_products_counts;

-- For each department, retrieve the number of ordered products. Show the department_name in the result. Sort the result by the number of products in descending order
select d.department_id, department, count(op.product_id) as pnumber 
from departments d left join products p on d.department_id = p.department_id left join order_products op on p.product_id = op.product_id 
group by d.department_id, department
order by pnumber desc 


-- Refine the previous query by returning only the departments with more than 1M of ordered products
select d.department_id, department, count(op.product_id) as pnumber 
from departments d left join products p on d.department_id = p.department_id left join order_products op on p.product_id = op.product_id 
group by d.department_id, department
having count(op.product_id) > 1000000
order by pnumber desc 

-- For each product in the coffee aisle, retrieve the number of orders submitted on Tuesday (order_dow = 2). Include in the result the products that are never ordered (if they exist)
SELECT products.product_id, product_name, count(orders.order_id) 
FROM aisles INNER JOIN products ON products.aisle_id = aisles.aisle_id LEFT JOIN order_products ON order_products.product_id = products.product_id
LEFT JOIN orders ON (order_products.order_id = orders.order_id AND order_dow = 2) 
WHERE aisles.aisle = 'coffee'
GROUP BY products.product_id, product_name
ORDER BY 3;


