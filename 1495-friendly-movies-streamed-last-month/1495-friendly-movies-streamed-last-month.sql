# Write your MySQL query statement below
SELECT DISTINCT C.title 
FROM Content C 
INNER JOIN TVProgram T
ON T.content_id = C.content_id 
WHERE DATE_FORMAT(T.program_date,'%Y-%m') = '2020-06'
AND C.Kids_content = 'Y'
AND C.content_type = 'movies'