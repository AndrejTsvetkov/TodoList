import tkinter as tk


def main():

    root = tk.Tk()
    root.title("To-Do List")
    root.minsize(width=300, height=400)

    frame = tk.Frame(master=root, bg="#121212")
    frame.pack(fill=tk.BOTH, expand=True)
    frame.columnconfigure(0, weight=1, minsize=200)
    frame.rowconfigure(0, weight=1, minsize=300)

    todo_list = tk.Listbox(master=frame, font="Roboto 16 italic", bg="#121212", bd=0, fg="#DFDFDD",
                           highlightthickness=0, selectbackground="#273a64")
    todo_list.grid(row=0, column=0, columnspan=2, sticky="nsew")
    todo_list.insert(tk.END, 'Привет')
    todo_list.insert(tk.END, 'Пока')

    entry_todo = tk.Entry(master=frame, font="Roboto 14 italic", fg="#DFDFDD", justify="left", bd=0, width="10",
                          bg="#343434")
    entry_todo.grid(row=1, column=0, sticky="nsew")

    insert_btn = tk.Button(master=frame, text="Добавить",
                           background="#343434",  # фоновый цвет кнопки
                           foreground="#DFDFDD",  # цвет текста
                           activebackground="#1D1D1D",
                           activeforeground="#8C8C8C",
                           borderwidth=0,
                           padx="0",  # отступ от границ до содержимого по горизонтали
                           pady="0",  # отступ от границ до содержимого по вертикали
                           font="Roboto 14",  # высота шрифта
                           )
    insert_btn.grid(row=1, column=1, sticky="nsew")

    root.mainloop()


if __name__ == '__main__':
    main()
