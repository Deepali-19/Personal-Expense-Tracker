import tkinter as tk
from tkinter import ttk, messagebox
from database import add_transaction, fetch_transactions

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.create_widgets()

    def create_widgets(self):
        # Entry for date, category, description, amount, type
        # Button to add transaction
        # Treeview or listbox to show transactions
        # Button to visualize or generate report
        pass

    def add_expense(self):
        # Collect inputs, validate, add to DB
        # Refresh transaction list display
        pass

    def show_transactions(self):
        # Fetch from DB and display
        pass
