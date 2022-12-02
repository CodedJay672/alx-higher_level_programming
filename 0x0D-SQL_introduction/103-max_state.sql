-- script which displays the maximum temperatures of each state
-- SELECT statement is implemented
SELECT state, MAX(value) AS max_temp FROM temperatures
	GROUP BY state
	ORDER BY state;
