# Write your MySQL query statement below
WITH CNT AS (SELECT R1.user_id AS user1_id, R2.user_id AS user2_id, COUNT(*) AS maxCommon
FROM relations R1 
JOIN relations R2
ON R1.user_id < R2.user_id
AND R1.follower_id = R2.follower_id
GROUP BY R1.user_id, R2.user_id),
MAXT AS (
SELECT  MAX(maxCommon) as max_cnt
FROM CNT 
)

SELECT user1_id, user2_id 
FROM CNT 
JOIN MAXT 
ON CNT.maxCommon = MAXT.max_cnt 