# Write your MySQL query statement below
# rank based on the scores (dense ranks) - DESC score 
# Score DESC 
# score / rank 
# ROUND(,2) -> maintain

SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) AS "rank"
FROM Scores 

