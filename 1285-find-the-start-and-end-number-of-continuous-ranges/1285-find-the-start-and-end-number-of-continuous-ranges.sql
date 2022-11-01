# Write your MySQL query statement below
WITH RT AS 
(SELECT log_id, ROW_NUMBER() OVER (ORDER BY log_id ASC) AS id
FROM Logs 
ORDER BY log_id
), RT2 AS 
(SELECT log_id, log_id-id AS id 
FROM RT)


SELECT MIN(log_id) AS start_id, MAX(log_id) end_id
FROM RT2
GROUP BY id