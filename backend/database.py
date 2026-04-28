# import mysql.connector

# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="KidanFer22G@",
#     database="smart_task_db"
# )

# cursor = conn.cursor(dictionary=True)


import os
import mysql.connector

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST", "localhost"),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASSWORD", "KidanFer22G@"),
    database=os.getenv("DB_NAME", "smart_task_db")
)

cursor = conn.cursor()