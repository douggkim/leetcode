# Write your MySQL query statement below


SELECT id, CASE 
WHEN (id % 2 = 1 AND id = (SELECT MAX(id) FROM Seat)) THEN student
WHEN (S1.id % 2 = 1) THEN (SELECT student FROM Seat S2 WHERE S2.id = S1.id +1)
WHEN (S1.id % 2 = 0) THEN (SELECT student FROM Seat S2 WHERE S2.id = S1.id - 1)
END  AS student
FROM Seat S1