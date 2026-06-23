"""
==================================================================
 PROJECT 2: EXPENSE TRACKER
 Industrial Training Kit - DecodeLabs (Batch 2026)
==================================================================
 Author      : Python Developer Intern
 Description : A menu-driven, object-oriented console application
               that allows users to add, view, search, delete,
               analyze, save and load expenses. Built using the
               Accumulator Pattern (total = total + new_expense)
               and defensive coding (try-except) as per the
               DecodeLabs Project 2 brief.
==================================================================
"""

import os


class ExpenseTracker:
    """
    ExpenseTracker encapsulates all data (the expense list) and all
    behavior (add, view, delete, search, save, load, analyze) related
    to tracking expenses.

    Each expense is stored as a dictionary:
        {"id": int, "category": str, "amount": float}
    This makes it easy to identify, search, and delete a specific
    expense later, while still allowing simple accumulation logic.
    """

    # File used for persistent storage (Phase 3: Output / Persistence)
    FILE_NAME = "expenses.txt"

    def __init__(self):
        """
        Constructor - runs once when an ExpenseTracker object is created.

        self.expenses : list  -> stores every expense dictionary (STATE)
        self.next_id  : int   -> auto-incrementing unique ID generator

        NOTE: These are initialized OUTSIDE any loop, exactly once.
        This is the 'Initialization (Memory)' principle from the
        training deck - state must persist across iterations, not
        reset every cycle (the 'Iteration Amnesia' trap).
        """
        self.expenses = []
        self.next_id = 1

    # ----------------------------------------------------------------
    # 1. ADD EXPENSE
    # ----------------------------------------------------------------
    def add_expense(self):
        """
        Prompts the user for a category and an amount, validates the
        amount using try-except (defensive coding / Poka-Yoke), and
        appends a new expense record to self.expenses.
        """
        category = input("Enter expense category (e.g., Food, Travel): ").strip()
        if category == "":
            category = "General"

        try:
            # int('100') + int('50') = 150 (Truth) -> we use float() here
            # so users can enter paise/cents too, e.g. 49.99
            amount = float(input("Enter expense amount: Rs. "))

            if amount <= 0:
                print("⚠ Amount must be a positive number. Expense not added.\n")
                return

            expense = {
                "id": self.next_id,
                "category": category,
                "amount": amount
            }
            self.expenses.append(expense)
            self.next_id += 1

            print(f"✅ Expense added successfully! [ID: {expense['id']}, "
                  f"{category}: Rs. {amount:.2f}]\n")

        except ValueError:
            # Triggered if user types "ten" instead of 10
            print("❌ Invalid input! Please enter numeric values only (e.g., 100, 49.99).\n")

    # ----------------------------------------------------------------
    # 2. VIEW ALL EXPENSES
    # ----------------------------------------------------------------
    def view_expenses(self):
        """Displays every expense currently stored, in a tabular format."""
        if not self.expenses:
            print("📭 No expenses recorded yet.\n")
            return

        print("\n" + "-" * 50)
        print(f"{'ID':<5}{'Category':<20}{'Amount (Rs.)':>15}")
        print("-" * 50)
        for exp in self.expenses:
            print(f"{exp['id']:<5}{exp['category']:<20}{exp['amount']:>15.2f}")
        print("-" * 50 + "\n")

    # ----------------------------------------------------------------
    # 3. CALCULATE TOTAL EXPENSES (Accumulator Pattern)
    # ----------------------------------------------------------------
    def calculate_total(self):
        """
        Core accumulator logic as required by the project brief:
            total = total + new_expense
        Returns the float total and also prints it.
        """
        total = 0  # Accumulator initialized to zero BEFORE the loop
        for exp in self.expenses:
            total += exp["amount"]  # total = total + new_expense

        print(f"💰 Total Spent: Rs. {total:.2f}\n")
        return total

    # ----------------------------------------------------------------
    # 4. FIND HIGHEST EXPENSE
    # ----------------------------------------------------------------
    def find_highest(self):
        """Finds and displays the single largest expense recorded."""
        if not self.expenses:
            print("📭 No expenses recorded yet.\n")
            return

        highest = self.expenses[0]
        for exp in self.expenses:
            if exp["amount"] > highest["amount"]:
                highest = exp

        print(f"🔺 Highest Expense -> ID {highest['id']}, "
              f"{highest['category']}: Rs. {highest['amount']:.2f}\n")

    # ----------------------------------------------------------------
    # 5. FIND LOWEST EXPENSE
    # ----------------------------------------------------------------
    def find_lowest(self):
        """Finds and displays the single smallest expense recorded."""
        if not self.expenses:
            print("📭 No expenses recorded yet.\n")
            return

        lowest = self.expenses[0]
        for exp in self.expenses:
            if exp["amount"] < lowest["amount"]:
                lowest = exp

        print(f"🔻 Lowest Expense -> ID {lowest['id']}, "
              f"{lowest['category']}: Rs. {lowest['amount']:.2f}\n")

    # ----------------------------------------------------------------
    # 6. CALCULATE AVERAGE EXPENSE
    # ----------------------------------------------------------------
    def calculate_average(self):
        """Calculates the mean of all recorded expenses."""
        if not self.expenses:
            print("📭 No expenses recorded yet.\n")
            return

        total = sum(exp["amount"] for exp in self.expenses)
        average = total / len(self.expenses)
        print(f"📊 Average Expense: Rs. {average:.2f} "
              f"(across {len(self.expenses)} entries)\n")

    # ----------------------------------------------------------------
    # 7. DELETE EXPENSE
    # ----------------------------------------------------------------
    def delete_expense(self):
        """
        Deletes an expense by its unique ID.
        Uses try-except to guard against non-integer input.
        """
        if not self.expenses:
            print("📭 No expenses recorded yet.\n")
            return

        self.view_expenses()
        try:
            target_id = int(input("Enter the ID of the expense to delete: "))
        except ValueError:
            print("❌ Invalid ID. Please enter a whole number.\n")
            return

        for exp in self.expenses:
            if exp["id"] == target_id:
                self.expenses.remove(exp)
                print(f"🗑 Expense ID {target_id} deleted successfully.\n")
                return

        print(f"❌ No expense found with ID {target_id}.\n")

    # ----------------------------------------------------------------
    # 8. SEARCH EXPENSE
    # ----------------------------------------------------------------
    def search_expense(self):
        """
        Searches expenses by category keyword (case-insensitive,
        partial match supported).
        """
        if not self.expenses:
            print("📭 No expenses recorded yet.\n")
            return

        keyword = input("Enter category keyword to search: ").strip().lower()
        results = [exp for exp in self.expenses if keyword in exp["category"].lower()]

        if not results:
            print(f"🔍 No expenses found matching '{keyword}'.\n")
            return

        print(f"\n🔍 Found {len(results)} matching expense(s):")
        print("-" * 50)
        print(f"{'ID':<5}{'Category':<20}{'Amount (Rs.)':>15}")
        print("-" * 50)
        for exp in results:
            print(f"{exp['id']:<5}{exp['category']:<20}{exp['amount']:>15.2f}")
        print("-" * 50 + "\n")

    # ----------------------------------------------------------------
    # 9. SAVE EXPENSES TO FILE
    # ----------------------------------------------------------------
    def save_to_file(self):
        """
        Persists all current expenses to expenses.txt so data is not
        lost when the program exits (Phase 3: Output / Persistence).
        Each line format: id,category,amount
        """
        try:
            with open(self.FILE_NAME, "w") as file:
                for exp in self.expenses:
                    file.write(f"{exp['id']},{exp['category']},{exp['amount']}\n")
            print(f"💾 {len(self.expenses)} expense(s) saved to '{self.FILE_NAME}' successfully.\n")
        except IOError as e:
            print(f"❌ Error saving file: {e}\n")

    # ----------------------------------------------------------------
    # 10. LOAD EXPENSES FROM FILE
    # ----------------------------------------------------------------
    def load_from_file(self):
        """
        Loads previously saved expenses from expenses.txt back into
        memory. Replaces the current in-memory list and rebuilds the
        next_id counter so new entries don't clash with loaded ones.
        """
        if not os.path.exists(self.FILE_NAME):
            print(f"❌ No saved file found ('{self.FILE_NAME}' does not exist yet).\n")
            return

        try:
            loaded_expenses = []
            with open(self.FILE_NAME, "r") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(",")
                    if len(parts) != 3:
                        continue  # skip malformed/corrupt lines (defensive coding)
                    exp_id, category, amount = parts
                    loaded_expenses.append({
                        "id": int(exp_id),
                        "category": category,
                        "amount": float(amount)
                    })

            self.expenses = loaded_expenses
            self.next_id = (max((exp["id"] for exp in self.expenses), default=0) + 1)
            print(f"📂 {len(self.expenses)} expense(s) loaded from '{self.FILE_NAME}' successfully.\n")

        except (IOError, ValueError) as e:
            print(f"❌ Error loading file: {e}\n")

    # ----------------------------------------------------------------
    # MENU DISPLAY
    # ----------------------------------------------------------------
    @staticmethod
    def display_menu():
        """Prints the main menu options to the console."""
        print("=" * 50)
        print("        💼  EXPENSE TRACKER - DecodeLabs  💼")
        print("=" * 50)
        print("1.  Add Expense")
        print("2.  View All Expenses")
        print("3.  Calculate Total Expenses")
        print("4.  Find Highest Expense")
        print("5.  Find Lowest Expense")
        print("6.  Calculate Average Expense")
        print("7.  Delete Expense")
        print("8.  Search Expense")
        print("9.  Save Expenses to File")
        print("10. Load Expenses from File")
        print("11. Exit Program")
        print("=" * 50)

    # ----------------------------------------------------------------
    # 11. EXIT / MAIN LOOP CONTROLLER (Kill Switch / Sentinel Pattern)
    # ----------------------------------------------------------------
    def run(self):
        """
        Main driver loop of the program. Implements the 'while True'
        Logic Skeleton with a sentinel value (choice 11 / 'exit') to
        gracefully break out of the continuous audit loop.
        """
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-11): ").strip()

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.calculate_total()
            elif choice == "4":
                self.find_highest()
            elif choice == "5":
                self.find_lowest()
            elif choice == "6":
                self.calculate_average()
            elif choice == "7":
                self.delete_expense()
            elif choice == "8":
                self.search_expense()
            elif choice == "9":
                self.save_to_file()
            elif choice == "10":
                self.load_from_file()
            elif choice == "11":
                print("👋 Thank you for using DecodeLabs Expense Tracker. Goodbye!")
                break  # Sentinel value reached -> graceful shutdown
            else:
                print("❌ Invalid choice! Please select a number between 1 and 11.\n")


# ======================================================================
# ENTRY POINT
# ======================================================================
if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
