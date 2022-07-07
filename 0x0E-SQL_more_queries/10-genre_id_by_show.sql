-- Genre ID by show
-- Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
INNER JOIN tv_shows
ON tv_shows.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id
