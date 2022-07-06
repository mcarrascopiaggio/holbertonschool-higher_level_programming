-- Cities of California
-- Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT id, name FROM cities WHERE stated_id = (SELECT id FROM states WHERE name = 'California') GROUP BY id ORDER BY id;
