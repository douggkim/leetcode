# Write your MySQL query statement below
WITH MaxDate AS 
(SELECT product_id, MAX(order_date) max_date 
FROM Orders O
GROUP BY product_id) 

SELECT P.product_name, O.product_id, O.order_id, O.order_date
FROM  Orders O, Products P, MaxDate M
WHERE O.product_id = P.product_id 
AND O.order_date = M.max_date 
AND O.product_id = M.product_id
ORDER BY product_name ASC, product_id ASC, order_id ASC 