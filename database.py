import sqlite3

conn = sqlite3.connect('todolist.db')

c = conn.cursor()
# 1 - done, 0 - not
c.execute("""CREATE TABLE IF NOT EXISTS todolist (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL,
            task_status INTEGER NOT NULL,
            date TEXT NOT NULL
            )""")
conn.commit()
# conn.close() думать как решить проблему закрытия
# c.execute("INSERT into todolist (task_name, task_status, date) VALUES (?, ?, date('now'))", ('task1', 1))
# conn.commit()


def get_tasks():
    c.execute("SELECT task_name from todolist where task_status = 0")
    return c.fetchall()


def insert_task(task_name, task_status):
    with conn:
        c.execute("INSERT into todolist (task_name, task_status, date) VALUES (?, ?, date('now'))", (task_name, task_status))


def make_task_done(task_name):
    with conn:
        c.execute("UPDATE todolist SET task_status = 1 WHERE task_status = 0 AND task_name = :task_name", {'task_name': task_name})
