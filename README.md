🐍 Python Daily Practice
This repository documents my daily Python learning journey as part of full-stack development.

📅 Progress Tracker

Day 01 – Python Fundamentals
Basics & Type Casting
Input / Output
Conditional Statements
Loops
Functions & Lambda
Lists, Tuples, Sets
Logical Programs

Day 02 – Python Core Concepts
Dictionary & Dictionary Methods
Menu-Driven Programs using Dictionary
String Manipulation & String Methods
String Logical Programs (reverse, palindrome, duplicates)
File Handling (read, write, append)
Exception Handling (try, except and finally)

Day 03 - Python Advanced and logical concepts
list Operations and List Logical Programs
Tuple, Set and Dictionary Conversions
Looping Pattern(for, while, else)
Error and Exception Handling
try, except, else, finally
Built-in Errors(ZeroDivisionError, ValueError, TypeError, etc.)
Raising Errors(raise)
Custom Exceptions
Mutable vs Immutable Data Types
Functions Behavior and Return Flow
String and List Logical Programs
Move zeros to end
Longest words in the sentence
Palindrome and duplicates
Problem-Solving Approaches
Brute force logic
Pair sum/Target sum problems

Day 04 - Python Mini Projects and File-Based Applications
Menu-Driven Program Design
Functions-Based Program Structure
Global Variable and global keyword
File Handling for Data Persistence
Load data from file
Save updated data to file
ATM Simulator Project
Balance check
Deposit and withdrawl logic 
PIN verification and change
Data storage using files
Quiz Application Project
Questions and answers using lists
Score caculation
High-score tracking using files
Conditional Logic for score comparison
Program Flow Control using main()
Error Handling with try / except

Focus of Day04: Building real-word mini projects, understanding program flow,
                file-based data storage and modular coding using functions..!

Day 05- Object Oriented Programming(OOP) in Python
Introduction to OOP

Class as a blueprint
Object Creation
Constructors(init)
No-argument constructor
Parameterized constructor
Multiple parameter in constructor
Inastance Variable and object Attribute
Class Variable(shared data)
Access via object and class name
Updating class attributes
Normal Methods
Defining and calling instance methods
Static Method(concept)
Real life Class Examples
Student, Car, Companny, College
Counting Objects using Class Attributes
Mutuable vs Immutable Behaviour in OOP Context
Four Pillar of OOP
Encapsulation
Abstraction
Inheritance
Polymorphism
Encapsulation
Private Variable
Getter and Setter methods
Bank and Account Examples
Hidden Balance
Deposit and withdraw logic
Secure data access using methods

Focus on Day 05: Understanding core OOP concepts, class design, data handling, and implementing real world logic using encapsulation..!!


Day 06: Python Practise
This notebook covers basic Object-Oriented Programming(OOP) concepts in Python, including:
Inheritance
Multiple Inheritance
super()
public private protected
Diamond problem
Polymorphism
Reference

Day 7: OOPS CONCEPTS(Brief)
Abstraction shows what to do and hides how to do.Used to reduce complexity in large programs.

Abstract Class contains both implemented and non-implemented methods.
Child class completes the abstract methods.

Interface pure rule class with only method declarations.All methods must be implemented by the child class.

Abstract Class vs Interface Abstract Class->partial implementation interface->only rules,no logic

Composition(HAS-A) One class uses the object of another class.Preferred when inheritance is not needed.

Mini Projects(OOPS-PYTHON)
1.Library Management System
Demonstration Abstraction,Inheritance,Polymorphism,Encapsulation
LibraryItem->Parent class
Book,Magazine->Child classes(IS-A)
LibraryApp->Controller(HAS-A)
Different items calculate borrowing charges differently
Sample Output:
Iten type:Book->Borrow Days:5 -> Charge:50
Item type: Magzine->Borrow Days:3 ->Charge:30 

2.Employee Payroll System
Demonstrate all 4 pillars of OOPS
Employee -> Abstract class
FullTimeEmployee, PartTimeEmployee->
Child classes
Salary->Encapsulated data
PayrollSystem->Controller(HAS-A)
Salary calculation differs based on employee type
Sample Output:
Employee Created -> Salary:500000
Employee Created -> Salary:40000

