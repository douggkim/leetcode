# Write your MySQL query statement below
WITH pivot AS (
SELECT customer_id, SUM(CASE product_name WHEN 'A' THEN 1 ELSE 0 END) AS A_yn,
SUM(CASE product_name WHEN 'B' THEN 1 ELSE 0 END) AS B_yn,
SUM(CASE product_name WHEN 'C' THEN 1 ELSE 0 END) AS C_yn
FROM Orders O 
GROUP BY customer_id
)

SELECT C.customer_id, C.customer_name
FROM Customers C, pivot P 
WHERE P.A_yn >= 1 AND P.B_yn >= 1. AND P.C_yn = 0 
AND C.customer_id = P.customer_id 
ORDER BY C.customer_id