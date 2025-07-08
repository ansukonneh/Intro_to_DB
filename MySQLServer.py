import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server (no DB specified yet)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mayking@3"
    )

    if mydb.is_connected():
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Alx database is printed", mydb.get_server_info())

except Error as e:
    print(" Error:", e)

finally:
    if 'mycursor' in locals():
        mycursor.close()
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
