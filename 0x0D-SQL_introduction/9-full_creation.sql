-- create a second table on th hbtn_0c_0 database

USE hbtn_0c_0;

CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
	);

INSERT INTO second_table (id, name, score)
VALUE (1,'john', 10), (2, 'Alex', 3), (3, 'Bob', 14), (4, George, 8);
