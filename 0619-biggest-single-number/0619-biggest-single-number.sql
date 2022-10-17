# Write your MySQL query statement below
SELECT IFNULL(MAX(num), NULL) AS num 
FROM (SELECT MN.num FROM MyNumbers MN 
GROUP BY MN.num 
HAVING COUNT(*)=1) MN 
ORDER BY MN.num DESC
