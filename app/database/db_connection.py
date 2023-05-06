import mysql.connector
"""
 Create the connection to the database.
"""
conn = mysql.connector.connect(
    host = 'localhost',
    user = '',
    password = '',
    database = 'tsdb22',
    port = '3306'
)

# Cursor
cursor = conn.cursor()
