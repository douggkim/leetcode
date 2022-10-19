# Write your MySQL query statement below
SELECT P1.id AS p1, P2.id AS p2, ABS(P1.x_value-P2.x_value)*ABS(P2.y_value-P1.y_value) AS area 
FROM Points P1
INNER JOIN Points P2
ON P1.x_value != P2.x_value 
AND P1.y_value != P2.y_value 
WHERE P1.id < P2.id
ORDER BY area DESC, p1 ASC, p2 ASC
