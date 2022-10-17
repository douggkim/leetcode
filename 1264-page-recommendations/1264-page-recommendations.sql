# Write your MySQL query statement below
With NF as (
SELECT user1_id, user2_id
FROM Friendship
WHERE user1_id < user2_id 
UNION 
SELECT user2_id, user1_id 
FROM Friendship
WHERE user2_id < user1_id)

SELECT DISTINCT page_id AS recommended_page
FROM Likes L
WHERE L.user_id IN 
(SELECT user2_id 
FROM NF
WHERE NF.user1_id = 1)
AND L.page_id NOT IN 
(SELECT page_id 
FROM Likes
WHERE user_id=1)