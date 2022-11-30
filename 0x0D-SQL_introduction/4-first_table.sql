-- script that creates a table if it doesnt exist in the SQL server
-- CREATE command with the "IF NOT EXISTS" option can perform this
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
	)
