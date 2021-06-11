import tkinter as tk
from tkinter import filedialog as fd
import database
from datetime import datetime, date


class ToDo(tk.Frame):
    week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    def __init__(self, conn, master=None):
        super().__init__(master)
        self.conn = conn
        self.master = master
        self.master.title("To-Do")
        self.master.minsize(width=300, height=400)
        p1 = tk.PhotoImage(file='icon/todo_icon.png')
        self.master.iconphoto(False, p1)
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(master=self.master, bg="#353a40")
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.frame.columnconfigure((0, 1), weight=1)
        self.frame.rowconfigure(3, weight=1)

        self.weekday_label = tk.Label(master=self.frame, text=ToDo.week_days[datetime.now().weekday()],
                                      font="Roboto 16 bold",
                                      bg="#27292D", fg="#e2e9f1")
        self.date_label = tk.Label(master=self.frame, text=date.today().strftime("%b %d, %Y"), font="Roboto 12",
                                   bg="#27292D",
                                   fg="#5c636b")
        self.weekday_label.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.date_label.grid(row=1, column=0, columnspan=2, sticky="new")

        self.empty_label = tk.Label(master=self.frame, bg="#27292D")
        self.empty_label.grid(row=2, column=0, columnspan=2, sticky="nsew")

        self.todo_list = tk.Listbox(master=self.frame, font="Roboto 16 italic", bg="#27292D", bd=0, fg="#DFDFDD",
                                    highlightthickness=0, selectbackground="#273a64")
        self.todo_list.grid(row=3, column=0, columnspan=2, sticky="nsew")

        self.entry_todo = tk.Entry(master=self.frame, font="Roboto 14 italic", fg="#DFDFDD", justify="left", bd=0,
                                   width="10",
                                   bg="#2D2F34")
        self.entry_todo.grid(row=4, column=0, sticky="nsew")

        self.insert_btn = tk.Button(master=self.frame, text="Add",
                                    background="#2D2F34",  # фоновый цвет кнопки
                                    foreground="#DFDFDD",  # цвет текста
                                    activebackground="#1D1D1D",
                                    activeforeground="#8C8C8C",
                                    borderwidth=0,
                                    padx="0",  # отступ от границ до содержимого по горизонтали
                                    pady="0",  # отступ от границ до содержимого по вертикали
                                    font="Roboto 14",  # высота шрифта
                                    command=self.add_item
                                    )

        self.delete_btn = tk.Button(master=self.frame, text="Delete",
                                    background="#2D2F34",  # фоновый цвет кнопки
                                    foreground="#DFDFDD",  # цвет текста
                                    activebackground="#1D1D1D",
                                    activeforeground="#8C8C8C",
                                    borderwidth=0,
                                    padx="0",  # отступ от границ до содержимого по горизонтали
                                    pady="0",  # отступ от границ до содержимого по вертикали
                                    font="Roboto 14",  # высота шрифта
                                    command=self.delete_item
                                    )

        self.done_btn = tk.Button(master=self.frame, text="Done",
                                  background="#2D2F34",  # фоновый цвет кнопки
                                  foreground="#DFDFDD",  # цвет текста
                                  activebackground="#1D1D1D",
                                  activeforeground="#8C8C8C",
                                  borderwidth=0,
                                  padx="0",  # отступ от границ до содержимого по горизонтали
                                  pady="0",  # отступ от границ до содержимого по вертикали
                                  font="Roboto 14",  # высота шрифта
                                  command=self.done_item
                                  )

        self.statistic_btn = tk.Button(master=self.frame, text="Get statistic",
                                       background="#2D2F34",  # фоновый цвет кнопки
                                       foreground="#DFDFDD",  # цвет текста
                                       activebackground="#1D1D1D",
                                       activeforeground="#8C8C8C",
                                       borderwidth=0,
                                       padx="0",  # отступ от границ до содержимого по горизонтали
                                       pady="0",  # отступ от границ до содержимого по вертикали
                                       font="Roboto 14",  # высота шрифта
                                       command=self.get_statistic
                                       )

        self.insert_btn.grid(row=4, column=1, sticky="nsew")
        self.delete_btn.grid(row=5, column=1, sticky="ew")
        self.done_btn.grid(row=5, column=0, sticky="ew")
        self.statistic_btn.grid(row=6, column=0, columnspan=2, sticky="ew")

        database.db_init(self.conn)
        self.get_data_from_database()

    def get_data_from_database(self):
        current_list_of_tasks = database.get_current_tasks(self.conn)
        for task in current_list_of_tasks:
            self.todo_list.insert(tk.END, task[0])

    def add_item(self):
        if self.entry_todo.get() and not self.entry_todo.get().isspace():
            self.todo_list.insert(tk.END, self.entry_todo.get())
            database.insert_task(self.conn, self.entry_todo.get(), 0)
            self.entry_todo.delete(0, tk.END)

    def delete_item(self):
        database.delete_task(self.conn, self.todo_list.get(tk.ACTIVE))
        self.todo_list.delete(tk.ACTIVE)

    def done_item(self):
        database.complete_task(self.conn, self.todo_list.get(tk.ACTIVE))
        self.todo_list.delete(tk.ACTIVE)

    def get_statistic(self):
        path = fd.askdirectory(title="Save statistic")
        default_file_name = "statistic.txt"

        if path:
            todays_completed_tasks = database.get_todays_completed_tasks(self.conn)
            with open(f'{path}/{default_file_name}', 'w') as wf:
                wf.write("I`ve done today next tasks:")
                wf.write("\n" * 2)
                for task in todays_completed_tasks:
                    wf.write(f'- {task[0]}\n')


def main():
    default_file_path = "todolist.db"
    conn = database.db_connect(default_file_path)

    root = tk.Tk()
    app = ToDo(conn, master=root)
    app.mainloop()

    database.db_close(conn)


if __name__ == '__main__':
    main()
