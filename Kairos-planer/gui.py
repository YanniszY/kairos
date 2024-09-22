import customtkinter as ctk
import tkinter as tk
import sqlite3

# Подключение к базе данных
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Создание таблицы, если она не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT 0
)
''')
conn.commit()

ctk.set_appearance_mode("dark")

def add_label(task_id, text_content, completed=False):
    frame = ctk.CTkFrame(main_frame)
    frame.pack(side='top', anchor='nw', pady=5, padx=5, fill='x')

    label = ctk.CTkLabel(frame, text=f"{text_content}", wraplength=500, anchor='w')
    label.pack(side='left', padx=5, pady=5, fill='x')

    checkbox = ctk.CTkCheckBox(frame, text='', command=lambda: toggle_task_completion(task_id))
    checkbox.pack(side='right', padx=10)
    checkbox.select() if completed else checkbox.deselect()

def add_task():
    text_content = add_entry.get("1.0", tk.END).strip()
    if text_content:
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (text_content,))
        conn.commit()
        task_id = cursor.lastrowid
        add_label(task_id, text_content)
        add_entry.delete("1.0", tk.END)  # Очищаем текстовое поле после добавления задачи

def load_tasks():
    for widget in main_frame.winfo_children():
        widget.destroy()

    cursor.execute("SELECT id, task, completed FROM tasks WHERE completed = 0")
    tasks = cursor.fetchall()
    for task in tasks:
        add_label(task[0], task[1], task[2])

def add_task_win():
    add_win = ctk.CTk()
    add_win.geometry("300x400")
    add_win.resizable(False, False)

    frame = ctk.CTkFrame(master=add_win, width=290, height=390)
    frame.place(x=5, y=5)

    global add_entry
    add_entry = ctk.CTkTextbox(master=frame, width=270, height=90, wrap='word')
    add_entry.place(x=10, y=10)

    add_btn = ctk.CTkButton(master=frame, width=100, height=30, text="Add Task", command=add_task)
    add_btn.place(x=95, y=120)

    add_win.mainloop()

def toggle_task_completion(task_id):
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    load_tasks()

# Инициализация основного приложения
app = ctk.CTk()
app.geometry("800x800")
app.title("Kairos | Planner")
app.resizable(False, False)

# Создание боковой панели
sidebar_frame = ctk.CTkFrame(master=app, width=200, height=740, corner_radius=0)
sidebar_frame.grid(row=0, column=0, sticky="nsw", padx=5, pady=5)

# Добавление кнопок в боковую панель
home_button = ctk.CTkButton(master=sidebar_frame, text="Home", command=lambda: print("Home Clicked"))
home_button.pack(pady=10, padx=10)

tasks_button = ctk.CTkButton(master=sidebar_frame, text="Tasks", command=load_tasks)
tasks_button.pack(pady=10, padx=10)

settings_button = ctk.CTkButton(master=sidebar_frame, text="Settings", command=lambda: print("Settings Clicked"))
settings_button.pack(pady=10, padx=10)

# Основной фрейм для задач
main_frame = ctk.CTkFrame(master=app, width=590, height=740)
main_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

# Кнопка для открытия окна добавления задачи
add_task_btn = ctk.CTkButton(master=app, width=30, height=30, text="+", command=add_task_win)
add_task_btn.grid(row=1, column=1, pady=10, padx=10, sticky='se')

add_work_space = ctk.CTkButton(master=app, width=30, height=30, text="add workspace")
add_work_space.grid(row=1, column=0, pady=10, padx=10, sticky='sw')

# Загрузка задач из базы данных при запуске приложения
load_tasks()

# Настройка сетки для автоматического изменения размеров
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

app.mainloop()

# Закрытие соединения с базой данных при завершении работы приложения
conn.close()
