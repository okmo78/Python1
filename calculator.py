import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")

# Function to perform calculations
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            result = num1 / num2
        else:
            result = "Select an operation"
        
        result_label.config(text=f"Result: {result}")
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Entry fields for numbers
entry_num1 = tk.Entry(root, width=10)
entry_num1.pack(pady=5)

entry_num2 = tk.Entry(root, width=10)
entry_num2.pack(pady=5)

# Dropdown menu for operations
operation_var = tk.StringVar()
operation_var.set("Add")
operations_menu = tk.OptionMenu(root, operation_var, "Add", "Subtract", "Multiply", "Divide")
operations_menu.pack(pady=5)

# Calculate button
calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=20)

# Run the application
root.mainloop()
