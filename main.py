import tkinter as tk
from tkinter import ttk, messagebox
from database import init_db, add_transaction, fetch_transactions
from analysis import generate_financial_report
from visualization import plot_spending_over_time
from datetime import datetime

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Expense Tracker")
        self.root.geometry("700x500")
        self.create_widgets()
        self.refresh_transaction_list()

    def create_widgets(self):
        # Input fields frame
        frame = ttk.Frame(self.root)
        frame.pack(pady=10)

        ttk.Label(frame, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = ttk.Entry(frame)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)
        self.date_entry.insert(0, datetime.now().strftime('%Y-%m-%d'))

        ttk.Label(frame, text="Category:").grid(row=0, column=2, padx=5, pady=5)
        self.category_entry = ttk.Entry(frame)
        self.category_entry.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frame, text="Description:").grid(row=1, column=0, padx=5, pady=5)
        self.description_entry = ttk.Entry(frame, width=40)
        self.description_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        ttk.Label(frame, text="Amount:").grid(row=2, column=0, padx=5, pady=5)
        self.amount_entry = ttk.Entry(frame)
        self.amount_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Type:").grid(row=2, column=2, padx=5, pady=5)
        self.type_combo = ttk.Combobox(frame, values=["expense", "income"], state="readonly")
        self.type_combo.grid(row=2, column=3, padx=5, pady=5)
        self.type_combo.current(0)

        add_btn = ttk.Button(frame, text="Add Transaction", command=self.add_expense)
        add_btn.grid(row=3, column=0, columnspan=4, pady=10)

        # Transactions list frame
        self.tree = ttk.Treeview(self.root, columns=("Date", "Category", "Description", "Amount", "Type"), show='headings')
        for col in ("Date", "Category", "Description", "Amount", "Type"):
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        self.tree.pack(expand=True, fill='both')

        # Buttons for reports and visualization
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)

        report_btn = ttk.Button(btn_frame, text="Show Financial Report", command=self.show_report)
        report_btn.grid(row=0, column=0, padx=5)

        plot_btn = ttk.Button(btn_frame, text="Plot Spending Over Time", command=plot_spending_over_time)
        plot_btn.grid(row=0, column=1, padx=5)

    def add_expense(self):
        date = self.date_entry.get()
        category = self.category_entry.get()
        description = self.description_entry.get()
        amount = self.amount_entry.get()
        ttype = self.type_combo.get()

        if not (date and category and description and amount):
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        try:
            datetime.strptime(date, '%Y-%m-%d')
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Input Error", "Date must be YYYY-MM-DD and amount must be a number.")
            return

        add_transaction(date, category, description, amount, ttype)
        messagebox.showinfo("Success", "Transaction added successfully!")
        self.clear_entries()
        self.refresh_transaction_list()

    def refresh_transaction_list(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        transactions = fetch_transactions()
        for txn in transactions:
            self.tree.insert('', 'end', values=txn[1:])  # Skip id

    def clear_entries(self):
        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, datetime.now().strftime('%Y-%m-%d'))
        self.category_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.type_combo.current(0)

    def show_report(self):
        report = generate_financial_report()
        messagebox.showinfo("Financial Report", report)

if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
