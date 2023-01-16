# Connect to the database
import sqlite3
conn = sqlite3.connect('student_db.db')
cursor = conn.cursor()

# Open and read the contents of query_1.sql
with open('query_10.sql', 'r') as file:
    sql = file.read()

# Execute the query
cursor.execute(sql)

# Fetch and print the results
results = cursor.fetchall()
for row in results:
    print(row)

# Close the connection
conn.close()