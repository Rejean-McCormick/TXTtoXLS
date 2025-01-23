import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def split_text_to_xls():
    # Open a file dialog to select the text file
    file_path = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not file_path:
        return  # If no file is selected, return
    
    # Get the delimiter from the user
    delimiter = delimiter_entry.get()
    if not delimiter:
        messagebox.showerror("Error", "Delimiter cannot be empty.")
        return

    try:
        # Read the content of the text file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Split the content using the delimiter
        split_content = content.split(delimiter)
        
        # Create a DataFrame with the split content
        df = pd.DataFrame([split_content], columns=[f'Column {i+1}' for i in range(len(split_content))])
        
        # Create the Excel file path
        xls_file_path = os.path.splitext(file_path)[0] + ".xlsx"
        
        # Write the DataFrame to an Excel file
        df.to_excel(xls_file_path, index=False, engine='openpyxl')
        messagebox.showinfo("Success", f"Excel file saved at: {xls_file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main GUI window
root = tk.Tk()
root.title("Text to Excel Converter")

# File selection button
file_button = tk.Button(root, text="Select Text File", command=split_text_to_xls, width=20)
file_button.grid(row=0, column=0, pady=10, padx=10)

# Delimiter entry
delimiter_label = tk.Label(root, text="Enter Delimiter:")
delimiter_label.grid(row=1, column=0, sticky="w", padx=10)
delimiter_entry = tk.Entry(root, width=30)
delimiter_entry.grid(row=2, column=0, padx=10)

# Run the application
root.mainloop()
