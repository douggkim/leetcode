# Write your MySQL query statement below
SELECT DISTINCT L1.account_id
FROM LogInfo L1 
INNER JOIN LogInfo L2 
ON L1.account_id = L2.account_id 
AND L1.ip_address != L2.ip_address 
AND L1.login >= L2.login AND L1.login <= L2.logout
