# Write your MySQL query statement below
# SENIOR -> COUNT salary accum_sum  < = 70000 
# JUNIOR -> MAX Salary <= 70000 

WITH AT AS 
(SELECT C.*, SUM(salary) OVER (PARTITION BY experience ORDER BY salary ASC) AS accum_sal 
FROM Candidates C)


SELECT "Senior" AS experience, COUNT(*) AS accepted_candidates 
FROM AT 
WHERE AT.accum_sal <= 70000 
AND AT.experience = 'Senior' 
UNION 
SELECT "Junior" AS experience, COUNT(*) AS accepted_candidates 
FROM AT 
WHERE AT.accum_sal <=  70000 - (SELECT IFNULL(MAX(accum_sal),0) FROM AT WHERE AT.experience = 'Senior' AND AT.accum_sal<=70000) 
AND AT.experience = 'Junior' 
