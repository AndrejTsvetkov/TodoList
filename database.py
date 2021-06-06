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
# conn.close() deal with "close" issue
# c.execute("SELECT time('now')")
# print(c.fetchall())


# If we didn't finish any tasks yesterday they will be deleted automatically the next day
def delete_not_done_tasks():
    with conn:
        c.execute("DELETE FROM todolist WHERE task_status = 0 AND date < date('now', 'localtime')")


def get_current_tasks():
    delete_not_done_tasks()
    c.execute("SELECT task_name FROM todolist WHERE task_status = 0")
    return c.fetchall()


def get_done_tasks():
    c.execute("SELECT task_name, date FROM todolist WHERE task_status = 1")
    return c.fetchall()


def insert_task(task_name, task_status):
    with conn:
        c.execute("INSERT INTO todolist (task_name, task_status, date) VALUES (?, ?, date('now'))",
                  (task_name, task_status))


def make_task_done(task_name):
    with conn:
        c.execute("UPDATE todolist SET task_status = 1 WHERE task_status = 0 AND task_name = :task_name",
                  {'task_name': task_name})


# We are deleting task in that case when we added one with wrong name or we decided we wouldn't do it today,
# so in WHERE clause we check task_status (you can't delete task that already done) and date.
def delete_task(task_name):
    with conn:
        c.execute("DELETE FROM todolist WHERE task_status = 0 AND date == date('now') and task_name = :task_name",
                  {'task_name': task_name})


def get_todays_completed_tasks():
    c.execute("SELECT task_name FROM todolist WHERE task_status = 1 AND date == date('now')")
    return c.fetchall()
