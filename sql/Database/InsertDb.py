import sqlite3

def insert_variable(name, email, gr, direction, joining_date, age, salary):
    try:
        sqlite_connection = sqlite3.connect("./Database.db")
        cursor = sqlite_connection.cursor()
        print("connected")

        sqlite_insert_query = """
            INSERT INTO sqlitedb_developers
            (name, email, gr, direction, joining_date, age, salary)
            VALUES(?, ?, ?, ?, ?, ?, ?);
        """

        data = (name, email, gr, direction, joining_date, age, salary)
        cursor.execute(sqlite_insert_query, data)
        sqlite_connection.commit()
        print("Good")
        cursor.close()

    except sqlite3.Error as error:
        print(error)

