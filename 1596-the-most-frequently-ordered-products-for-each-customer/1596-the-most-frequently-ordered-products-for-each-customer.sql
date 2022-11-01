# Write your MySQL query statement below
WITH A AS 
(SELECT O.customer_id, O.product_id, COUNT(*) cnt
FROM Orders O 
GROUP BY O.customer_id, O.product_id), 
AT2 AS 
(SELECT A.customer_id, MAX(cnt) max_cnt
FROM A
GROUP BY A.customer_id)

SELECT A.customer_id, A.product_id, P.product_name
FROM A
INNER JOIN AT2 
ON A.customer_id = AT2.customer_id
AND AT2.max_cnt = A.cnt
INNER JOIN Products P 
ON P.product_id = A.product_id
