
class Budget:
    def __init__(self, monthly_income):
        self.monthly_income = monthly_income
        self.expenses = {}
        self.monthly_costs = 0
        self.percent_per_category = {}
        
    def add_new_expense(self, description, amount):
        try:
            amount = float(amount.replace('$',''))
            description = description.lower()
            self.expenses.update({description : self.expenses[description] + amount}) if self.expenses.get(description) else self.expenses.update({description:amount})
            print(f'Expense added successfully')
        except:
            print('Invalid input for amount.')
            
    def update_monthly_income(self, num):
        try:
            num = float(num.replace('$',''))
            self.monthly_income = num
            print(f'Monthly income successfully updated to ${num}')
        except:
            print('Invalid input for income.')
            
    def get_monthly_cost(self):
        for key in self.expenses:
            self.monthly_costs += self.expenses[key]
        return self.monthly_costs
        
    def get_expense(self, description):
        description = description.lower()
        if self.expenses.get(description):
            return self.expenses[description]
        else:
            print("Sorry! Can't find that expense.")
                
    def get_category_percentages(self):
        for key in self.expenses:
            percentage = (self.expenses[key] / self.monthly_income) * 100
            percentage = round(percentage, 3)
            self.percent_per_category.update({key : percentage})
        return self.percent_per_category
                