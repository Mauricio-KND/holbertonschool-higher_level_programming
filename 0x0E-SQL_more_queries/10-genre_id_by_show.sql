-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- SELECT is used to retrieve rows selected from one or more tables.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
-- JOIN clause link data between tables based on values of common columns.
JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
