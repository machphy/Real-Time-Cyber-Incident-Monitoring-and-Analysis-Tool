import psycopg2
from psycopg2 import sql

# Database connection details
DB_NAME = "cybersecurity"
DB_USER = "cyber_admin"
DB_PASSWORD = "123456789"
DB_HOST = "localhost"
DB_PORT = "5432"

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
)
cur = conn.cursor()

# Read schema.sql and execute
with open("database/schema.sql", "r") as schema_file:
    schema_sql = schema_file.read()
    cur.execute(schema_sql)

# Commit changes and close connection
conn.commit()
cur.close()
conn.close()

print("✅ Database initialized successfully!")
