# Write your MySQL query statement below
WITH MT AS 
(
SELECT E1.*, E2.name AS report_name
FROM Employee E1, Employee E2 
WHERE E1.id = E2.managerId)

SELECT name
FROM MT 
GROUP BY id,name 
HAVING COUNT(DISTINCT report_name)>=5