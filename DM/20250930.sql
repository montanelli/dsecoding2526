-- DDL
CREATE TABLE imdb.country (
	iso3 bpchar(3) NOT NULL,
	"name" varchar(50) NOT NULL,
	UNIQUE (name),
	PRIMARY KEY (iso3)
);

-- empty strings and blank strings are not considered as null valuess
INSERT INTO imdb.country VALUES ('ZZX', null); -- error on insert: null violation on name
INSERT INTO imdb.country VALUES ('ZZZ', ''); -- succesful insert: empty string is not a violation for not null constraint
INSERT INTO imdb.country VALUES ('ZZY', '    '); -- successful insert: blank string is not a violation for not null constraint
INSERT INTO imdb.country(iso3) VALUES ('ZZQ'); -- error on insert: a null is inserted as a default for name attribute and this is a violation for the not null constraint

CREATE TABLE imdb.cinema (
	"name" varchar(50) NOT NULL CHECK (trim()"name") <> ''),
	city varchar(50) NOT NULL CHECK (trim(city) <> ''),
	address varchar(100) NOT NULL CHECK (trim(address) <> ''),
	phone varchar(50),
);
-- trim: remove heading and trailing blanks from a string
-- check performs custom constraints on the records

key: address (PK) 
key: phone
key: name, address  (superkey)

-- do we have to introduce an id?!


INSERT INTO imdb.cinema(name) VALUES ('Ducale'); -- error: cannot insert records with null on city and address
INSERT INTO imdb.cinema(name, city, address) VALUES ('Ducale', 'Milan', 'Piazza Napoli'); -- ok
INSERT INTO imdb.cinema VALUES ('Orfeo', 'Milan', ''); -- error: empty string not possible due to check
INSERT INTO imdb.cinema VALUES ('Orfeo', '', ''); -- error: empty string not possible due to check
INSERT INTO imdb.cinema VALUES ('Orfeo', '', '         '); -- error: empty string not possible due to check
INSERT INTO imdb.cinema(name, city, address) VALUES ('Orfeo', 'Milan', ''); -- ok if the check is not specified

'     i     ' ->trim-> 'i'
'          ' ->trim-> ''

-- keys -> attribute (or set of attributes) that are UNIQUE (two records cannot have the same value on the key attributes)

CREATE TABLE imdb.movie (
	official_title varchar(200) NOT NULL,
	budget numeric(12, 2), -- 9,999,999,999.99
	"year" bpchar(4),
	length int4 ,
	plot text,
    UNIQUE (official_title, year)
);

-- what is the key?
-- we can have multiple keys
key: (official_title, year),
key: (official_title, budget) 

INSERT INTO movie(official_title, year) VALUES ('Dracula', '1967'); -- successful insert
INSERT INTO movie(official_title, year) VALUES ('Dracula', '2002'); -- not a violation of uniqueness wrt the previous
INSERT INTO movie(official_title, year) VALUES ('Dracula', '2002'); -- duplicate of the previous: violation on unique(official_title, year)
INSERT INTO movie(official_title, year) VALUES ('Dracula', null); -- ok: not a violation for unique

-- a primary key is a key that cannot be null
CREATE TABLE imdb.movie (
	official_title varchar(200) NOT NULL,
	budget numeric(12, 2), -- 9,999,999,999.99
	"year" bpchar(4),
	length int4 ,
	plot text,
    PRIMARY KEY (official_title, year)
);

INSERT INTO movie(official_title, year) VALUES ('Dracula', null); -- error: nulls on primary keys is not possbile

-- in a table there is exactly one and only one PK

CREATE TABLE imdb.movie (
    id varchar(10) PRIMARY KEY,
	official_title varchar(200) NOT NULL ,
	budget numeric(12, 2), -- 9,999,999,999.99
	"year" bpchar(4),
	length int4 ,
	plot text,
    UNIQUE (official_title, year)
);

--> PRIMARY KEY means UNIQUE and NOT NULL

INSERT INTO imdb.movie(id, official_title, year) VALUES ('AAD', 'Dracula', '1967');
INSERT INTO imdb.movie(id, official_title, year) VALUES ('AAE', 'Dracula', '1967'); -- error: duplicate on the natural identifier of the table (official_title, year)

CREATE TABLE imdb.person (
    id varchar(10) NOT NULL,
	bio text NULL,
	birth_date date NULL, -- '2025-09-23'
	death_date date NULL,
	given_name varchar(100) NOT NULL,
	CONSTRAINT person_pkey PRIMARY KEY (id)
);

key: bio
key: given_name, birth_date 
key: id (PK) 


-- this table describes the association of movies and genres
-- this is a MANY-TO-MANY relationship
CREATE TABLE imdb.genre (
	movie varchar(10) NOT NULL REFERENCES movie(id), -- this is a foreign key 
	genre varchar(20) NOT NULL,
	PRIMARY KEY (movie, genre)
);

-- genre.movie is referring to the attribute movie.id 
-- we can say that: 
--- any record of table genre refer to one and only one record of table movie 

INSERT INTO imdb.genre VALUES ('FSDKKF', 'Thriller'); 
-- if this insert is successful it means that a record in movie exists with movie.id = 'FSDKKF'

-- a foreign key is a constraint on an attribute T1.A that refers to an attribtute T2.B with T1 called eferencing table and T2 called referenced table 

INSERT INTO imdb.genre VALUES ('4093999', 'Thriller'); -- successful insert
-- is it possible that the movie id=4093999 is not existing in table movie? no, the movie with id = 4093999 must be existing in table movie
-- is it possible that more than one movie with id = 4093999 is existing? no, the referenced attribute must be unique in the referenced table (movie.id)



