import mysql.connector
from mysql.connector import Error

def create_database():
    """ Create a database in MySQL server """
    connection = None  # Initialize connection variable
    try:
        # Establish a connection to MySQL
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Replace with your username if different
            password='Yvonneboss@88'  # Replace with your password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection and connection.is_connected():  # Check if connection was established
            cursor.close()
            connection.close()

if __name__ == '__main__':
    create_database()

