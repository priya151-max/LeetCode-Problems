# Write your MySQL query statement below
SELECT 
    ROUND(
        COUNT(DISTINCT q.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 
        2
    ) AS fraction
FROM Activity q
JOIN (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
) p 
ON q.player_id = p.player_id 
AND q.event_date = DATE_ADD(p.first_login, INTERVAL 1 DAY);
