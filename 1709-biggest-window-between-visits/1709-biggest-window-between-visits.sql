# Write your MySQL query statement below
WITH W AS 
(SELECT UV.user_id, UV.visit_date, TIMESTAMPDIFF(DAY, (LAG(visit_date,1) OVER (PARTITION BY user_id ORDER BY visit_date ASC)), visit_date)AS w, TIMESTAMPDIFF(DAY, visit_date, '2021-1-1') as default_w
FROM UserVisits UV) 


SELECT W.user_id, IF(MAX(W.w)> MIN(W.default_w), MAX(W.w), MIN(W.default_w)) AS biggest_window
FROM W 
GROUP BY W.user_id
