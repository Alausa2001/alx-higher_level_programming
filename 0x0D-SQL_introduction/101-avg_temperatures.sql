-- displays the average temperature by city ordered by average temperature in descending order

SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
