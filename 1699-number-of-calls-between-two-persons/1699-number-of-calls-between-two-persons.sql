# Write your MySQL query statement below
WITH TC AS 
(SELECT * 
FROM Calls C1
UNION ALL 
SELECT C2.to_id AS from_id, C2.from_id AS to_id, duration
FROM Calls C2)

SELECT from_id AS person1, to_id AS person2, COUNT(duration) AS call_count, SUM(duration) AS total_duration
FROM TC 
WHERE from_id < to_id
GROUP BY from_id, to_id 
