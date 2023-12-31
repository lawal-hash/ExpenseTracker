from expense import Expense
from expensedb import ExpenseDatabase


def main():
    expense_one = Expense("Spain", 80.00)
    expense_two = Expense("UK", 180.00)
    expense_three = Expense("Malaga", 300.00)

    expense_db = ExpenseDatabase()

    for expense in [expense_one, expense_two, expense_three]:
        expense_db.add_expense(expense)

    expense_by_title = expense_db.get_expense_by_title("Spain")
    print(expense_by_title)


if __name__ == "__main__":
    main()