3.Bank Account Managemant System
Demonstrate Abstraction, Encapsulatin,Inheritance,Polymorphism
BankAccount->Parent/abstract behaviour
SavingAccount,Current Account->Child classes
BankApp->Controller(HAS-A)
Interest calculation varies by account type
Key Features:
Deposit
Withdraw
Balance check
Interest calculation
!..Summary..!
These mini projects helped in understanding:
Real-world uses of OOPS concepts
IS-A and HAS-A relationships
Controller-based application design
Clean and reusable code structure

Day 8: Python  Practise
Import Libraries
Random Module
DataTime Module
Collections Module
Regular Expressions

Day 9 Python Practice
Regex to validate 10-digit mobile number
Extract email IDs from a string
Extract numbers from alphanumeric text
Strong password validation using regex
PAN number validation
IPv4 address validation
IPv6 address validation
Hexadecimal value validation
Sys module usage
Random number generation
Even and odd number checking
Mathematical operations and rounding
Frequency counting using collections
File handling concepts
OS module for directory and file handling
Random password generation
Password strength checking
Character count in password
Strength score calculation


Day 10 Python Practice
This practice file demonstrates hands-on MySQL database operations using the MySQL command-line interface. It focuses on building a strong foundation in SQL basics and data analysis queries.
Key concepts covered:
Creating and managing databases and tables (CREATE, USE, DROP, TRUNCATE)
Inserting and retrieving data (INSERT, SELECT)
Filtering records using conditions (WHERE, AND, OR)
Sorting and limiting results (ORDER BY, LIMIT)
Aggregate functions:
AVG, SUM, COUNT, MAX, MIN
Grouping data for analysis (GROUP BY)
Using aliases for better readability
Performing real-world style queries on:
Student data
Candidates data
Employee data
Identifying and fixing SQL syntax errors
Analyzing data by department, city, gender, salary, and experience
Outcome: This exercise strengthens practical SQL skills required for data analysis, backend development, and database management, with real-life table structures and queries

Day 11 Python Practice
Primary Key - Not null + unique Not NULL - Unique Syntax for foreign jey - student_id REFERENCES student(student_id) INNER JOIN → A ∩ B
LEFT JOIN → A ∪ (A ∩ B) → A + A^B | RIGHT JOIN → B ∪ (A ∩ B) → B + A^B | FULL JOIN → A ∪ B

Day 12 Python Practice
A subquery is a query inside another query, used when one question depends on the result of another.

Transaction (All or Nothing) A transaction is a sequence of SQL operations executed as a single unit where either all changes are committed or all are rolled back. It starts with a transaction, executes multiple SQL statements, and ends with either commit or rollback.

Indexing Indexing helps SQL find data faster, similar to a book index or page number. Without an index, the database scans every row from beginning to end, which is slow. With an index, the database directly jumps to the required data, which is fast.
SQL Commands Are Divided Into Five Types

Data Definition Language (DDL) – Structure (Design) CREATE, ALTER, DROP, RENAME, TRUNCATE

Data Manipulation Language (DML) – Data (Rows) INSERT, UPDATE, DELETE

Data Query Language (DQL) – Fetch Data SELECT

Data Control Language (DCL) – Security GRANT, REVOKE

Transaction Control Language (TCL) – Transactions SAVEPOINT, COMMIT, ROLLBACK

Normalization Normalization is the process of converting a messy and unorganized table into clean, well-structured tables.

Why Normalization? Reduces data duplication Avoids insert anomaly

Day 13 Python Practice

