# Write your MySQL query statement below
WITH RT AS 
(SELECT id, name, salary, departmentId, RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS sal_rnk 
FROM Employee)


SELECT D.name AS Department, RT.name AS Employee, RT.salary 
FROM RT 
INNER JOIN Department AS D 
ON RT.departmentId = D.id
WHERE sal_rnk = 1 