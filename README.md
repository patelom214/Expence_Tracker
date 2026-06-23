<<<<<<< HEAD
# Expense Tracker (Python | OOP Console Application)

A menu-driven, object-oriented Python console application for tracking,
analyzing, and persisting personal expenses. Built as Project 2 of the
DecodeLabs Industrial Training Kit (Batch 2026).

## Features
- Add multiple expenses with category and amount
- View all expenses in a formatted table
- Calculate total expenses (Accumulator Pattern)
- Find the highest and lowest expense
- Calculate the average expense
- Delete an expense by unique ID
- Search expenses by category keyword
- Save expenses to a file (expenses.txt)
- Load previously saved expenses from file
- Clean exit via a sentinel-controlled menu loop

## Tech Stack
- Python 3 (no external dependencies)
- Object-Oriented Programming (single ExpenseTracker class)
- Built-in file I/O for persistence

## How to Run
```bash
# Clone the repository
git clone <your-repo-url>
cd expense-tracker

# Run the application (requires Python 3.x)
python expense_tracker.py
```

## Project Structure
```
expense-tracker/
|-- expense_tracker.py   # Main application source code
|-- expenses.txt         # Auto-generated data file (created on first save)
`-- README.md            # Project documentation
```

## Sample Usage
```
1.  Add Expense
2.  View All Expenses
3.  Calculate Total Expenses
...
11. Exit Program
Enter your choice (1-11): 1
Enter expense category: Food
Enter expense amount: Rs. 250
Expense added successfully! [ID: 1, Food: Rs. 250.00]
```

## Core Concept: The Accumulator Pattern
```python
total = 0
for exp in self.expenses:
    total += exp['amount']   # State(new) = State(old) + Input
```

## Future Enhancements
- Date & time tracking per expense
- Category-wise budgeting and alerts
- Data visualization (matplotlib charts)
- JSON-based storage instead of plain text
- Edit expense option
- Multi-user support with authentication
- GUI / web interface (Tkinter / Flask)
- Database integration (SQLite / PostgreSQL)
- Multi-currency support
- Export reports to PDF / Excel

## Author
Python Developer Intern - DecodeLabs Industrial Training Program, Batch 2026

## License
This project was created for educational purposes as part of the
DecodeLabs Industrial Training Kit.
=======
# Expence_Tracker
>>>>>>> 0dbbfd6102f410ef4c1a358325861e5a56f38297
