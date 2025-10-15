-- retrieve title of movies of 2010
SELECT official_title
FROM movie
WHERE year = '2010';

-- retrieve all the attributes of movies of 2010 with length greater than one hour
SELECT *
FROM movie
WHERE year = '2010' AND length > 60;

-- retrieve all the attributes of movies of 2010 with length betweem 1 and 2 hours (excluding extremes)
SELECT *
FROM movie
WHERE year = '2010' AND length > 60 AND length < 120;

-- retrieve all the attributes of movies not realized in 2010 with length betweem 1 and 2 hours (including extremes) 
SELECT *
FROM movie
WHERE year <> '2010' AND length >= 60 AND length <= 120;

-- retrieve the persons whose death date is known
SELECT given_name, death_date
FROM person
WHERE death_date is not null;

-- retrieve the persons that have "Mark" in the given name
SELECT given_name
FROM imdb.person 
WHERE given_name like '%Mark%';

-- retrieve the persons that have "Mark" as first name
SELECT given_name
FROM imdb.person 
WHERE given_name like 'Mark %';

-- retrieve the persons that have "Mark" as last name
SELECT given_name
FROM imdb.person 
WHERE given_name like '% Mark';

-- retrieve the title of movies of 2010 or 2011 or 2012
select id, official_title
From imdb.movie
where year = '2010' OR year = '2011' OR year = '2012';

select id, official_title
From imdb.movie
where year IN ('2010', '2011', '2012');

-- retrieve the title of movies of 2010 or length between one and two hours;
select id, official_title, year, length
From imdb.movie
where year = '2010' OR length > 60 AND length < 120
order by year DESC, length;

-- retrieve the title of movies produced in USA
SELECT official_title, country
FROM movie INNER JOIN produced ON movie.id = produced.movie
WHERE produced.country = 'USA'; 

-- retrieve the countries in which movies of 2010 have been released (return the movie title, both the official and the released one (where available))
SELECT r.country as paese, m.official_title as "titolo ufficiale", r.title as "titolo di distribuzione"
FROM released r, movie AS m
WHERE r.movie = m.id AND m.year = '2010';

SELECT r.country as paese, m.official_title as "titolo ufficiale", r.title as "titolo di distribuzione"
FROM released r INNER JOIN movie AS m ON r.movie = m.id
WHERE m.year = '2010';

-- retrieve the movies for which the title released in Italy is not defined
SELECT id, official_title
FROM imdb.movie, imdb.released
WHERE movie.id = released.movie AND title IS NULL;

-- retrieve the name of actors in the movie Inception
SELECT given_name, official_title, p_role
FROM movie INNER JOIN crew ON movie.id = crew.movie INNER JOIN person ON crew.person = person.id
WHERE official_title = 'Inception' AND p_role = 'actor';

-- retrieve the actors that joined movies of 2010
SELECT distinct person
FROM crew INNER JOIN movie ON crew.movie = movie.id
WHERE year = '2010';

-- retrieve the persons for which birth and death coutries are different 
SELECT l1.person, given_name, l1.country as "paese di nascita", l2.country as "paese di decesso"
FROM location l1 INNER JOIN location l2 ON l1.person = l2.person INNER JOIN person ON l1.person = person.id
WHERE l1.d_role = 'B' AND l2.d_role = 'D' AND l1.country <> l2.country;

-- retrieve the movies without associated materials
SELECT *
FROM movie LEFT JOIN material ON movie.id = material.movie
WHERE material.movie is null;

-- retrieve the countries without produced movies
SELECT *
FROM country LEFT JOIN produced ON country.iso3 = produced.country
WHERE produced.country is null;

SELECT *
FROM produced RIGHT JOIN country ON country.iso3 = produced.country
WHERE produced.country is null;

SELECT * 
FROM country
WHERE iso3 NOT IN 
(SELECT country FROM produced);

-- retrieve the movie with highest/lowest/avg length
SELECT max(length)
FROM movie;

SELECT min(length)
FROM movie;

SELECT avg(length)
FROM movie;

-- return also code and title of the movie in the previous query
SELECT id, official_title, length
FROM movie
WHERE length = 
(SELECT max(length)
FROM movie);


-- retrieve the overall length of 2010 movies
SELECT sum(length)
FROM movie
WHERE year = '2010'

-- retrieve the number of stored movies
SELECT count(*)
FROM movie;

SELECT count(id)
FROM movie;

-- retrieve the number of stored movies for which the title is defined
SELECT count(official_title)
FROM movie;

-- retrieve the number of movies with different title
SELECT count(distinct official_title)
FROM movie;

-- retrieve the number of movies by year
SELECT year as "anno", count(*) as "numero di pellicole per l'anno"
FROM movie
GROUP BY year
ORDER BY year;

-- retrieve the years after 2010 in which more than 10 movies have been produced
SELECT year, count(*)
FROM movie
WHERE year >= '2010'
GROUP BY year
HAVING count(*) > 10
ORDER BY year;

-- for each movie, retrieve the number of persons involved for each role 
SELECT movie, p_role, count(*)
FROM crew
GROUP BY movie, p_role
ORDER BY movie, p_role;

-- retrieve the average movie length for each year (sorted) 
SELECT year, avg(length)
FROM movie
GROUP BY year
ORDER BY year;

-- retrieve the number of persons by role
SELECT p_role AS ruolo, count(*)
FROM crew
GROUP BY p_role;

-- retrieve the movies with more than 10 actors in the crew 
SELECT movie, official_title, count(*)
FROM crew INNER JOIN movie ON crew.movie = movie.id
WHERE p_role = 'actor'
GROUP BY movie, official_title
HAVING count(*) > 10;

-- retrieve the persons that played more than one role 
SELECT person, count(*)
FROM crew
GROUP BY person
HAVING count(distinct p_role) > 1

-- retrieve the best rating score for each movie 
SELECT movie, max(score)
FROM rating
GROUP BY movie;

-- retrieve the title of movies whose length is greater than Inception 
SELECT official_title
FROM movie 
WHERE lengh > 
(SELECT length
FROM movie
WHERE official_title = 'Inception');

-- retrieve the movies produced in ITA and USA
SELECT movie
FROM produced
WHERE country = 'ITA' AND movie IN 
(SELECT movie
FROM produced 
WHERE country = 'USA');

-- alternative solution
SELECT p_italy.movie
FROM produced AS p_italy INNER JOIN produced AS p_usa ON p_italy.movie = p_usa.movie
WHERE p_italy.country = 'ITA' AND p_usa.country = 'USA'; 

-- alternative solution
SELECT movie, official_title
FROM produced INNER JOIN movie ON movie = id
WHERE country = 'ITA'
INTERSECT
SELECT movie, official_title
FROM produced  INNER JOIN movie ON movie = id
WHERE country = 'USA';

-- retrieve the movies produced only in ITA
SELECT movie
FROM produced
WHERE country = 'ITA' AND movie NOT IN 
(SELECT movie
FROM produced 
WHERE country <> 'ITA');

-- alternative solution
SELECT movie
FROM produced
WHERE country = 'ITA'
EXCEPT
SELECT movie
FROM produced
WHERE country <> 'ITA';

-- retrieve the actor that played in the highest number of movies 
SELECT person
FROM crew
WHERE p_role = 'actor'
GROUP BY person
HAVING count(*) >= all
(SELECT count(*)
FROM crew
WHERE p_role = 'actor'
GROUP BY person);
