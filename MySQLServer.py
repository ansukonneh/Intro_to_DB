import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mayking@3",
    database="alx_book_store"
)

print("Alx database is printed", mydb.get_server_info())