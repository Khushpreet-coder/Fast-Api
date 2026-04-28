import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="KidanFer22G@",
    database="smart_task_db"
)

cursor = conn.cursor(dictionary=True)