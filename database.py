import psycopg2
import config

def connect_to_database():
    try:
        connection = psycopg2.connect(dsn=config.db_connection)
        return connection
    except psycopg2.Error as error:
        print("Error connecting to the database:", error)
        return None

def execute_sql_query(sql_query, query_parameters=None):
    connection = connect_to_database()
    if not connection:
        return "Connection Error"

    result = None
    try:
        cursor = connection.cursor()
        cursor.execute(sql_query, query_parameters)

        if sql_query.strip().upper().startswith("SELECT"):
            # Execute SELECT queries for GET requests
            result = cursor.fetchall()
        else:
            # Execute non-SELECT queries (e.g., INSERT, UPDATE, DELETE) for POST requests
            connection.commit()
            result = True

        cursor.close()
    except psycopg2.Error as exception:
        print("Error executing SQL query:", exception)
        result = exception
    finally:
        connection.close()

        return result