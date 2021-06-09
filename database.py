import sqlite3


def db_connect(sqlite_file):
    """ Make connection to an SQLite database file """
    return sqlite3.connect(sqlite_file)


def db_close(conn):
    """ Close connection to the database """
    conn.close()


def db_init(conn):
    """ Create table and delete yesterday's not done tasks """
    cur = conn.cursor()
    with conn:
        # 1 - done, 0 - not
        cur.execute("""CREATE TABLE IF NOT EXISTS todolist (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL,
            task_status INTEGER NOT NULL,
            date TEXT NOT NULL
            )""")
        # If we didn't finish any tasks yesterday they will be deleted automatically the next day
        cur.execute("DELETE FROM todolist WHERE task_status = 0 AND date < date('now', 'localtime')")


def get_current_tasks(conn):
    """ Get current tasks """
    cur = conn.cursor()
    cur.execute("SELECT task_name FROM todolist WHERE task_status = 0")
    return cur.fetchall()


def insert_task(conn, task_name, task_status):
    """ Insert task with its status """
    cur = conn.cursor()
    with conn:
        cur.execute("INSERT INTO todolist (task_name, task_status, date) VALUES (?, ?, date('now'))",
                    (task_name, task_status))


def complete_task(conn, task_name):
    """ Mark task as complete """
    cur = conn.cursor()
    with conn:
        cur.execute("UPDATE todolist SET task_status = 1 WHERE task_status = 0 AND task_name = :task_name",
                    {'task_name': task_name})


# We are deleting task in that case when we added one with wrong name or we decided we wouldn't do it today,
# so in WHERE clause we check task_status (you can't delete task that already done) and date.
def delete_task(conn, task_name):
    """ Delete task"""
    cur = conn.cursor()
    with conn:
        cur.execute("DELETE FROM todolist WHERE task_status = 0 AND date == date('now') and task_name = :task_name",
                    {'task_name': task_name})


def get_todays_completed_tasks(conn):
    """ Get today's completed tasks """
    cur = conn.cursor()
    cur.execute("SELECT task_name FROM todolist WHERE task_status = 1 AND date == date('now')")
    return cur.fetchall()
