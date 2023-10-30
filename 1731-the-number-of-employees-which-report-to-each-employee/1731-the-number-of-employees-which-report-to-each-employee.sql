# Write your MySQL query statement below
WITH MT AS (
SELECT reports_to, COUNT(employee_id) AS reports, ROUND(AVG(age),0) as avg_age 
FROM employees E 
WHERE E.reports_to IS NOT NULL 
GROUP BY reports_to)

SELECT E.employee_id, E.name, MT.reports AS reports_count, MT.avg_age as average_age
FROM employees E 
JOIN MT 
ON MT.reports_to = E.employee_id 
ORDER BY E.employee_id