import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None  # Initialize the connection variable outside of the try block
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',  # Change this if your MySQL server is on a different host
            user='root',       # Your MySQL username
            password='Yvonneboss@88'  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()

