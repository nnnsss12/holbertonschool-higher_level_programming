-- lists all records of second_table where name has a value, ordered by score (descending)
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
