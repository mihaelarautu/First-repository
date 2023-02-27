import sqlite3

con = sqlite3.connect("students.db")
cursor = con.cursor()

cursor.execute("INSERT INTO Students (name, email, age) VALUES('Adam', 'adam@g.com', 28)")
cursor.execute("INSERT INTO Students (name, email, age) VALUES('Eva', 'eva@g.com', 26)")

cursor.execute("SELECT * FROM Students")
print(cursor.fetchall())

grades_values = [
    ('WEB DEV', 8, 1),
    ('DB DEV', 9, 1),
    ('DB DEV', 6, 2),
    ('FRONTEND DEV', 9, 2),
    ('WEB DEV', 9, 2),
    ('WEB DEV', 8, 2),
    ('WEB DEV', 7, 7)
]
SQL_query = "INSERT INTO GRADES (topic, grade, student_id) VALUES (?,?,?)"
cursor.executemany(SQL_query, grades_values)
cursor.execute("SELECT * FROM Grades")
print(cursor.fetchall())
con.commit()
