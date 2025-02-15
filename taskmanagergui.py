import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        update_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_tasks()
    else:
        messagebox.showwarning("Warning", "No task selected!")

def complete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks[selected_task_index[0]]["completed"] = True
        update_tasks()
    else:
        messagebox.showwarning("Warning", "No task selected!")

def update_tasks():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        task_listbox.insert(tk.END, f'{task["task"]} [{status}]')

def clear_all_tasks():
    tasks.clear()
    update_tasks()

# Create the main window
root = tk.Tk()
root.title("Task Manager")

# Create and place the widgets
task_label = tk.Label(root, text="Enter a task:")
task_label.pack()

task_entry = tk.Entry(root, width=50)
task_entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

complete_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_button.pack()

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_all_tasks)
clear_button.pack()

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack()

# Start the main loop
root.mainloop()
