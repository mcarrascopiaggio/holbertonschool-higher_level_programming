-- task 15
-- Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in
SELECT score, COUNT( score ) AS number FROM second_table GROUP BY score ORDER BY score DESC;
