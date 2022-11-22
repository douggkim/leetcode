# Write your MySQL query statement below
WITH CT AS 
(SELECT DISTINCT C.id, C.name AS Customers
FROM Customers C 
LEFT OUTER JOIN Orders O 
ON C.id = O.customerId
WHERE O.customerId IS NULL) 

SELECT Customers 
FROM CT