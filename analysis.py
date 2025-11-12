import sqlite3
import pandas as pd

DB_NAME = 'expenses.db'

def fetch_transactions():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT date, category, amount, type FROM transactions", conn, parse_dates=['date'])
    conn.close()
    return df

def total_expenses():
    df = fetch_transactions()
    expenses = df[df['type'] == 'expense']
    return expenses['amount'].sum()

def total_income():
    df = fetch_transactions()
    income = df[df['type'] == 'income']
    return income['amount'].sum()

def spending_by_category():
    df = fetch_transactions()
    expenses = df[df['type'] == 'expense']
    summary = expenses.groupby('category')['amount'].sum().sort_values(ascending=False)
    return summary

def monthly_spending():
    df = fetch_transactions()
    expenses = df[df['type'] == 'expense']
    expenses['month'] = expenses['date'].dt.to_period('M')
    monthly_summary = expenses.groupby('month')['amount'].sum()
    return monthly_summary

def generate_financial_report():
    # Generate a basic financial summary report as a string
    income = total_income()
    expenses = total_expenses()
    savings = income - expenses
    by_category = spending_by_category()

    report_lines = [
        "----- Financial Performance Report -----",
        f"Total Income: ₹{income:.2f}",
        f"Total Expenses: ₹{expenses:.2f}",
        f"Savings: ₹{savings:.2f}",
        "\nSpending by Category:"
    ]
    for category, amount in by_category.items():
        report_lines.append(f"  {category}: ₹{amount:.2f}")
    report_lines.append("----------------------------------------")
    return '\n'.join(report_lines)
