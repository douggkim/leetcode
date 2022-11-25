# Write your MySQL query statement below
# Country name where AVG(duration) < AVG(duration) AS global 
# Person -> SUBSTR(phone_number,1,3) = C.country_code
WITH Person_with_country AS (
SELECT P.id, P.name, C.name AS country 
FROM Person P 
INNER JOIN Country C 
ON SUBSTR(P.phone_number,1,3) = C.country_code
), global_average AS (
SELECT AVG(duration) global_avg
FROM Calls), UT AS (
SELECT caller_id, duration
FROM Calls 
UNION 
SELECT callee_id, duration 
FROM Calls )

SELECT PC.country
FROM UT
INNER JOIN Person_with_country AS PC
ON UT.caller_id = PC.id 
GROUP BY PC.country 
HAVING AVG(duration) > (SELECT global_avg FROM global_average )