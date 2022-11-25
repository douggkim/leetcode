# Write your MySQL query statement below
# 1) Create UNION Table + win lose
# 2) JOIN with Teams 
# 
# ORDER BY points DESC, goal_diff DESC, team_name ASC 


WITH UT AS 
(SELECT home_team_id, home_team_goals, away_team_goals, (CASE WHEN home_team_goals>away_team_goals THEN 3 WHEN home_team_goals = away_team_goals THEN 1 ELSE 0 END) AS win_lose 
FROM Matches 
UNION ALL
SELECT away_team_id, away_team_goals, home_team_goals, (CASE WHEN away_team_goals>home_team_goals THEN 3 WHEN home_team_goals = away_team_goals THEN 1 ELSE 0 END) AS win_lose
FROM Matches 
), CT AS 
(
SELECT home_team_id, COUNT(*) AS matches_played, SUM(win_lose) AS points, SUM(home_team_goals)AS goal_for, SUM(away_team_goals) AS goal_against, SUM(home_team_goals - away_team_goals) AS goal_diff 
FROM UT
GROUP BY home_team_id )


SELECT T.team_name, CT.matches_played, CT.points, CT.goal_for, CT.goal_against, CT.goal_diff
FROM CT 
INNER JOIN Teams T
ON CT.home_team_id = T.team_id 
ORDER BY points DESC, goal_diff DESC, team_name ASC 