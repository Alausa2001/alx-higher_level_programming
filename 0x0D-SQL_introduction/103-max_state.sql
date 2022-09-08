-- lists the max temperature of each state ordered by the states' name
SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state;
