-- Lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- SELECT statement retrieves rows selected from one or more tables.
SELECT tv_shows.title, tv_show_genres.genre_id
-- FROM clause lists the tables and any joins in "tv_shows".
FROM tv_shows
-- LEFT JOIN keyword returns all records from "tv_shows" table, and matched records from "tv_show_genres".
LEFT JOIN tv_show_genres
-- ON clause, separates the join terms from the filtering terms.
ON tv_show_genres.show_id = tv_shows.id
-- WHERE clause filters out the results.
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
