import sqlite3

def read_sqlite_table():
    try:
        sqlite_connection = sqlite3.connect("Database.db")
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """
            SELECT * from sqlitedb_developers
        """

        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        return records

    except sqlite3.Error as error:
        print(error)

    finally:
        if sqlite_connection:
            cursor.close()