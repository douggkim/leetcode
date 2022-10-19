# Write your MySQL query statement below
SELECT id,CASE WHEN id=(SELECT COUNT(*) FROM Seat S3) AND id%2!=0 THEN S1.student 
WHEN id%2=0 THEN (SELECT student FROM Seat S3 WHERE S3.id=S1.id-1) WHEN id%2!=0 THEN (SELECT student FROM Seat S3 WHERE S3.id=S1.id+1) END AS student
FROM Seat S1
