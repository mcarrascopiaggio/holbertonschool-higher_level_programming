-- Cities of California
-- Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT id, name states AS name 
FROM cities
INNER JOIN states
ON cities.states_id = state_id
ORDER BY id;
