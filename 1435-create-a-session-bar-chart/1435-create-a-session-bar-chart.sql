# Write your MySQL query statement below
WITH bin_t AS 
(SELECT CASE WHEN duration/60 <=5 THEN '[0-5>' 
WHEN duration/60 <=10 THEN '[5-10>'
WHEN duration/60 <=15 THEN '[10-15>'
ELSE '15 or more' END AS bin, session_id
FROM Sessions S 
GROUP BY session_id),
bin_all AS 
(SELECT "[0-5>" AS bin 
 UNION 
 SELECT "[5-10>" AS bin
 UNION 
 SELECT "[10-15>" AS bin 
 UNION 
 SELECT "15 or more" AS bin)

SELECT BT1.bin, COUNT(BT2.session_id) AS total
FROM bin_all AS BT1 
LEFT OUTER JOIN bin_t AS BT2
ON BT1.bin = BT2.bin 
GROUP BY BT1.bin  
