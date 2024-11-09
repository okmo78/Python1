import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")

# List to store tasks
tasks = []

# Function to add a task
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input required", "Please enter a task.")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        tasks.pop(selected_task_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection required", "Please select a task to delete.")

# Function to update the listbox with the tasks
def update_task_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Entry for new task input
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Add and Delete buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Listbox to display tasks
listbox = tk.Listbox(root, width=30, height=15)
listbox.pack(pady=10)

# Run the application
root.mainloop()
