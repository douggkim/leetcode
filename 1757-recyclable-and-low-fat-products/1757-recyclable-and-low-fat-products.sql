# Write your MySQL query statement below
SELECT product_id
FROM Products 
WHERE low_fats IS NOT NULL
AND low_fats = 'Y'
AND recyclable IS NOT NULL
AND recyclable = 'Y'