import tkinter as tk
from tkinter import ttk


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


# Create the main window
root = tk.Tk()
root.title("Court Fees Calculator")

# Create and place widgets
label_subject_matter = ttk.Label(root, text="Enter the subject matter value:")
label_subject_matter.grid(row=0, column=0, padx=10, pady=10)

entry_subject_matter = ttk.Entry(root)
entry_subject_matter.grid(row=0, column=1, padx=10, pady=10)

calculate_button = ttk.Button(root, text="Calculate", command=calculate_button_click)
calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Start the GUI main loop
root.mainloop()
