SQL (Structure Querty Language) is a declarative language for doing the following things with databases:
- create the schema (DDL - data definition language) - CREATE/ALTER/DROP 
- populate the schema (DML - data manipulation language) - INSERT/UPDATE/DELETE 
- query the database (DQL - data query languge) - SELECT
- define the permissions on data (DCL - data control language)

a table in a relational db is composed by:
- a schema: field/attribute names with related constraints
- an instance: the set of records/rows stored in the table

in a schema we have constraints:
- domains (datatypes)
- nulls -> missing values (non-existing values and existing values but not known)
- check (custom constraints on the data)
- keys / primary keys
- foreign keys

when you define a table you must declare the keys, namely the set of attributes that univocally identifies each record of the table 

in a table we can have multiple keys 
a key can be null (unless you specify not null)
among the keys one and only one is elected as primary key 
a primary key is unique and not null 
a key can be composed by one attribute or a set of attributes 

if A is a key you can say that two records cannot exist with same value on the attribute A 

CREATE TABLE imdb.movie (
	id varchar(10) NOT NULL,
	official_title varchar(200) NOT NULL,
	budget numeric(12, 2), -- 9,999,999,999.99
	"year" bpchar(4),
	length int4 ,
	plot text ,
	CONSTRAINT length_check CHECK ((length > 0)),
	CONSTRAINT movie_pkey PRIMARY KEY (id),
	UNIQUE(official_title, year)
);

-- use of title, year as key
inception, 2010
inception, 2020
inception, 2010 -- duplicate
Inception, 2010 -- ok

-- with the id all record are ok, I cannot recognize records with duplicate pair (title, year)
MOV001 - inception, 2010
MOV002 - inception, 2020
MOV003 - inception, 2010 
MOV004 - Inception, 2010 

id is a key 
official_title, year is a key (we choose them as a key)

CREATE TABLE imdb.person (
	id varchar(10) NOT NULL,
	bio text NULL,
	birth_date date NULL, -- '2025-09-23'
	death_date date NULL,
	given_name varchar(100) NOT NULL,
	CONSTRAINT person_pkey PRIMARY KEY (id)
);

CREATE TABLE imdb.crew (
	person varchar(10) NOT NULL,
	movie varchar(10) NOT NULL,
	p_role imdb."person_role" NOT NULL,
	"character" varchar(200) NULL,
	CONSTRAINT crew_person_movie_p_role_pk PRIMARY KEY (person, movie, p_role)
);



