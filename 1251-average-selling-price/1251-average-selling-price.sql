# Write your MySQL query statement below
SELECT US.product_id, ROUND(SUM(price*units)/SUM(units),2) AS average_price
FROM Prices P, UnitsSold US 
WHERE US.purchase_date BETWEEN P.start_date AND P.end_date
AND US.product_id = P.product_id 
GROUP BY US.product_id 