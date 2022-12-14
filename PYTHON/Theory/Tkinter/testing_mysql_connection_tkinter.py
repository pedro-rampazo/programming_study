import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P*e*d*r*o*16541815",
    database="sum_numbers"
)

my_cursor = mydb.cursor()

my_cursor.execute("SELECT * FROM `math_expression`")

print(my_cursor)
