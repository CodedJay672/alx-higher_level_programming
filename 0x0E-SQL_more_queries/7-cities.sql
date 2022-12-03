-- script that creates a database
-- if the database already exists, the script should not fail
-- a table should be created (inside the database)
-- if the table already exists, the script shoulf not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL, FOREIGN KEY (state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL
	);
