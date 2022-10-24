# Write your MySQL query statement below
WITH MT AS 
(SELECT SUM(quantity)/COUNT(DISTINCT product_id) avg_amt
FROM OrdersDetails OD
GROUP BY OD.order_id 
ORDER BY avg_amt DESC
LIMIT 1)

SELECT OD.order_id
FROM OrdersDetails OD
GROUP BY OD.order_id 
HAVING MAX(quantity)> (SELECT avg_amt FROM MT)