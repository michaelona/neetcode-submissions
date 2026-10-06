-- Write your query below
-- Get names from sales_person name from orders table where sales id is not in
-- (Selection of sale_ids from CRIMSON orders)

SELECT s.name
FROM sales_person s
WHERE sales_id NOT IN (
    SELECT sales_id
    FROM orders o 
    LEFT JOIN company c ON c.com_id = o.com_id
    WHERE c.name = 'CRIMSON'
);