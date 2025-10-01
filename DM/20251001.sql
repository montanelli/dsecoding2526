CREATE TABLE imdb.genre (
	movie varchar(10) NOT NULL REFERENCES movie(id), -- this is a foreign key 
	genre varchar(20) NOT NULL,
	PRIMARY KEY (movie, genre)
);

genre.movie -> movie.id  -- this is a foreign key (FK)

-- any record of table genre refers to one and only one record of table movie 
INSERT INTO imdb.genre VALUES ('4093999', 'Thriller');
-- if this insert is successful, we can say that:
--- the combination of ('4093999', 'Thriller') is unique in the table genre 
--- a record with id = '4093999' is existing in table movie 
--- the record in movie with id = '4093999' is unique 

CREATE TABLE imdb.crew (
	person varchar(10) NOT NULL REFERENCES person(id),
	movie varchar(10) NOT NULL,
	p_role imdb."person_role" NOT NULL,
	"character" varchar(200) NULL,
	PRIMARY KEY(person, movie, p_role),
	FOREIGN KEY (movie) REFERENCES movie(id)
);

-- what is the primary key?
-- is it useful to define a serial id? 

INSERT INTO imdb.movie(id, official_title, year, length) VALUES ('00M1', 'Dracula', '2025', 90); -- successful insert
INSERT INTO imdb.movie(id, official_title, year, length) VALUES ('00M2', 'Dracula', '1967', 110); -- successful insert

INSERT INTO imdb.person(id, given_name) VALUES ('00P1', 'Gene Hackman'); -- successful insert 

INSERT INTO imdb.crew(person, movie, p_role) VALUES ('00P1', '00M1', 'producer'); ---successful
INSERT INTO imdb.crew(person, movie, p_role) VALUES ('00P2', '00M3', 'producer'); -- error if 00P2 is not existing in person table; error if 00M3 is not existing in movie table

DELETE FROM imdb.movie where id = '00M1'; -- error: not possible to delete the record since it violates the FK constraint 
DELETE FROM imdb.movie where id = '00M2'; -- no error: deletion is completed since no references are defined in crew for 00M2

UPDATE imdb.movie SET id = '00M4' WHERE id = '00M1'; -- the value of id for the record with id = '00M1 'is replaced by the value '00M4'
-- error: not possible to edit/change/update the id of a record that is referenced by a FK

UPDATE imdb.movie SET id = '00M4' WHERE id = '00M2'; -- no error: the update is completed since no references are defined in crew for 00M2

UPDATE imdb.movie SET year = '2010' WHERE length > 90; -- no problem, change is performed. No involvement of foreign keys

-- referential integrity policies
-- we can change the behavior of referential integrity
CREATE TABLE imdb.crew (
	person varchar(10) NOT NULL REFERENCES person(id) ON DELETE CASCADE ON UPDATE CASCADE,
	movie varchar(10) NOT NULL,
	p_role imdb."person_role" NOT NULL,
	"character" varchar(200) NULL,
	PRIMARY KEY(person, movie, p_role),
	FOREIGN KEY (movie) REFERENCES movie(id) ON DELETE NO ACTION ON UPDATE CASCADE 
);

INSERT INTO imdb.person(id, given_name) VALUES ('00P1', 'Gene Hackman'); 
INSERT INTO imdb.crew(person, movie, p_role) VALUES ('00P1', '00M1', 'producer'); 

DELETE FROM imdb.person WHERE id = '00P1';
-- teh cascade policy says that if you delete a record from the referenced table (person), all the records in referencing tables (crew) are deleted as well
-- the records of crew with person = '00P1' are deleted as a cascade 

UPDATE imdb.person SET id = '00P3' WHERE id = '00P1'; -- the update is successful
-- the cascade policy implies that the same update is propagated to the referencing object
-- the records in crew with person = '00P1' are changes to references to person = '00P3'

CREATE TABLE imdb.rating (
	check_date date NOT NULL,
	"source" varchar(200) NOT NULL,
	movie varchar(10) NOT NULL REFERENCES movie(id) ON UPDATE CASCADE,
	"scale" numeric NOT NULL,
	votes int4 NOT NULL,
	score numeric NOT NULL,
	CONSTRAINT check_score CHECK (((score >= (0)::numeric) AND (score <= scale))),
	PRIMARY KEY (check_date, source, movie)
);

-- is it possible for a source to evaluate a specific movie two times? 

check_date	 source		movie	scale 	votes 	score
2017-10-31  imdb		00M1	10		XXX		7.2
2017-10-30	imdb		00M1	10		XXX		6.9 -- no violations
2017-10-31	imdb		00M2	10		XXX		6.9 
2017-10-31	imdb		00M2	10		XXX		8.1 -- error. duplicate PK

DELETE FROM imdb.rating WHERE check_date = '2017-10-31'; -- no problem with the FK, operation is permitted

DELETE FROM imdb.movie WHERE id = '00M2'; -- error, deleetion is not permitted since the records of rating with movie = '00M2' become inconsistent (NO ACTION policy)

UPDATE imdb.rating SET source = 'Corriere della Sera' WHERE check_date = '2017-10-31'; -- no problem with FKs 

UPDATE imdb.rating SET movie = '00M3' WHERE movie = '00M2'; -- ok, no error provided that a movie with id = '00M3' exists in movie table

UPDATE imdb.movie SET id = '00M9' WHERE id = '00M2'; -- the id of movie '00M2' is changed to '00M9' in movie table. All the references to 00M2 are moved to 00M9 in table rating