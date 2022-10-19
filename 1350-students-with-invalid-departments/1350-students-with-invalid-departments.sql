# Write your MySQL query statement below
SELECT S.id, S.name
FROM Students S 
LEFT OUTER JOIN Departments D 
ON S.department_id = D.id
WHERE D.name IS NULL 