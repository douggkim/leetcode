# Write your MySQL query statement below
WITH MT AS 
(SELECT O.product_id, MAX(order_date) max_order_date
FROM Orders O 
GROUP BY O.product_id)

SELECT P.product_name, O.product_id, O.order_id, O.order_date
FROM Orders O 
INNER JOIN MT
ON MT.product_id = O.product_id 
AND O.order_date = MT.max_order_date  
INNER JOIN Products P 
ON P.product_id = O.product_id 
ORDER BY P.product_name, O.product_id, O.order_id