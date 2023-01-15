# SQL

### 🔶 1. What types of relationships between tables do you know?

---
#### Answer:
Types of relationships between tables are:
- One-to-One: where one record in table A corresponds to one record in table B
- One-to-Many: where one record in table A corresponds to multiple records in table B
- Many-to-Many: where multiple records in table A correspond to multiple records in table B
### 🔶 2. What types of JOIN do you know? What is the difference?

---
#### Answer:
- INNER JOIN: only returns records where there is a match in both tables
- LEFT JOIN: returns all records from the left table and any matching records from the right table
- RIGHT JOIN: returns all records from the right table and any matching records from the left table
- FULL OUTER JOIN: returns all records from both tables
### 🔶 3. What is selectivity?

---
#### Answer:
Selectivity is the degree to which the values of a column in a table are unique. A column with high selectivity has unique values, while a column with low selectivity has many repeating values. This is important when creating indexes, because an index on a column with high selectivity will be more efficient than an index on a column with low selectivity.
### 🔶 4. Have you ever profiled requests?

---
#### Answer:
Profiling requests is the process of measuring the performance of a database query and identifying bottlenecks. This can be done using tools such as the EXPLAIN command in SQL or a database profiler.

#### Example:
```postgresql
EXPLAIN SELECT * FROM users_table WHERE name = 'Alice';
```
### 🔶 5. What is the difference between explain and explain analyze?

---
#### Answer:
The difference between EXPLAIN and EXPLAIN ANALYZE is that EXPLAIN shows the execution plan of the query without actually running it, while EXPLAIN ANALYZE not only shows the execution plan but also runs the query and provides statistics on its performance.

### 🔶 6. In what order is the SELECT query evaluated?

---
#### Answer:
SELECT query is evaluated in the following order:
- FROM clause
- JOIN clause
- WHERE clause
- GROUP BY clause
- HAVING clause
- SELECT clause
- ORDER BY clause
### 🔶 7. What is an index?

---
#### Answer:
An index is a database feature that allows for faster searching and sorting of data. Indexes can be created on one or more columns of a table, and are used to quickly locate specific rows in the table.
### 🔶 8. What indexes do you know?

---
#### Answer:
Types of indexes:
- B-Tree index
- Bitmap index
- Hash index
- Full-text index
- Spatial index

### 🔶 9. What is B-Tree?

---
#### Answer:
B-Tree index is a balanced tree data structure that stores data in a sorted order and allows for efficient insertion, deletion and search operations. It is commonly used in databases to improve the performance of SELECT, INSERT and UPDATE operations. In a B-Tree, the data is stored in a balanced tree, so the height of the tree is always

---

## Here is a list of features that correspond to the Middle+ level:
- You quickly answer simple questions about indexes.
- You are answering a question about transaction isolation levels.
- You have experience in query profiling and optimization.
- You can write complex queries such as window functions and CTEs.
- You understand when not to write complex queries.

### <a href="#top"> Back to top ⬆️</a>
