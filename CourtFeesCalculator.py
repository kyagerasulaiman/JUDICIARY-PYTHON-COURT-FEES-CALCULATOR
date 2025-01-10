import tkinter as tk
from tkinter import ttk
import math

def calculate_court_fees(subject_matter):
    initial_fee = 130000
    increment_fee = 3000
    threshold = 33000000

    if subject_matter <= threshold:
        return initial_fee
    else:
        excess = subject_matter - threshold
        additional_fees = (excess // 3000000) * increment_fee
        total_fees = initial_fee + additional_fees
        return total_fees

def calculate_button_click():
    try:
        subject_matter = float(entry_subject_matter.get())
        fees = calculate_court_fees(subject_matter)
        result_label.config(text=f"The court fees for {subject_matter} subject matter is: {fees}")
    except ValueError:
        result_label.config(text="Please enter a valid numeric value for subject matter.")

def on_button_click(value):
    current = entry_subject_matter.get()
    entry_subject_matter.delete(0, tk.END)
    entry_subject_matter.insert(0, current + str(value))

def clear_entry():
    entry_subject_matter.delete(0, tk.END)

def calculate_expression():
    try:
        expression = entry_subject_matter.get()
        result = eval(expression)
        entry_subject_matter.delete(0, tk.END)
        entry_subject_matter.insert(0, str(result))
    except Exception:
        entry_subject_matter.delete(0, tk.END)
        entry_subject_matter.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Court Fees Calculator")

# Define custom styles for buttons
style = ttk.Style()
style.configure("TButtonRed.TButton", font=("Helvetica", 12), foreground="red")
style.configure("TButtonBlue.TButton", font=("Helvetica", 12), foreground="blue")

# Create and place widgets
label_subject_matter = ttk.Label(root, text="Enter the subject matter value:")
label_subject_matter.grid(row=0, column=0, padx=10, pady=10, columnspan=5)

entry_subject_matter = ttk.Entry(root, font=("Helvetica", 12), width=40)
entry_subject_matter.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="we")

button_frame = ttk.Frame(root)
button_frame.grid(row=2, column=0, columnspan=5, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sin', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('cos', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('tan', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3), ('log', 4, 4),
    ('(', 5, 0), (')', 5, 1), ('C', 5, 2), ('sqrt', 5, 3), ('exp', 5, 4)
]

number_buttons = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

for (text, row, col) in buttons:
    if text == '=':
        button = ttk.Button(button_frame, text=text, command=calculate_expression, style="TButtonBlue.TButton")
    elif text == 'C':
        button = ttk.Button(button_frame, text=text, command=clear_entry, style="TButtonBlue.TButton")
    else:
        style = "TButtonRed.TButton" if text in number_buttons else "TButtonBlue.TButton"
        button = ttk.Button(button_frame, text=text, command=lambda t=text: on_button_click(t), style=style)
    button.grid(row=row, column=col, padx=5, pady=5, ipadx=10, ipady=10)

calculate_button = ttk.Button(root, text="Calculate Court Fees", command=calculate_button_click, style="TButtonBlue.TButton")
calculate_button.grid(row=6, column=0, columnspan=5, pady=10)

result_label = ttk.Label(root, text="", font=("Helvetica", 14))
result_label.grid(row=7, column=0, columnspan=5, pady=10)

# Start the GUI main loop
root.mainloop()
