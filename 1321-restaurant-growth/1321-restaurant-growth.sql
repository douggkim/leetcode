WITH NT AS 
(
SELECT C.visited_on, SUM(C.amount) AS amt, AVG(C.amount) AS avg_amt, ROW_NUMBER() OVER (ORDER BY C.visited_on) AS rownum 
FROM Customer C
GROUP BY 1),
NT2 AS 
(
SELECT visited_on, SUM(amt) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount, ROUND(AVG(amt) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW),2) AS average_amount, rownum
FROM NT 
)

SELECT visited_on, amount, average_amount
FROM NT2 
WHERE rownum >= 7



