import csv
import os

FILENAME = "expenses.csv"

def add_expense():
    """Take user input and add a new expense to the CSV file."""
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, etc.): ")
    description = input("Enter description: ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return
    
    file_exists = os.path.isfile(FILENAME)
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Category", "Description", "Amount"])
        writer.writerow([date, category, description, amount])
    print("✅ Expense added successfully!\n")

def view_expenses():
    """Read and display all saved expenses."""
    if not os.path.isfile(FILENAME):
        print("No expenses recorded yet!\n")
        return
    
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        expenses = list(reader)
    
    if len(expenses) <= 1:
        print("No expenses recorded yet!\n")
        return
    
    print("\n📋 Your Expenses:")
    for row in expenses:
        print("\t".join(row))
    print()

def total_expenses():
    """Calculate and display total amount spent."""
    if not os.path.isfile(FILENAME):
        print("No expenses recorded yet!\n")
        return
    
    total = 0
    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row["Amount"])
    
    print(f"💰 Total Amount Spent: {total:.2f}\n")

def main():
    """Main menu loop for the expense tracker."""
    while True:
        print("=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()