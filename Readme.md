# 💰 Personal Expense Tracker

A simple yet powerful **desktop-based application** built using **Python** that helps users efficiently manage their daily income and expenses.  
It provides a clean interface to record transactions, analyze spending habits, and generate financial reports with visual insights.

---

## Overview
The **Personal Expense Tracker** is designed to simplify financial management for individuals.  
Users can record daily transactions, categorize expenses, and view total income, total expenses, and savings at a glance.  

The system automatically generates **financial reports** and provides **visualizations** of monthly spending and category-wise expenses.

---

## Features

**Add and View Transactions**  
Easily record daily income or expenses with category, description, and date.

**Automatic Financial Report Generation**  
Displays total income, total expenses, savings, and category-wise spending.

**Spending Visualization**  
Graphs and charts show trends over time for better financial understanding.

**User-Friendly Interface**  
Built using Tkinter with a modern, clean layout.

**Local Database Storage**  
Uses SQLite for secure and lightweight data management.

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Programming Language** | Python 3 |
| **Frontend (UI)** | Tkinter |
| **Database** | SQLite |
| **Data Analysis** | Pandas |
| **Data Visualization** | Matplotlib |
| **IDE Used** | VS Code / PyCharm |

---

## 📂 Project Structure  
ExpenseTracker/  
│  
├── database.py # Handles database creation and transaction storage  
├── analysis.py # Contains financial analysis functions  
├── visualization.py # Generates spending charts and plots  
├── main.py # Main Tkinter GUI application  
│
├── expenses.db # SQLite database (auto-created)  
├── requirements.txt # List of dependencies   
└── README.md # Project documentation  
