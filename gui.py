import customtkinter as ctk
import tkinter as tk
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE tasks (
    task TEXT NOT NULL
)
''')

conn.commit()

ctk.set_appearance_mode("dark")

label_counter = 0

def add_label():
    frame = ctk.CTkFrame(main_frame)
    frame.pack(side='top', anchor='nw', pady=5, padx=5, fill='x')

    text_content = add_entry.get("1.0", tk.END).strip()
    

    global label_counter
    label_counter += 1
    # Создаем лейбл с текстом и установкой wraplength
    label = ctk.CTkLabel(frame, text=f"{text_content}", wraplength=500, anchor='w')
    label.pack(side='left', padx=5, pady=5, fill='x')

    checkbox = ctk.CTkCheckBox(frame, text='')
    checkbox.pack(side='right', padx=10)

    add_entry.delete("1.0", tk.END)  # Очищаем текстовое поле после добавления задачи

def add_task_win():
    add_win = ctk.CTk()
    add_win.geometry("300x400")
    add_win.resizable(False, False)

    frame = ctk.CTkFrame(master=add_win, width=290, height=390)
    frame.place(x=5, y=5)

    global add_entry
    add_entry = ctk.CTkTextbox(master=frame, width=270, height=90, wrap='word')
    add_entry.place(x=10, y=10)

    add_btn = ctk.CTkButton(master=frame, width=100, height=30, text="Add Task", command=add_label)
    add_btn.place(x=95, y=120)

    add_win.mainloop()

# Инициализация основного приложения
app = ctk.CTk()
app.geometry("600x800")
app.title("Kairos | Planner")
app.resizable(False, False)

# Основной фрейм
main_frame = ctk.CTkFrame(master=app, width=590, height=790)
main_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

# Кнопка для открытия окна добавления задачи
add_task_btn = ctk.CTkButton(master=main_frame, width=30, height=30, text="+", command=add_task_win)
add_task_btn.pack(anchor='se', padx=10, pady=10)

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

app.mainloop()
