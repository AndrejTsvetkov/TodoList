import tkinter as tk
import database
from datetime import datetime, date


class ToDo(tk.Frame):
    week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("To-Do")
        self.master.minsize(width=300, height=400)
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(master=self.master, bg="#353a40")
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.frame.columnconfigure((0, 1), weight=1)
        self.frame.rowconfigure(3, weight=1)

        self.weekday_label = tk.Label(master=self.frame, text=ToDo.week_days[datetime.now().weekday()],
                                      font="Roboto 16 bold",
                                      bg="#353a40", fg="#e2e9f1")
        self.date_label = tk.Label(master=self.frame, text=date.today().strftime("%b %d, %Y"), font="Roboto 12",
                                   bg="#353a40",
                                   fg="#5c636b")
        self.weekday_label.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.date_label.grid(row=1, column=0, columnspan=2, sticky="new")

        self.empty_label = tk.Label(master=self.frame, bg="#353a40")
        self.empty_label.grid(row=2, column=0, columnspan=2, sticky="nsew")

        self.todo_list = tk.Listbox(master=self.frame, font="Roboto 16 italic", bg="#353a40", bd=0, fg="#DFDFDD",
                                    highlightthickness=0, selectbackground="#273a64")
        self.todo_list.grid(row=3, column=0, columnspan=2, sticky="nsew")

        self.entry_todo = tk.Entry(master=self.frame, font="Roboto 14 italic", fg="#DFDFDD", justify="left", bd=0,
                                   width="10",
                                   bg="#343434")
        self.entry_todo.grid(row=4, column=0, sticky="nsew")

        self.insert_btn = tk.Button(master=self.frame, text="Add",
                                    background="#343434",  # фоновый цвет кнопки
                                    foreground="#DFDFDD",  # цвет текста
                                    activebackground="#1D1D1D",
                                    activeforeground="#8C8C8C",
                                    borderwidth=0,
                                    padx="0",  # отступ от границ до содержимого по горизонтали
                                    pady="0",  # отступ от границ до содержимого по вертикали
                                    font="Roboto 14",  # высота шрифта
                                    command=self.add_item
                                    )

        self.delete_btn = tk.Button(master=self.frame, text="Delete selected",
                                    background="#343434",  # фоновый цвет кнопки
                                    foreground="#DFDFDD",  # цвет текста
                                    activebackground="#1D1D1D",
                                    activeforeground="#8C8C8C",
                                    borderwidth=0,
                                    padx="0",  # отступ от границ до содержимого по горизонтали
                                    pady="0",  # отступ от границ до содержимого по вертикали
                                    font="Roboto 14",  # высота шрифта
                                    command=self.delete_item
                                    )
        self.insert_btn.grid(row=4, column=1, sticky="nsew")
        self.delete_btn.grid(row=5, column=0, columnspan=2, sticky="ew")

        self.get_data_from_database()

    def get_data_from_database(self):
        current_list_of_tasks = database.get_tasks()
        for task in current_list_of_tasks:
            self.todo_list.insert(tk.END, task[0])

    def add_item(self):
        # добавить проверку на невидимые символы (например пробел в задаче)
        if self.entry_todo.get():
            self.todo_list.insert(tk.END, self.entry_todo.get())
            database.insert_task(self.entry_todo.get(), 0)
            self.entry_todo.delete(0, tk.END)

    def delete_item(self):
        self.todo_list.delete(tk.ACTIVE)


def main():
    root = tk.Tk()
    app = ToDo(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()
