# Write your MySQL query statement below
WITH TC AS 
(SELECT Wimbledon AS won
FROM Championships
UNION ALL
SELECT Fr_open AS won 
FROM Championships
UNION ALL 
SELECT US_open AS won
FROM Championships
UNION ALL 
SELECT Au_open AS won 
FROM Championships)

SELECT  P.player_id, P.player_name, COUNT(*) AS grand_slams_count 
FROM Players P, TC
WHERE TC.won = P.player_id 
GROUP BY P.player_id, P.player_name