# Write your MySQL query statement below
WITH RT AS 
(
SELECT id, name, salary, departmentId, DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS sal_rnk 
FROM Employee 
)


SELECT D.name AS Department, RT.name AS Employee, RT.salary AS Salary
FROM RT 
INNER JOIN Department D 
on D.id = RT.departmentId
WHERE sal_rnk <=3