import tkinter as tk
from tkinter import filedialog, messagebox
from modules.data_generator import generate_fake_data
from modules.cleaner import clean_data
from modules.reporter import generate_report

def run_cleaner():
    file_path = filedialog.askopenfilename(title="Select file", filetypes=[("Excel files", "*.xlsx")])
    if not file_path:
        return
    df, cleaned_file = clean_data(file_path)
    generate_report(df, cleaned_file)
    messagebox.showinfo("Done", f"File cleaned!\nSaved as: {cleaned_file}\nReport generated.")

def run_generator():
    filename = filedialog.asksaveasfilename(defaultextension=".xlsx", title="Save fake data as")
    if filename:
        generate_fake_data(20, filename)

root = tk.Tk()
root.title("Secure Data Cleaner")
root.geometry("400x200")

tk.Button(root, text="Generate Fake Data", command=run_generator, width=30).pack(pady=20)
tk.Button(root, text="Clean Data File", command=run_cleaner, width=30).pack(pady=20)

root.mainloop()
