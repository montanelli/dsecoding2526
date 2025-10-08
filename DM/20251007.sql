-- this is an example of many-to-many relationship 
CREATE TABLE imdb.genre (
	movie varchar(10) NOT NULL REFERENCES movie(id),
	genre varchar(20) NOT NULL,
	PRIMARY KEY (movie, genre)
);

INSERT INTO imdb.genre VALUES ('004949', 'Thriller');

UPDATE imdb.genre SET movie = '4849859' WHERE movie = '004949';
-- this statement is successfully executed if:
-- the pair (4849859, Thriller) is not already stored in imdb.genre (duplication of PK)
-- a movie 4849859 exists in imdb.movie

DELETE FROM imdb.genre WHERE movie = '4849859'; -- no issues related to referential integrity constraints: we are deleting tuples from imdb.genre only

DELETE FROM imdb.movie WHERE id = '4849859'; -- this command is aborted (no delete) if records in genre with movie = '4849859' are existing (violation of FK constraint)

UPDATE imdb.movie SET id = '48499' WHERE id = '4849859'; -- this command is aborted (no update) if records in genre with movie = '4849859' are existing (violation of FK constraint)

-- consider a different referential integrity policy on the FK: cascade option
CREATE TABLE imdb.genre (
	movie varchar(10) NOT NULL REFERENCES movie(id) ON UPDATE CASCADE,
	genre varchar(20) NOT NULL,
	PRIMARY KEY (movie, genre)
);

DELETE FROM imdb.movie WHERE id = '4849859'; -- this command is aborted (no delete) if records in genre with movie = '4849859' are existing (violation of FK constraint)

UPDATE imdb.movie SET id = '48499' WHERE id = '4849859'; -- this command is performed, so 1) the record in table movie with id = '4849859' is updated to id = '48499', 2) the records in genre with movie = '4849859' are updated to movie = '48499'

-- consider this other case on referential integrity constraints
CREATE TABLE A (
	a varchar,
	b varchar, 
	c varchar primary key
);

CREATE TABLE B (
	d varchar primary key REFERENCES A(c) ON DELETE CASCADE,
	e varchar
);

CREATE TABLE C (
	f varchar PRIMARY KEY REFERENCES B(d),
	g varchar
);

INSERT INTO A VALUES ('aa', 'bb', 'cc');
INSERT INTO B VALUES ('cc', 'ee');
INSERT INTO C VALUES ('cc', 'gg');

DELETE FROM A WHERE c = 'cc'; -- error: I cannot leave the records of C with referencees to records of B that have been deleted due to cascade

-- consider this other case with different policies on referential integrity
CREATE TABLE A (
	a varchar,
	b varchar, 
	c varchar primary key
);

CREATE TABLE B (
	d varchar primary key REFERENCES A(c),
	e varchar
);

CREATE TABLE C (
	f varchar PRIMARY KEY REFERENCES B(d) ON DELETE CASCADE,
	g varchar
);

DELETE FROM B WHERE d = 'cc'; -- successful: records from C are deleted due to cascade. the records of A are consistent (not affected by deletions on B)


-- focus on extraction: SELECT command 
-- extract/retrieve the records of movies produced in 2010
SELECT *
FROM imdb.movie
WHERE year = '2010';

-- retrieve the movies of 2010 with length greater than 60 minutes 
SELECT id, official_title, year
FROM imdb.movie
WHERE year = '2010' and length > 60;

id      year    length
001		2010	78	-- appended to the result of the query 
002		2009	68	-- discarded
003		2010	15 	-- discarded
003		2006	29	-- discarded

-- retrieve the movies of 2010 or movies with length greater than 60 minutes 
SELECT id, official_title, year
FROM imdb.movie
WHERE year = '2010' or length > 60;

id      year    length
001		2010	78	-- appended to the result of the query
002		2009	68	-- appended to the result of the query
003		2010	15 	-- appended to the result of the query
003		2006	29	-- discarded

-- retrieve movies not from 2010 (different from 2010)
SELECT id, official_title, year
FROM imdb.movie
WHERE not (year = '2010');

-- same as:
SELECT id, official_title, year
FROM imdb.movie
WHERE year <> '2010';

id      year   
001		2010	-- discarded 
002		2009	-- appended to the result of the query
003	    [NULL]  N  -- ATTENTION: discarded


