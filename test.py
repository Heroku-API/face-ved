# import mysql.connector as sql
#
# connection = sql.connect(
#   host="localhost",
#   user="root",
#   password="root"
# )
#
# print(connection)
# cursor = connection.cursor()
# #cursor.execute("CREATE DATABASE Emp1")
# #cursor.execute("CREATE TABLE Emp1.studentinfo (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), subject VARCHAR(255))")
# query = "INSERT INTO Emp1.studentinfo (name, subject) VALUES (%s, %s)"
# values = [("Krish", "Stats"),
#         ("Joe", "Maths"),
#         ("Ankur","Data Science"),
#         ("Paul","Data Science"),
#         ("Vishal","Maths"),
#         ("Krish","Data Science")]
# cursor.executemany(query,values)
# print("Row inserted",cursor.lastrowid)
# cursor.execute("Select * from Emp1.studentinfo")
# print(cursor.fetchall())
# connection.commit()
a='yash 71.05%'
v,c=a.split()
print(v)