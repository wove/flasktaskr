import sqlite3
from config import DATABASE_PATH


with sqlite3.connect(DATABASE_PATH) as connection:
    c = connection.cursor()

    c.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    due_date TEXT NOT NULL,
                                    priority INTEGER NOT NULL,
                                    status INTEGER NOT NULL)""")

    # Insert dummy data into table
    c.execute("""INSERT INTO tasks(name, due_date, priority, status)
                VALUES('Finish this tutorial', '02/05/2015', 10, 1)""")


    c.execute("""INSERT INTO tasks(name, due_date, priority, status)
                VALUES('Finish course', '02/06/2015', 10, 1)""")

