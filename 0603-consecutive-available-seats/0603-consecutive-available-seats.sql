SELECT seat_id
FROM 
((SELECT C1.seat_id
FROM Cinema C1
INNER JOIN Cinema C2 
ON C1.seat_id = C2.seat_id + 1 
WHERE C1.free=1 AND C2.free=1 )
UNION 
(SELECT C2.seat_id
FROM Cinema C1
INNER JOIN Cinema C2 
ON C1.seat_id = C2.seat_id + 1 
WHERE C1.free=1 AND C2.free=1)) AS Integrated
ORDER BY seat_id ASC;