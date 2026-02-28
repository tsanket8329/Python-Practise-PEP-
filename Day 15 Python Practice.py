Microsoft Windows [Version 10.0.26100.7462]
(c) Microsoft Corporation. All rights reserved.

C:\Users\Varsha Tiwari>psql --version
psql (PostgreSQL) 18.1

C:\Users\Varsha Tiwari>psql -u postgres
psql: illegal option -- u
psql: hint: Try "psql --help" for more information.

C:\Users\Varsha Tiwari>psql -U postgres
Password for user postgres:

psql (18.1)
WARNING: Console code page (437) differs from Windows code page (1252)
         8-bit characters might not work correctly. See psql reference
         page "Notes for Windows users" for details.
Type "help" for help.

postgres=# \l
                                                              List of databases
     Name      |  Owner   | Encoding | Locale Provider |      Collate       |       Ctype        | Locale | ICU Rules |   Access privileges
---------------+----------+----------+-----------------+--------------------+--------------------+--------+-----------+-----------------------
 mydatabase.db | postgres | UTF8     | libc            | English_India.1252 | English_India.1252 |        |           |
 postgres      | postgres | UTF8     | libc            | English_India.1252 | English_India.1252 |        |           |
 template0     | postgres | UTF8     | libc            | English_India.1252 | English_India.1252 |        |           | =c/postgres          +
               |          |          |                 |                    |                    |        |           | postgres=CTc/postgres
 template1     | postgres | UTF8     | libc            | English_India.1252 | English_India.1252 |        |           | =c/postgres          +
               |          |          |                 |                    |                    |        |           | postgres=CTc/postgres
(4 rows)


postgres=# CREATE DATABASE school;
CREATE DATABASE
postgres=# \c school
You are now connected to database "school" as user "postgres".
school=# CREATE TABLE students(
school(# id INT,
school(# name VARCHAR(50),
school(# age INT);
CREATE TABLE
school=# \dt
            List of tables
 Schema |   Name   | Type  |  Owner
--------+----------+-------+----------
 public | students | table | postgres
(1 row)


school=# INSERT INTO students VALUES(1,'Ram', 18);
INSERT 0 1
school=# INSERT INTO students VALUES(2,'Sita', 19);
INSERT 0 1
school=# select * from students;
 id | name | age
----+------+-----
  1 | Ram  |  18
  2 | Sita |  19
(2 rows)


school=# select * from students where age = 18
school-# ;
 id | name | age
----+------+-----
  1 | Ram  |  18
(1 row)


school=# ALTER TABLE students
school-# ADD PRIMARY KEY (id);
ALTER TABLE
school=# ALTER TABLE students
school-# ALTER COLUMN name SET NOT NULL;
ALTER TABLE
school=# ALTER TABLE students
school-# ALTER COLUMN age SET NOT NULL;
ALTER TABLE
school=# ALTER TABLE students
school-# ADD CONSTRAINT age_check CHECK (age >= 5 AND age <= 100);
ALTER TABLE
school=# ALTER TABLE students
school-# ADD CONSTRAINT unique_student_name UNIQUE (name);
ALTER TABLE
school=# ALTER TABLE students
school-# ALTER COLUMN age SET DEFAULT 18;
ALTER TABLE
school=# CREATE TABLE courses (
school(#     course_id INT PRIMARY KEY,
school(#     course_name VARCHAR(50) NOT NULL
school(# );
CREATE TABLE
school=# ALTER TABLE students
school-# ADD COLUMN course_id INT;
ALTER TABLE
school=# \d students
                      Table "public.students"
  Column   |         Type          | Collation | Nullable | Default
-----------+-----------------------+-----------+----------+---------
 id        | integer               |           | not null |
 name      | character varying(50) |           | not null |
 age       | integer               |           | not null | 18
 course_id | integer               |           |          |
Indexes:
    "students_pkey" PRIMARY KEY, btree (id)
    "unique_student_name" UNIQUE CONSTRAINT, btree (name)
Check constraints:
    "age_check" CHECK (age >= 5 AND age <= 100)


school=# ALTER TABLE students
school-# ADD CONSTRAINT fk_students_courses
school-# FOREIGN KEY (course_id)
school-# REFERENCES courses(course_id);
ALTER TABLE
school=# INSERT INTO courses VALUES (101, 'Mathematics');
INSERT 0 1
school=# INSERT INTO courses VALUES (102, 'Computer Science');
INSERT 0 1
school=# INSERT INTO courses VALUES (103, 'Physics');
INSERT 0 1
school=# INSERT INTO students VALUES (4, 'Arjun', 20, 101);
INSERT 0 1
school=# INSERT INTO students VALUES (5, 'Meera', 21, 102);
INSERT 0 1
school=# INSERT INTO students VALUES (6, 'Ravi', 19, 103);
INSERT 0 1
school=# SELECT s.id, s.name, s.age, c.course_name
school-# FROM students s
school-# INNER JOIN courses c
school-# ON s.course_id = c.course_id;
 id | name  | age |   course_name
----+-------+-----+------------------
  4 | Arjun |  20 | Mathematics
  5 | Meera |  21 | Computer Science
  6 | Ravi  |  19 | Physics
(3 rows)


school=# SELECT s.id, s.name, c.course_name
school-# FROM students s
school-# LEFT JOIN courses c
school-# ON s.course_id = c.course_id;
 id | name  |   course_name
----+-------+------------------
  1 | Ram   |
  2 | Sita  |
  4 | Arjun | Mathematics
  5 | Meera | Computer Science
  6 | Ravi  | Physics
(5 rows)


school=# SELECT c.course_name, COUNT(s.id)
school-# FROM courses c
school-# LEFT JOIN students s
school-# ON c.course_id = s.course_id
school-# GROUP BY c.course_name;
   course_name    | count
------------------+-------
 Computer Science |     1
 Mathematics      |     1
 Physics          |     1
(3 rows)


school=# BEGIN;
BEGIN
school=*# UPDATE students SET age = age + 1 WHERE course_id = 101;
UPDATE 1
school=*# ROLLBACK;
ROLLBACK
school=# CREATE INDEX idx_students_course ON students(course_id);
CREATE INDEX
school=#