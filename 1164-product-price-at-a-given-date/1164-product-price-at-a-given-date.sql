# Write your MySQL query statement below
WITH  TotalT AS(
SELECT DISTINCT product_id, 10 AS new_price, DATE('2000-01-01') AS change_date 
FROM Products
UNION
SELECT *
FROM Products
), MaxT AS (
SELECT product_id, MAX(P.change_date) AS change_date
FROM TotalT P 
WHERE P.change_date <= '2019-08-16'
GROUP BY product_id 
)

SELECT  P.product_id, IFNULL(new_price,10) AS price
FROM TotalT P 
INNER JOIN MaxT
ON P.product_id = MaxT.product_id 
AND P.change_date = MaxT.change_date
WHERE MaxT.change_date
