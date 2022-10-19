# Write your MySQL query statement below
SELECT DISTINCT L1.num AS ConsecutiveNums
FROM Logs L1
INNER JOIN Logs L2
ON (L1.id+1 = L2.id AND L1.num=L2.num)
INNER JOIN Logs L3 
ON (L2.id+1 = L3.id AND L2.num = L3.num)
WHERE L2.num IS NOT NULL AND L3.num IS NOT NULL; 