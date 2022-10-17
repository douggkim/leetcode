# Write your MySQL query statement below
SELECT C.country_name, CASE WHEN SUM(W.weather_state)/COUNT(*)<= 15 THEN 'Cold'
WHEN SUM(W.weather_state)/COUNT(*)>=25 THEN 'Hot'
ELSE 'Warm' END AS weather_type
FROM Countries C, Weather W
WHERE DATE_FORMAT(W.day, '%Y-%m') = '2019-11'
AND C.country_id = W.country_id
GROUP BY C.country_name