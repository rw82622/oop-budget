from classes.Budget import Budget

my_budget = Budget(0)
while True:
    
    mode = input("\nWhat would you like to do?\nOptions:\n1. Update monthly income\n2. Add Expense <Description, amount>\n3. Get Expense <Description>\n4. Get monthly cost\n5. Get Category Percentages\n6. Quit\n> ")
    if mode == '6':
        break
    elif mode == '1':
        user_input = input('Enter New Monthly Income: ')
        my_budget.update_monthly_income(user_input)
    elif mode == '2':
        desc = input('Enter Expense name: ')
        amount = input('Enter Expense amount: ')
        my_budget.add_new_expense(desc, amount)
    elif mode == '3':
        user_input = input('Enter expense name: ')
        print(my_budget.get_expense(user_input))
    elif mode == '4':
        print(my_budget.get_monthly_cost())
    elif mode == '5':
        print(my_budget.get_category_percentages())
    else:
        print('Invalid Request. Enter the number that corresponds to the action you would like to take.')

