import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, description):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.expenses.append({"amount": amount, "description": description, "date": date})
        print("Expense added successfully.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses to show.")
            return
        for idx, expense in enumerate(self.expenses, 1):
            print(f"{idx}. {expense['date']} - {expense['description']}: ${expense['amount']}")

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            removed = self.expenses.pop(index)
            print(f"Removed expense: {removed['description']} - ${removed['amount']}")
        else:
            print("Invalid index. Please try again.")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            tracker.add_expense(amount, description)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            index = int(input("Enter the index of the expense to delete: ")) - 1
            tracker.delete_expense(index)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
