# Write your MySQL query statement below
# Create a table without cancelled 

WITH without_cancel AS 
(SELECT T.id, T.client_id, T.driver_id, T.status, T.request_at
FROM Trips T
INNER JOIN Users U1 
ON T.client_id = U1.users_id
INNER JOIN Users U2 
ON T.driver_id = U2.users_id 
WHERE U1.banned = 'No'
AND U2.banned = 'No')


SELECT DATE_FORMAT(WC.request_at, '%Y-%m-%d') AS "Day", ROUND(SUM(CASE WHEN WC.status != 'completed' THEN 1 ELSE 0 END)/COUNT(*), 2) AS "Cancellation Rate"
FROM without_cancel WC 
WHERE WC.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY DATE_FORMAT(WC.request_at, '%Y-%m-%d') 