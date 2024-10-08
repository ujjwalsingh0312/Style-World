import mysql.connector as ms

db1 = ms.connect(
  host="localhost",
  user="root",
  passwd="1234"
)
mycursor = db1.cursor()
if db1.is_connected():
    print(":)")
else:
    print(":(")
mycursor.execute("CREATE DATABASE fashion")
print("Database created successfully!")
