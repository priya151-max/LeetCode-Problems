# Write your MySQL query statement below
SELECT 
    start_table.machine_id,
    ROUND(AVG(end_table.timestamp - start_table.timestamp), 3) AS processing_time
FROM 
    Activity start_table
JOIN 
    Activity end_table 
    ON start_table.machine_id = end_table.machine_id 
    AND start_table.process_id = end_table.process_id
WHERE 
    start_table.activity_type = 'start' 
    AND end_table.activity_type = 'end'
GROUP BY 
    start_table.machine_id;
