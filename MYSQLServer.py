import mysql.connector
from mysql.connector import Error

try:
    # Connect to the MySQL server (assuming localhost with default port and root user)
    connection = mysql.connector.connect(host='localhost', user='root', password='Yvonneboss@88')

    if connection.is_connected():
        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Create the database if it does not already exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error: {e}")

finally:
    if 'connection' in locals():
        # Close the database connection
        connection.close()
