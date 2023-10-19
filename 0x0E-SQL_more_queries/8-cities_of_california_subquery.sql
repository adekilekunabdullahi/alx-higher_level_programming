-- a script that lists all the cities of California
-- code
SELECT id, name FROM cities WHERE id = (SELECT id from states WHERE name = 'California') ORDER BY id ASC;
