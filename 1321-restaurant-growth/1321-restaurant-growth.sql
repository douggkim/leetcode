# Write your MySQL query statement below
WITH OT AS 
(SELECT C.visited_on, SUM(amount) AS amount, ROW_NUMBER() OVER (ORDER BY visited_on) rownum
FROM Customer C
GROUP BY 1
ORDER BY rownum), OT2 AS 
(SELECT C.visited_on AS visited_on, SUM(amount) OVER ( ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount, ROUND(AVG(amount) OVER ( ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW ),2) AS average_amount, rownum
FROM OT C 
WHERE amount IS NOT NULL
ORDER BY visited_on)

SELECT C.visited_on, C.amount, C.average_amount 
FROM OT2 C 
WHERE C.rownum >=7




