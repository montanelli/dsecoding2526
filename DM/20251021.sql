-- for each genre, return the number of movies 
select genre, count(*) as n_movies
from imdb.genre
group by genre
order by n_movies desc

-- for each movie of 2012, return the number of genres and the title of the movie 
-- do not exclude the id: the title is not unique and the risk is that records belonging to different movies with same title are put together
select id, official_title, count(*)
from imdb.movie inner join imdb.genre on id = movie
where year = '2012'
group by movie.id, official_title  

-- do we need to use left/right join?
-- right join is equivalent to inner since we cannot have records of genre without link to movies
-- left join includes in the result the movies without genre
-- consider all the movies without filtering those of 2012 (so we can see differences on  count(*) and count(genre))
select id, official_title, count(*), count(genre)
from imdb.movie left join imdb.genre on id = movie
-- where year = '2012'
group by movie.id, official_title 
order by 4

-- example
id  title     genre
001 django    thriller
001 django    drama
002 envelope  comedy
003 Regina    [NULL]
 
-- for each movie, return the number of involved persons
select movie, count(person), count(*)
from imdb.crew 
group by movie 
 
-- for each movie, return the number of involved persons for each role
select movie, p_role, count(person), count(*)
from imdb.crew 
group by p_role, movie
order by movie
 
 crew
 movie person p_role
 001	ABC   writer   *
 001    DEF   writer   *
 002 	ABC   writer   ** 
 001	GFD	  actor    *** 
 001	HFD   actor    ***
 002    GFD   actor    ****
 
 -- return the persons that played as actors in more than 10 movies 
 select person, count(movie)
 from imdb.crew 
 where p_role = 'actor'
 group by person 
 having count(movie) > 10 
 
 -- for each year, return the sum of length for the movies of that year 
select year, sum(length)
from imdb.movie 
group by "year" 

-- only consider movies after 1970
select year, sum(length)
from imdb.movie 
where year > '1970'
group by "year" 

-- only consider years with less that 10 hours of duration 
select year, sum(length)
from imdb.movie 
where year > '1970'
group by "year" 
having sum(length)/60 < 10

-- return the title of movies with more than 50 actors 
select id, official_title, count(person)
from imdb.crew inner join imdb.movie on id = movie 
where p_role = 'actor'
group by id, official_title 
having count(person) > 50

-- return the movie(s) with the highest number of associated genres
-- explain is used to get estimations on the execution time of a query
-- explain analyze 
select id, official_title, count(genre)
from imdb.movie left join imdb.genre on id = movie
group by movie.id, official_title 
having count(genre) >= all (
select count(genre)
from imdb.genre 
group by movie
)

-- alternative solution
select id, official_title, count(genre)
from imdb.movie left join imdb.genre on id = movie
group by movie.id, official_title 
having count(genre) = (
select count(genre)
from imdb.genre 
group by movie
order by 1 desc
limit 1
)

-- alternative solution with cte
-- common table expression
with movie_counts as (
select movie, count(genre) as mc
from imdb.genre 
group by movie),
max_count as (
select max(mc) as mmax
from movie_counts)
select *
from imdb.movie  left join movie_counts on movie.id = movie_counts.movie 
where mc = (select mmax from max_count);



