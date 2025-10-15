-- retrieve the score of movies of 2010
-- syntax of a inner join operation
select *
from imdb.rating, imdb.movie
where rating.movie = movie.id and year = '2010'

-- alternative syntax
select *
from imdb.rating inner join imdb.movie on rating.movie = movie.id
where  year = '2010'

-- retrieve the name of actors in the Inception movie 
select person.id as "person id", person.given_name, "character" 
select *
from imdb.movie inner join imdb.crew on movie.id = crew.movie inner join imdb.person on person.id = crew.person 
where official_title = 'Inception' and p_role = 'actor'
order by given_name 

-- retrieve the movies produced in GBR and USA
-- wrong solution: empty result
select *
from imdb.produced
where country = 'GBR' and country = 'USA'

-- wrong solution: the result is larger than expected 
select *
from imdb.produced
where country = 'GBR' or country = 'USA'
order by movie

-- solution with subquery
select movie, country
from imdb.produced
where country = 'USA' and movie in (
select movie
from imdb.produced 
where country = 'GBR')

-- check on a sample 
select *
from imdb.produced 
where movie ='0049470'

-- solution with join
select gbr_movies.movie 
from imdb.produced usa_movies, imdb.produced gbr_movies
where usa_movies.country = 'USA' and gbr_movies.country = 'GBR'
and a.movie = b.movie 

-- solution with set operation 
-- we are looking for the intersection of two sets 
-- requirements: same number of attributes in projection and same type
-- only identical records in the two query resuls are returned
select movie
from imdb.produced 
where country = 'GBR'
intersect 
select movie
from imdb.produced 
where country = 'USA'

-- retrieve the movies without rating 
movie 
id  title
001  ABC
002  DEF -- this is the expected result

rating 
check_date  movie   score 
2025-10-14  001     8.5
2025-10-13	001     7.5 

-- solution with subquery
select id
from imdb.movie
where id not in 
(select distinct movie
from imdb.rating)

-- solution with set operation 
-- we want the records in the first query that are not belonging to the second query: minus operation (except operator is defined in SQL to implement this operation)
-- requirements: same number of attributes in projection and same type
-- only identical records in the two query resuls are returned
select id
from imdb.movie
except 
select distinct movie
from imdb.rating

-- further set operation: union 
-- retrieve the set of movies produced in ITA or FRA
-- requirements: same number of attributes in projection and same type
-- only identical records in the two query resuls are returned
select movie
from imdb.produced 
where country = 'ITA'
union
select movie
from imdb.produced 
where country = 'FRA'

-- alternative solution
select movie
from imdb.produced 
where country = 'ITA' or country = 'FRA'



-- external join operations 
-- consider an alternative solution to the following query
-- retrieve the movies without rating 

movie inner join rating on id = movie
id    title  ...   check_date   movie   score
001   ABC  		   2025-10-14   001     8.5
001   ABC  		   2025-10-13	001     7.5


-- consider two tables A, B
-- A left join B: the result is the inner join + the possible spourious records of table A (the one on the left of the join operation)
movie left join rating on id = movie
id    title  ...   check_date   movie   score
001   ABC  		   2025-10-14   001     8.5
001   ABC  		   2025-10-13	001     7.5
002   DEF		   [NULL]		[NULL]	[NULL]

-- retrieve the movies without rating 
select * 
from imdb.movie left join imdb.rating on id = movie
where rating.movie is null;

-- consider two tables A, B
-- A right join B: the result is the inner join + the possible spourious records of table B (the one on the right of the join operation)
movie right join rating on id = movie
id    title  ...   check_date   movie   score
001   ABC  		   2025-10-14   001     8.5
001   ABC  		   2025-10-13	001     7.5
-- the result of right is the same as inner
-- we know it by definition: rating cannot contain dandling pointers to non-existing movies in table movie (FK constraint)

rating right join movie on id = movie
check_date   movie   score ... id    title
2025-10-14   001     8.5       001   ABC
2025-10-13	 001     7.5       001   ABC
[NULL]		[NULL]	[null]	   002   DEF

