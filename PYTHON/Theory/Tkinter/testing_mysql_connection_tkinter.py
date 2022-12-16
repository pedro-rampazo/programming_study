import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="****",
    database="sum_numbers"
)

my_cursor = mydb.cursor()

my_cursor.execute("SELECT * FROM `math_expression`")

for x in my_cursor:
    print(x)
