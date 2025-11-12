import matplotlib.pyplot as plt
import sqlite3
import pandas as pd


def plot_spending_over_time():
    conn = sqlite3.connect('expenses.db')
    df = pd.read_sql_query("SELECT date, SUM(amount) as total FROM transactions WHERE type='expense' GROUP BY date",
                           conn)
    conn.close()

    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df.sort_index(inplace=True)

    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['total'], marker='o')
    plt.title("Spending Over Time")
    plt.xlabel("Date")
    plt.ylabel("Amount Spent")
    plt.grid(True)
    plt.show()

