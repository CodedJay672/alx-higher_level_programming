-- script that lists the average temperatures in the temperatures table
-- SELECT statement is implemented
SELECT city, AVG(value) AS avg_temp FROM temperatures
	GROUP BY city
	ORDER BY AVG(value) DESC;
