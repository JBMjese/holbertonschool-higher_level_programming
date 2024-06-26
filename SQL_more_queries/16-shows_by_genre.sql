USE hbtn_0d_tvshows;

-- Select all shows and their linked genres from the hbtn_0d_tvshows database.
-- NULL is displayed in the genre column for shows without a genre.
-- Results are sorted in ascending order by the show title and genre name.
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
