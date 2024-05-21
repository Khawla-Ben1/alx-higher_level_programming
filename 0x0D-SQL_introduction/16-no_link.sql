--no_link
SELECT name, score FROM second_table WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
