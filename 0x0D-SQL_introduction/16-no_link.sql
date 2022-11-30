-- script which prints all records with a value
-- SELECT statements with IS NOT NULL will be implemented
SELECT score, name FROM second_table
	WHERE name IS NOT NULL
	ORDER BY score DESC;
