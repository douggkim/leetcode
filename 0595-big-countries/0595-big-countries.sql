# Write your MySQL query statement below
# Big 1) area .= 3000000
# Big 2) population >= 25000000
# any order
# name, population, area 

SELECT name, population, area
FROM World 
WHERE area >= 3000000
OR population >= 25000000
