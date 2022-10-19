# Write your MySQL query statement below
SELECT COALESCE(EU.unique_id, NULL) AS unique_id, E.name
FROM Employees E
LEFT OUTER JOIN EmployeeUNI EU
ON E.id = EU.id 