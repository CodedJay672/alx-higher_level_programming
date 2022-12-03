-- script which creates a table with hardcoded value in the ID column
-- CREATE TABLE is implemented
CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1,
	name VARCHAR(256)
	);
