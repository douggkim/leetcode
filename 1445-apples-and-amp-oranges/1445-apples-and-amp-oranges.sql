# Write your MySQL query statement below
SELECT sale_date, SUM(CASE fruit WHEN 'apples' THEN sold_num WHEN 'oranges' THEN sold_num*-1 END) diff 
FROM Sales S 
GROUP by sale_date
ORDER BY sale_date