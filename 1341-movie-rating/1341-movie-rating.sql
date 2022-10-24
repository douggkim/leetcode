# Write your MySQL query statement below
(SELECT U.name results
FROM MovieRating MR 
INNER JOIN Users U 
ON U.user_id = MR.user_id 
GROUP BY MR.user_id
ORDER BY COUNT(*) DESC, U.name
LIMIT 1)
UNION 
(SELECT M.title results
FROM MovieRating MR 
INNER JOIN Movies M 
ON M.movie_id = MR.movie_id
WHERE DATE_FORMAT(created_at, '%Y-%m') = '2020-02'
GROUP BY MR.movie_id
ORDER BY AVG(rating) DESC, M.title
LIMIT 1)