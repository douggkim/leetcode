# Write your MySQL query statement below
SELECT S.seller_name
FROM Seller S
LEFT OUTER JOIN (SELECT * FROM Orders  WHERE YEAR(sale_date) = 2020) AS O
ON O.seller_id = S.seller_id 
WHERE order_id IS NULL
ORDER BY seller_name ASC