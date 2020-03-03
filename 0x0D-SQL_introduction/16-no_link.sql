
-- Lists all records of a table with names in descending order.
-- SELECT is used to retrieve rows selected from one or more tables.
SELECT score, name FROM second_table WHERE CHAR_LENGTH(name) > 0 ORDER BY score DESC;
