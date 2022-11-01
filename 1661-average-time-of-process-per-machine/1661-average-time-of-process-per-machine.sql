# Write your MySQL query statement below
WITH IT AS 
(SELECT A1.machine_id, A1.process_id, A1.activity_type a1_activity_type, A1.timestamp AS start_time, A2.activity_type a2_activity_type, A2.timestamp AS end_time
FROM Activity AS A1 
INNER JOIN Activity AS A2 
WHERE A1.machine_id = A2.machine_id 
AND A1.process_id = A2.process_id
AND A1.activity_type != A2.activity_type
AND A2.timestamp-A1.timestamp>0
)

# SELECT machine_id, end_time-start_time AS processing_time
# FROM IT

SELECT machine_id, ROUND(AVG(end_time-start_time),3) AS processing_time
FROM IT
GROUP BY machine_id 
ORDER BY machine_id