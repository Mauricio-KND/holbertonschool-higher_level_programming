-- Lists the number of records with the same score a the table.
-- SELECT is used to retrieve rows selected from one or more tables.
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