-- retrieve movies where the length is unknown
SELECT id, official_title, year
FROM imdb.movie
WHERE length is null; 

-- retrieve movies where the length is known (we have a value)
SELECT id, official_title, year
FROM imdb.movie
WHERE length is null and year is not null;

-- movies in the interval between 2010 and 2020
SELECT id, official_title, year
FROM imdb.movie
WHERE year >= '2010' and year <= '2020';

-- same as:
SELECT id, official_title, year
FROM imdb.movie
WHERE year between '2010' and '2020'; 

-- movies in the interval between 2010 and 2020 (boundaries excluded)
SELECT id, official_title, year
FROM imdb.movie
WHERE year >= '2010' and year < '2020';

-- brackets to determine the precedences when multiple boolean operators are applied
-- without brackets, the operators are executed from left to right
SELECT id, official_title, year
FROM imdb.movie
WHERE (year >= '2010' and year < '2020') or length > 60;

-- retrieve the movies that are produced in 2010, 2011, 2012
SELECT id, official_title, year
FROM imdb.movie
WHERE year = '2010' or year = '2011' or year = '2012'

-- same as:
SELECT id, official_title, year
FROM imdb.movie
WHERE year between '2010' and '2012';

-- same as:
SELECT id, official_title, year
FROM imdb.movie
WHERE year in ('2010', '2011', '2012');

-- retrieve the movies that are not from 2010, 2013, 2015
SELECT id, official_title, year
FROM imdb.movie
WHERE year not in ('2010', '2013', '2015');

-- retrieve the persons that are named Mark
-- like operator. we need a placeholder
-- % is a placeholder to denote a string of any length 
select * 
from imdb.person 
where given_name like '%Mark%'

-- retrieve the person with firstname as Mark 
select * 
from imdb.person 
where given_name like 'Mark %'

-- retrieve the person with lastname as Mark 
select * 
from imdb.person 
where given_name like '% Mark'

-- retrieve the person with middlename as Mark 
select * 
from imdb.person 
where given_name like '% Mark %'

-- ilike is the case-insensitive like 

-- retrieve the movies will kill/Kill/KILL inside the title
select * 
from imdb.movie 
where official_title ilike '%kill%'

-- ilike is not supported by all the DBMS
-- same as:
select * 
from imdb.movie 
where lower(official_title) like '%kill%'

-- retrieve the movies with genre Thriller or Drama
select distinct movie
from imdb.genre 
where genre = 'Thriller' or genre = 'Drama'
order by movie;

-- retrieve the ratings of movies from the highest value to the lowest 
select *
from imdb.rating 
order by score desc

-- retrieve the ratings of movies based on score normalized on scale 
select *, score/scale as scaled_score
from imdb.rating 
-- order by scaled_score desc
order by 7 desc 

-- retrieve the ratings of movies based on score normalized on scale. Consider only ratings with more than 1000 votes
select *, score/scale as scaled_score
from imdb.rating 
where votes > 1000 
order by 7 desc 

-- retrieve the movies from 2010 to 2020 and sort the result by year (descending order) and title
select * 
from imdb.movie 
where year between '2010' and '2020'
order by year desc, official_title

-- retrieve the title and year of movies with genre Thriller 
select movie
from imdb.genre 
where genre = 'Thriller';

-- we join the table genre with the table movie to get the result
-- this is the cartesian product of genres and movies 
select *
from imdb.genre, imdb.movie 
where genre ilike 'thriller' ;

-- join means that you filter the cartesian product and keep only records where the movie id is the same in the two tables 
select id, official_title, year
from imdb.genre, imdb.movie 
where genre ilike 'thriller' and genre.movie = movie.id ;

-- example of join on few instances 
genre
movie 	genre
001    	Thriller
002 	Thriller

movie
id   	official_title ...
001    	ABC
002	   	DEF
003 	GHI

genre x movie 
movie  genre  	 id  	official_title ... 
001    Thriller  001   	ABC  ok
001    Thriller  002   	DEF	 discarded 
001    Thriller  003   	GHI  discarded
002    Thriller  001   	ABC  discarded
002    Thriller  002   	DEF  ok
002    Thriller  003   	GHI  discarded

-- ok are records in the join if we use genre.movie = movie.id as a join condition

-- retrieve the score of movies of 2010
select *
from imdb.rating, imdb.movie
where rating.movie = movie.id and year = '2010'

