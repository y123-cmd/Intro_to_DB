import mysql.connector
from mysql.connector import Error

def create_database():
    """ Create a database in MySQL server """
    connection = None
    try:
        # Establish a connection to MySQL
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Adjust as needed
            password='Yvonneboss@88'  # Adjust as needed
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    create_database()

