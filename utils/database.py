import mysql.connector  

def db_connection():
    try:
        
        connection = mysql.connector.connect(
            host='your_host',
            user='your_user',
            password='your_password',
            database='your_database'
        )
        print("Database connection successful")
        return connection
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None

def close_connection(connection):
    if connection:
        connection.close()
        print("Database connection closed")
