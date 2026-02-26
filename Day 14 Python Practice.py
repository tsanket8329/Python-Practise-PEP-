import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="school",
    user="postgres",
    password="123"
)

cur = conn.cursor()

# Reset table (learning mode)
cur.execute("DROP TABLE IF EXISTS employees")
conn.commit()

# Create table with auto id
cur.execute("""
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    salary INT
)
""")
conn.commit()

# Insert data
cur.execute(
    "INSERT INTO employees (name, salary) VALUES (%s, %s)",
    ('Rahul', 50000)
)
conn.commit()

# Fetch data
cur.execute("SELECT * FROM employees")
for row in cur.fetchall():
    print(row)

cur.close()
conn.close()
