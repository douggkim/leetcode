# Write your MySQL query statement below
WITH MT AS 
(SELECT student_id, MAX(grade) grade
FROM Enrollments
GROUP BY student_id)

SELECT E.student_id, MIN(E.course_id) AS course_id, MAX(E.grade) as grade 
FROM Enrollments E, MT 
WHERE E.grade = MT.grade 
AND E.student_id = MT.student_id 
GROUP BY E.student_id 
ORDER BY E.student_id ASC 