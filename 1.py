import tkinter as tk
from tkinter import filedialog, messagebox

# Initialize the main window
root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("1000x500")

# Function to open a file
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    
    if file_path:
        try:
            with open(file_path, "r") as file:
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, file.read())
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file: {e}")

# Function to save the file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(text_area.get(1.0, tk.END))
            messagebox.showinfo("File Saved", "Your file has been saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {e}")

# Function to clear the text area
def clear_text():
    text_area.delete(1.0, tk.END)

# Text area for typing
text_area = tk.Text(root, wrap="word")
text_area.pack(expand=True, fill="both")

# Button frame
button_frame = tk.Frame(root)
button_frame.pack(fill="both")

# Open, Save, and Clear buttons
open_button = tk.Button(button_frame, text="Open", command=open_file)
open_button.pack(side="left", padx=5, pady=5)

save_button = tk.Button(button_frame, text="Save", command=save_file)
save_button.pack(side="left", padx=5, pady=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_text)
clear_button.pack(side="left", padx=5, pady=5)

# Run the application
root.mainloop()
