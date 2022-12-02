-- script which displays the top THREE cities by average temperature
-- SELECT the cities and grouping them can solve this problem
SELECT city, avg(value) AS avg_temp FROM temperatures
	WHERE month = 7 OR month = 8
	GROUP BY city
	ORDER BY AVG(value) DESC LIMIT 3;
