import tkinter as tk
from datetime import datetime, date, time
from functools import partial


def add_item(entry_todo, todo_list):
    if entry_todo.get():
        todo_list.insert(tk.END, entry_todo.get())
        entry_todo.delete(0, tk.END)

    print(todo_list.size())


def main():
    weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    root = tk.Tk()
    root.title("To-Do")
    root.minsize(width=300, height=400)



    frame = tk.Frame(master=root, bg="#121212")
    frame.pack(fill=tk.BOTH, expand=True)
    frame.columnconfigure((0, 1), weight=1)
    frame.rowconfigure((0, 1), weight=1)

    weekday_label = tk.Label(master=frame, text=weekDays[datetime.now().weekday()], font="Roboto 16 ", bg="#121212", fg="#DFDFDD")
    weekday_label.grid(row=0, column=0, columnspan=2, sticky="ew")

    todo_list = tk.Listbox(master=frame, font="Roboto 16 italic", bg="#121212", bd=0, fg="#DFDFDD",
                           highlightthickness=0, selectbackground="#273a64")
    todo_list.grid(row=1, column=0, columnspan=2, sticky="nsew")

    entry_todo = tk.Entry(master=frame, font="Roboto 14 italic", fg="#DFDFDD", justify="left", bd=0, width="10",
                          bg="#343434")
    entry_todo.grid(row=2, column=0, sticky="nsew")

    insert_btn = tk.Button(master=frame, text="Add",
                           background="#343434",  # фоновый цвет кнопки
                           foreground="#DFDFDD",  # цвет текста
                           activebackground="#1D1D1D",
                           activeforeground="#8C8C8C",
                           borderwidth=0,
                           padx="0",  # отступ от границ до содержимого по горизонтали
                           pady="0",  # отступ от границ до содержимого по вертикали
                           font="Roboto 14",  # высота шрифта
                           command=partial(add_item, entry_todo, todo_list)
                           )
    insert_btn.grid(row=2, column=1, sticky="nsew")

    root.mainloop()


if __name__ == '__main__':
    main()
