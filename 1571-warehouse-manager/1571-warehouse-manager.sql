# Write your MySQL query statement below
SELECT WH.name AS warehouse_name, SUM(WH.units*P.Width*P.Length*P.Height) AS volume 
FROM Warehouse AS WH, Products AS P
WHERE WH.product_id = P.product_id
GROUP BY WH.name 


