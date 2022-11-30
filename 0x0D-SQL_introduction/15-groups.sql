-- script which counts rows with same scores
-- SELECT statement with the count() function is used
SELECT score, count(score) AS number FROM second_table GROUP BY score;
