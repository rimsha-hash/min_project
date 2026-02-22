import sqlite3
import tkinter as tk
from tkinter import messagebox

# Database Setup
def connect_db():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        completed INTEGER DEFAULT 0
    )
    """)
    conn.commit()
    conn.close()

# Add Task
def add_task():
    task = task_entry.get()
    if task:
        conn = sqlite3.connect("todo.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (task, completed) VALUES (?, 0)", (task,))
        conn.commit()
        conn.close()
        task_entry.delete(0, tk.END)
        show_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Show Tasks
def show_tasks():
    task_list.delete(0, tk.END)
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    for task in tasks:
        status = "✓" if task[2] else "✗"
        task_list.insert(tk.END, f"{task[0]}. {task[1]} [{status}]")

# Mark Task as Completed
def complete_task():
    try:
        selected_task = task_list.get(task_list.curselection())
        task_id = selected_task.split(". ")[0]
        conn = sqlite3.connect("todo.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()
        show_tasks()
    except:
        messagebox.showwarning("Warning", "Please select a task to mark as completed!")

# Delete Task
def delete_task():
    try:
        selected_task = task_list.get(task_list.curselection())
        task_id = selected_task.split(". ")[0]
        conn = sqlite3.connect("todo.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()
        show_tasks()
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Edit Task
def edit_task():
    try:
        selected_task = task_list.get(task_list.curselection())
        task_id, task_text = selected_task.split(". ", 1)
        task_text = task_text.rsplit(" [", 1)[0]

        new_task = task_entry.get()
        if new_task:
            conn = sqlite3.connect("todo.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE tasks SET task = ? WHERE id = ?", (new_task, task_id))
            conn.commit()
            conn.close()
            task_entry.delete(0, tk.END)
            show_tasks()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")
    except:
        messagebox.showwarning("Warning", "Please select a task to edit!")

# UI Setup
connect_db()
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

task_list = tk.Listbox(root, width=50, height=10)
task_list.pack(pady=10)

show_tasks()

complete_button = tk.Button(root, text="Mark as Completed", command=complete_task)
complete_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

edit_button = tk.Button(root, text="Edit Task", command=edit_task)
edit_button.pack()

root.mainloop()
