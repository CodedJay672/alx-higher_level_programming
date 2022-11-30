-- Script that selects scores >= 10 in the second table
-- SELECT...WHERE...ORDER BY statement is implemented
SELECT score, name FROM second_table
	WHERE score >= 10
	ORDER BY score DESC;
