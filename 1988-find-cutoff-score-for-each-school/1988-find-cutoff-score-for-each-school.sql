SELECT S.school_id, IFNULL(MIN(E.score),-1) AS score
FROM Schools S
LEFT OUTER JOIN Exam E 
ON S.capacity >= E.student_count
GROUP BY S.school_id