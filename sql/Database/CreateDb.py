import sqlite3

def create_db():
    try:
        sqlite_connection = sqlite3.connect("Database.db")
        sqlite_select_query = """
            CREATE TABLE sqlitedb_developers(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                group_ TEXT NOT NULL,
                direction TEXT NOT NULL,
                email TEXT NOT NULL,
                joining_date datetime,
                age INTEGER NOT NULL,
                salary REAL NOT NULL
            );
        """
        cursor = sqlite_connection.cursor()
        print("DB create")

        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        print(record)
        cursor.close()

    except sqlite3.Error as error:
        print(error)

    finally:
        if(sqlite_connection):
            sqlite_connection.close()
            print("Close DB")

create_db()