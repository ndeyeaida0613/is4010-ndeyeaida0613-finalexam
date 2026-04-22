class BudgetPlanner:
    def __init__(self, month):
        self.month = month
        self.total_income = 0.0
        self.expenses = {}

    def add_income(self, amount, source="Main Paycheck"):
        """Adds income to the budget."""
        self.total_income += amount
        print(f"Added Income: ${amount:.2f} from {source}")

    def add_expense(self, category, amount):
        """Adds an expense under a specific category."""
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount
        print(f"Added Expense: ${amount:.2f} for {category}")

    def calculate_total_expenses(self):
        """Calculates the sum of all expenses."""
        return sum(self.expenses.values())

    def generate_report(self):
        """Prints a detailed budget summary."""
        total_expenses = self.calculate_total_expenses()
        balance = self.total_income - total_expenses

        print("\n" + "="*30)
        print(f" BUDGET REPORT: {self.month.upper()}")
        print("="*30)
        print(f"Total Income:   ${self.total_income:.2f}")
        print("-" * 30)
        
        print("Expenses:")
        for category, amount in self.expenses.items():
            # Calculate what percentage of your income this expense is
            percentage = (amount / self.total_income * 100) if self.total_income > 0 else 0
            print(f"  - {category}: ${amount:.2f} ({percentage:.1f}%)")
            
        print("-" * 30)
        print(f"Total Expenses: ${total_expenses:.2f}")
        print("="*30)
        
        if balance > 0:
            print(f"Remaining Balance: +${balance:.2f} (Great job! Put this in savings.)")
        elif balance == 0:
            print(f"Remaining Balance: $0.00 (Perfect Zero-Based Budget.)")
        else:
            print(f"Remaining Balance: -${abs(balance):.2f} (Warning: You are over budget!)")
        print("="*30 + "\n")

# --- How to use the code ---
if __name__ == "__main__":
    # 1. Create a new budget for the month
    my_budget = BudgetPlanner("April")

    # 2. Add your income
    my_budget.add_income(2000.00, "Monthly Salary")
    # 3. Add your expenses
    my_budget.add_expense("Rent", 300.00)
    my_budget.add_expense("Groceries",150.00)
    my_budget.add_expense("Utilities", 180.00)
    my_budget.add_expense("Car Insurence & Gas" , 200.00)
    my_budget.add_expense("Entertainment", 150.00)
    my_budget.add_expense("Student Loans", 300.00)
    
    # 4. Print the final report
    my_budget.generate_report()
