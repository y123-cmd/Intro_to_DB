import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host='localhost',  # Change if needed
            user='root',       # Change to your MySQL username
            password='Yvonneboss@88'  # Change to your MySQL password
        )

        # Check if the connection was successful
        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            
    except mysql.connector.Error as e:  # Ensure this line is included
        print(f"Error: '{e}' occurred when trying to create the database.")

    finally:
        # Close the connection and cursor if they were opened
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()

