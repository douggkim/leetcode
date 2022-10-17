# Write your MySQL query statement below
SELECT employee_id 
FROM 
((SELECT E.employee_id, S.salary, E.name
FROM Employees E 
LEFT OUTER JOIN Salaries S 
ON S.employee_id = E.employee_id)
UNION 
(SELECT S.employee_id, S.salary, E.name
FROM Salaries S 
LEFT OUTER JOIN Employees E 
ON S.employee_id = E.employee_id)) AS UT 
WHERE UT.salary IS NULL OR UT.name IS NULL
ORDER BY employee_id ASC 