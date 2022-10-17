# Write your MySQL query statement below
WITH TS AS 
(SELECT team_id, COUNT(employee_id) AS team_size
FROM Employee E 
GROUP BY team_id)

SELECT E.employee_id, TS.team_size
FROM TS, Employee E 
WHERE E.team_id = TS.team_id 