
## Coding for Data Science and Data Management — Lab Exercises

### 28 October 2025 — *Folder: `notebooks`*

- Creating and populating a SQLite database  
  *(“SQLite in Python” notebook)*  
- Creating and populating a PostgreSQL database  
  *(“Postgres in Python” notebook)*  
- Understanding key differences between SQLite and PostgreSQL, and when to use each
- Using SQL and Pandas together:
  - Database access through SQLAlchemy
  - Query execution with Pandas (`read_sql`)  
  *(“SQL in Pandas” notebook)*
- Comparing results from Pandas vs. direct SQL execution

---

### 29 October 2025 - *Folder: `notebooks` + `movie_app-sqlite`*

- Completing the exercises in the *“SQL in Pandas”* notebook. Showing (`to_sql`) function in Pandas.
- Demonstrating a real example that combines Python + SQL + Pandas:
  - **movie_app** (folder: `movie_app-sqlite`)
  - Uses a premade frontend library (**Streamlit**)
- **movie_app** originally created by *Darya Shlyk*  
  - Modified by *Vojimir Ranitovic* (SQLite database added with direct database connection)

---


## 18 November 2025 — *Folder: `notebooks`*

### `mongo1.ipynb`
This lesson introduces the fundamentals of using MongoDB with Python. It covers:
- Connecting to a MongoDB database using the **PyMongo** library  
- Performing basic queries with `find()`  
- Updating documents  
- Counting query results  
- An initial introduction to the **aggregation pipeline**, demonstrating simple `$match` (filtering) and `$group` (summarizing) operations

---

## 19 November 2025 — *Folder: `notebooks`*

### `mongo2.ipynb`
This lesson focuses on advanced data analysis using MongoDB’s aggregation framework.  
It explains and applies a wide range of operators to solve practical problems, such as analyzing shopping habits. Key concepts include:
- Using `$unwind` to deconstruct array fields  
- Using `$project` to reshape documents  
- Using `$facet` to run multiple aggregations in parallel  
- Using `$elemMatch` to query within arrays  
- Implementing a more efficient method for managing database connections

