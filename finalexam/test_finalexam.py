import pytest
from finalexam import BudgetPlanner

class TestBudgetPlanner: 

    def setup_method(self):
        """Initialize a fresh BudgetPlanner instance before each test."""
        self.planner = BudgetPlanner("April")

    def test_initialization(self):
        """Test if the planner starts with zero income and no expenses."""
        assert self.planner.month == "April"
        assert self.planner.total_income == 0.0
        assert len(self.planner.expenses) == 0

    def test_add_income(self):
        """Test adding multiple sources of income."""
        self.planner.add_income(1000.00, "Salary")
        self.planner.add_income(500.00, "Freelance")
        assert self.planner.total_income == 1500.00

    def test_add_expense_new_category(self):
        """Test adding an expense to a brand new category."""
        self.planner.add_expense("Rent", 500.00)
        assert "Rent" in self.planner.expenses
        assert self.planner.expenses["Rent"] == 500.00

    def test_add_expense_existing_category(self):
        """Test that expenses in the same category are summed correctly."""
        self.planner.add_expense("Food", 50.00)
        self.planner.add_expense("Food", 25.00)
        assert self.planner.expenses["Food"] == 75.00

    def test_calculate_total_expenses(self):
        """Test the sum logic of all combined expenses."""
        self.planner.add_expense("Rent", 300.00)
        self.planner.add_expense("Utilities", 100.00)
        assert self.planner.calculate_total_expenses() == 400.00

    def test_balance_logic(self):
        """Test the calculation of the remaining balance."""
        self.planner.add_income(1000.00)
        self.planner.add_expense("Rent", 600.00)
        
        total_expenses = self.planner.calculate_total_expenses()
        balance = self.planner.total_income - total_expenses
        assert balance == 400.00

    def test_over_budget_scenario(self):
        """Test logic when expenses exceed income."""
        self.planner.add_income(100.00)
        self.planner.add_expense("Luxury", 150.00)
        
        total_expenses = self.planner.calculate_total_expenses()
        balance = self.planner.total_income - total_expenses
        assert balance == -50.00
