DROP DATABASE IF EXISTS moviebot_thing;

CREATE DATABASE moviebot_thing;

USE moviebot_thing;

CREATE TABLE movie
(
	movie_imbd_url			VARCHAR(150)	PRIMARY KEY,
    movie_name				VARCHAR(50)		NOT NULL,
	movie_release_year		INT,
    movie_imdb_url			VARCHAR(150)	NOT NULL,
    movie_imdb_score		DOUBLE
);
