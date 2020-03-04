-- Lists all Comedy shows in the database hbtn_0d_tvshows.
-- SELECT statement with clauses. 
The tv_genres table contains only one record where name = Comedy
SELECT tv_shows.title
FROM tv_genres INNER JOIN tv_show_genres
	ON (tv_genres.name = 'Comedy' and tv_show_genres.genre_id = tv_genres.id)
	INNER JOIN tv_shows
	ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title ASC;