-- consider two tables A, B
-- A full [outer] join B: the result is the inner join + the possible spourious records of table A (the one on the left of the join operation) + the possible spourious records of table B (the one on the right of the join operation


-- aggregate operators (functions)
-- MIN/MAX
-- AVG
-- SUM
-- COUNT

-- retrieve the movie with highest/lowest/avg length
select max(length) as "max duration", min(length) as min_length, avg(length) as "average length", round(avg(length), 0)
from imdb.movie 

-- retrieve the title of the movies with the highest length 
-- this is not a solution: error due to impossibility to recall the record(s) that generated the max
select id, official_title, max(length) 
from imdb.movie

-- the solution is based on two steps
-- first: find the max
-- second: retrieve the record with the max value
select id, official_title, length
from imdb.movie 
where length = 
(select max(length) 
from imdb.movie)

-- the same with the min length
select id, official_title, length
from imdb.movie 
where length = 
(select min(length) 
from imdb.movie)


-- retrieve the movie with highest/lowest/avg length considering the movies of 2012
select max(length) as "max duration", min(length) as min_length, avg(length) as "average length", round(avg(length), 0)
from imdb.movie
where year = '2012'

-- retrieve the title of the movies of 2012 with longest duration
select * 
from imdb.movie 
where year = '2012' and length = 
(select max(length) 
from imdb.movie
where year = '2012')

-- retrieve the thriller movies with highest/lowest/avg length 
select max(length) as "max duration", min(length) as min_length, avg(length) as "average length", round(avg(length), 0)
from imdb.movie inner join imdb.genre on id = movie 
where genre = 'Thriller'

-- retrieve the most recent year of production for movies 
select *
from imdb.movie 
where year = 
(select max(year)
from imdb.movie)

-- retrieve the overall length of 2010 movies
select sum(length) as length_in_minutes, sum(length)/60 as length_in_hours
from imdb.movie 
where year = '2010'

-- retrieve the number of stored movies
-- count: counting the number of rows that belongs to the result of a query
select count(*)
from imdb.movie

-- retrieve the number of movies from 2012
select count(*)
from imdb.movie
where year = '2012'

-- retrieve the number of stored movies for which the title is defined
-- count([field]) means that you count the values on the field excluding nulls
select count(official_title)
from imdb.movie

-- the same as
select count(*)
from imdb.movie
where official_title is not null

-- count the movies without year
select count(year)
from imdb.movie


-- the same as
select count(*)
from imdb.movie
where year is not null

-- count the number of different years in which movies are produced 
select count(distinct year)
from imdb.movie

-- comparison on count operator
select count(*), count(year), count(distinct year)
from imdb.movie 

-- retrieve the number of movies with different title
select count(*), count(official_title)
from imdb.movie

-- retrieve the number of movies for each year
movie
id  year
001 2010  *
002 2011  **
003 2010  *
004 2012  ***
005 2011  **
006 2010  *

-- solution
select year, count(*)
from imdb.movie 
group by year 
order by 2 desc

-- incorrect solution: you cannot project attributes that are not appearing in the group by 
select id, year, count(*)
from imdb.movie 
group by year 
order by 2 desc

-- retrieve the number of persons involved in each movie 
select movie, count(person)
from imdb.crew 
group by crew.movie

-- retrieve the number of actors involved in each movie 
select movie, count(person)
from imdb.crew 
where p_role = 'actor'
group by crew.movie

-- retrieve the number of movies for each person
select person, count(movie)
from imdb.crew 
group by crew.person

-- retrieve the number of movies for each director
select person, given_name, count(movie)
from imdb.crew inner join imdb.person on person.id = crew.person 
where p_role = 'director'
group by crew.person, given_name 
order by 3 desc

crew inner join person id=person
person  movie  p_role  id  given_name
001     ABC		dir.   001  Paul    *
001     DEF		dir.   001  Paul    *
002     ABC     act.   002  Jane    ** 
001     JFG		dir.   001  Paul    *
002     FIR     dir.   002  Jane    ** 


