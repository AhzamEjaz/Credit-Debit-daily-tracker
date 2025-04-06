import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
import csv
import os
from datetime import datetime

CSV_FILE = "transactions.csv"

# Ensure the CSV file exists with headers
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Amount", "Description", "Date"])

# Save transaction to CSV
def save_transaction():
    t_type = type_var.get()
    amount = amount_var.get()
    description = desc_var.get()
    date = date_var.get()

    if not amount or not date:
        messagebox.showerror("Input Error", "Please enter amount and date.")
        return

    try:
        float(amount)
    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a number.")
        return

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([t_type, amount, description, date])

    messagebox.showinfo("Success", "Transaction saved!")
    clear_fields()

def clear_fields():
    amount_var.set("")
    desc_var.set("")
    #date_var.set("")
    date_var.set(datetime.now().strftime("%Y-%m-%d"))

# View transactions for a selected date and show totals
def view_transactions():
    for row in tree.get_children():
        tree.delete(row)

    selected_date = simpledialog.askstring("Select Date", "Enter date (YYYY-MM-DD):")
    if not selected_date:
        return

    try:
        selected = datetime.strptime(selected_date, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Format Error", "Date must be in YYYY-MM-DD format.")
        return

    total_credit = 0.0
    total_debit = 0.0

    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                row_date = datetime.strptime(row["Date"], "%Y-%m-%d")
                if row_date <= selected:
                    amount = float(row["Amount"])
                    if row["Type"] == "Credit":
                        total_credit += amount
                    elif row["Type"] == "Debit":
                        total_debit += amount

                    if row["Date"] == selected_date:
                        tree.insert("", "end", values=(row["Type"], row["Amount"], row["Description"], row["Date"]))
            except Exception as e:
                print("Skipping row due to error:", e)

    remaining = total_credit - total_debit

    messagebox.showinfo("Totals Until " + selected_date,
                        f"Total Credit: {total_credit:.2f}\n"
                        f"Total Debit: {total_debit:.2f}\n"
                        f"Remaining: {remaining:.2f}")

# Delete selected row from CSV and UI
def delete_selected():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("No selection", "Please select a row to delete.")
        return

    row_values = [str(val) for val in tree.item(selected_item)["values"]]
    deleted = False

    updated_rows = []

    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            if not deleted and [str(cell) for cell in row] == row_values:
                deleted = True  # Skip this row (delete it)
                continue
            updated_rows.append(row)

    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(updated_rows)

    tree.delete(selected_item)
    messagebox.showinfo("Deleted", "Entry deleted successfully.")

# GUI Setup
root = tk.Tk()
root.title("Credit/Debit Tracker")
root.geometry("900x650")
root.option_add("*Font", "Arial 14")

# Input Fields
tk.Label(root, text="Type").grid(row=0, column=0, padx=10, pady=10, sticky='e')
type_var = tk.StringVar(value="Credit")
tk.OptionMenu(root, type_var, "Credit", "Debit").grid(row=0, column=1, padx=10, pady=10, sticky='w')

tk.Label(root, text="Amount").grid(row=1, column=0, padx=10, pady=10, sticky='e')
amount_var = tk.StringVar()
tk.Entry(root, textvariable=amount_var, width=30).grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Description").grid(row=2, column=0, padx=10, pady=10, sticky='e')
desc_var = tk.StringVar()
tk.Entry(root, textvariable=desc_var, width=30).grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Date (YYYY-MM-DD)").grid(row=3, column=0, padx=10, pady=10, sticky='e')
date_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
tk.Entry(root, textvariable=date_var, width=30).grid(row=3, column=1, padx=10, pady=10)

# Buttons
tk.Button(root, text="Save", command=save_transaction, width=15).grid(row=4, column=0, pady=20)
tk.Button(root, text="View by Date", command=view_transactions, width=15).grid(row=4, column=1, pady=20)
tk.Button(root, text="Delete Selected", command=delete_selected, width=15, bg="red", fg="white").grid(row=4, column=2, pady=20)

# Treeview Table
columns = ("Type", "Amount", "Description", "Date")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=200)

tree.grid(row=5, column=0, columnspan=3, padx=10, pady=20)

# Apply font to Treeview
style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 14, "bold"))
style.configure("Treeview", font=("Arial", 13))

root.mainloop()
