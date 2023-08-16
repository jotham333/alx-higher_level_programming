-- List all records of the table second_table in htbn_0c_0 database

SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
