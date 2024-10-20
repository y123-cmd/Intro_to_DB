def create_database():
    """ Create a database in MySQL server """
    connection = None  
    try:
        # Establish a connection to MySQL
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  
            password='Yvonneboss@88'  
        )

<<<<<<< HEAD
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
=======
        # Your new code or changes here
>>>>>>> branch-name
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection and connection.is_connected():  
            cursor.close()
            connection.close()