TYPES OF NORMALIZATION:
1NF-> ONE CELL SHOULD NOT HAVE MORE THAN ONE VALUE -> ATOMIC VALUES -> DEFINITION --> EACH COLUMN SHOULD CONTAIN ATOMIC (SINGLE) VALUE
2NF-> TABLE MUST BE 1NF -> NO PARTIAL DEPENDENCY
3NF-> TABLE MUST BE 2NF -> NOT DEPENDENT ON ANOTHER ROW WHICH IS ALREADY DEPENDENT ON ANY OTHER ROW -> NO TRANSITIVE DEPENDENCY SQLite: IT IS A LIGHTWEIGHT DATABASE THAT STORES DATA IN A SINGLE FILE AND IS INBUILT IN PYTHON
COMMANDS IN SQLite:

connect()--> OPENS DATABASE cursor()--> RUNS SQL execute()--> EXECUTES SQL commit()--> SAVE CHANGES close()--> CLOSES CONNECTION Avoids update anomaly Avoids delete anomaly

Day 14 Python Practice
A simple Python script demonstrating PostgreSQL connectivity using psycopg2.
 It creates an employees table, inserts sample data, and fetches records from the database

 Day 15 – Python API Integration & JSON Handling

Today I learned how to connect Python with real-world data using APIs and handle JSON responses effectively.                    
I practiced sending HTTP requests, checking status codes, and handling errors using try and except. I also built a simple Weather App that fetches live weather data based on city input and displays formatted results.
This helped me understand client-server communication and how backend systems interact with external services.

Day 15 Python Practice
This file contains PostgreSQL and SQL practice focusing on database creation, table design, constraints, joins, transactions, and indexing

Key Topics:
Tables & constraints (PK, FK, UNIQUE, CHECK)
INSERT & SELECT queries
INNER & LEFT JOIN
GROUP BY
Transactions (BEGIN / ROLLBACK)
Index creation
Tools: PostgreSQL, SQL, Python 


Day 16 Python Practice
It focuses on ORM (Object Relational Mapping) in Python
Demonstrates how Python code is mapped to a database table
Uses SQLAlchemy as the ORM tool
Shows how to:
Create a database connection (SQLite)
Define a base class using declarative_base()
Create an Employee model/class
Map class attributes to table columns
The file is basically a practice/example of converting Python classes into SQL tables

Day 17 Python Practice
This file (Day 17 Python Practice.ipynb) mainly contains SQLAlchemy ORM practice, focused on understanding how Python code maps to database tables.
Introduction to ORM (Object Relational Mapping) and its purpose (Python ↔ SQL)
Basic SQLAlchemy imports like declarative_base, sessionmaker, and relationship
Small notes/practice cells explaining concepts (for example: operators like ==)
Steps to connect an engine to a database
Practice code related to table creation using ORM
A mini project section where ORM models and project-style code are written

Day 18 Python Practice
Project Personal Finance Manager

A Command Line Interface (CLI) based Personal Finance Tracker built using Python, SQLite, and SQLAlchemy ORM. This project helps users manage daily expenses, track subscriptions, monitor category-wise spending, and control monthly budgets.

Features: Add and manage expense categories 2) Record daily transactions (expenses) 3) Update entries 4) delete incorrect or extra entries 5) Search expenses by date 6) View category-wise spending summary (using Raw SQL) 7) Set monthly budgets for categories 8) Get budget alerts when spending exceeds the limit 9) Track subscriptions (Netflix, Gym, etc.) 10) Persistent storage using SQLite database

Technologies Used:

Python 3 SQLite Database SQLAlchemy ORM Raw SQL Queries CLI (Command Line Interface)

Database Schema:

The application uses four relational tables with proper foreign key relationships.

Categories Stores different types of spending categories. Fields: id — Integer, Primary Key name — String, name of the category (e.g., Food, Travel) Relationship: One category can have many transactions One category can have many budgets Transactions Stores all expense records entered by the user. Fields: id — Integer, Primary Key amount — Float, money spent description — String, expense details date — String, date of transaction (YYYY-MM-DD) category_id — Integer, Foreign Key referencing categories.id Relationship: Many transactions belong to one category Budgets Stores monthly spending limits for each category. Fields: id — Integer, Primary Key category_id — Integer, Foreign Key referencing categories.id month — String, month in format YYYY-MM budget_limit — Float, maximum allowed spending Relationship: Many budget records can belong to one category Used to compare actual spending vs planned budget Subscriptions Stores recurring expenses separately. Fields: id — Integer, Primary Key name — String, subscription name (e.g., Netflix) amount — Float, subscription cost start_date — String, start date (YYYY-MM-DD) end_date — String, end/renewal date Relationship: Independent table (not linked to categories) Relationship Summary Category → Transactions = One-to-Many Category → Budgets = One-to-Many Transactions → Category = Many-to-One Budgets → Category = Many-to-One Subscriptions = Standalone entity
How It Works(Workflow):

