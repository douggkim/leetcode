# Write your MySQL query statement below
WITH cnt_table AS (
SELECT email,COUNT(*) mail_cnt 
FROM Person P 
GROUP BY email)

SELECT email AS Email 
FROM cnt_table
WHERE mail_cnt>=2 