User creates categories (Food, Travel, etc.) User records transactions under categories System stores all data using SQLAlchemy ORM User can: Update or delete transactions Search by date View category spending summary User sets monthly budgets System compares spending with budget and shows alerts Subscriptions are tracked separately for recurring expenses

FLOW CHART(workflow):

START | v User Runs Program | v Database Connection Established (SQLite + SQLAlchemy) | v Tables Created (Categories, Transactions, Budgets, Subscriptions) | v Main Menu Displayed | v User Chooses an Option | v Add Category (1) | Enter Category Name | Category Stored in DB | v Back to Menu | v Update Transaction (3) --> Enter Transaction ID --> Modify Details --> Save --> Back | v Delete Transaction (4) --> Enter Transaction ID --> Delete Record --> Back | v Search by Date (5) --> Enter Date --> Fetch Matching Transactions --> Display --> Back | v Category Summary (6) | v Run RAW SQL JOIN (Categories + Transactions) | v Calculate SUM(amount) GROUP BY Category | v Display Category-wise Spending | v Back to Menu | v Set Budget (7) | v Enter Category ID, Month (YYYY-MM), Budget Limit | v Budget Stored in Budgets Table | v Back to Menu | v Budget Alert (8) | v Enter Month (YYYY-MM) | v System Calculates Total Spending per Category for that Month | v Compare Spending with Budget Limit | v If Spent > Limit → ALERT Else → Within Budget | v Back to Menu | v Add Subscription (9) | v Enter Name, Amount, Start Date, End Date | v Subscription Stored in DB | v Back to Menu | v User Selects Exit (0) | v Program Ends | v END

How to Run the Project: 1)Install dependencies: pip install sqlalchemy

Run the program: python finance_tracker.py CLI Menu Options:

Add Category Add Transaction Update Transaction Delete Transaction Search Transaction by Date Category Summary Set Budget Budget Alert Add Subscription Exit Learning Outcomes:

This project demonstrates: ORM-based database interaction SQL JOINs and aggregation CLI application design Budget tracking logic Modular programming with Python

Future Enhancements: Export reports to CSV Flask Web Interface User Authentication Charts and visual 


Day 19 Python Practice
Django is high level python web frameweork used to build websites , APIs ,Backend systems , Admin dashboard MTV - Model(Database) Template(Frontend) View (Business logic) MTV is a structure followed by Django -- Frontend =Bcakend= Database Model - Books table in database View - Logic to fetch the books Template - HTML page showing books setting.py - project settings urls - routing manage.py - run the command GET - fetch data POST - Create data PUT - update full PATCH - update partial DELETE - Delete data 200 - success 201 - created 400 - bad request 401 - unauthorized 403 - forbidden 404- not found 500 - server error Summary - I created a virtual environment and installed Django.
I created a Django project (config) and ran the server.

Django showed a warning about unapplied migrations (database tables not created yet).

I created an app named core.

I got an ImportError because the hello view didn’t exist.

After creating the hello view, the server worked.

hello works ✅

shows 404 because I didn’t define a root URL.

I still need to run python manage.py migrate to create the default database tables.

Apps in Django – Django projects are divided into small modules called apps. Each app handles a specific functionality of the project (for example: users, products, blog).

Migrations – Django uses migrations to create and update database tables automatically based on the models defined in the project.

ORM (Object Relational Mapper) – Django ORM allows developers to interact with the database using Python code instead of writing raw SQL queries.

Admin Panel – Django provides a built-in admin dashboard that allows developers to manage database records like users, products, and posts easily.
