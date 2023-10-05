import csv
from datetime import datetime
def csv_to_dicts(file_path):
    list_of_dicts = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            list_of_dicts.append(dict(row))
    return list_of_dicts

class report:
    def __init__(self,data):
        self.data = data

    def total_expenses(self):
        total = 0
        for i in data:
            try:
                amount = float(i['amount'])
                total += amount
            except ValueError:
                pass
        total = round(total,2)
        print("")
        print(f"Total Expense: ${total}")
        print("")

    def expenses_by(self, type, heading, max=float('inf')):
        amount_by = {}
        for i in data:
           data_type = i[type]
           try:
                amount = float(i['amount'])
                if data_type in amount_by:
                    amount_by[data_type].append(amount)
                else:
                    amount_by[data_type] = [amount]
           except ValueError:
                pass

        total_expenses_by = {}
        for key, value in amount_by.items():
            total_sum = sum(value)
            total_sum = round(total_sum,2)
            total_expenses_by[key] = total_sum

        try:
            total_expenses_by['None'] = total_expenses_by.pop('')
        except:
            pass

        try:
            sorted_items = sorted(total_expenses_by.items(), key=lambda x: x[1], reverse=True)
            top = dict(sorted_items[:max])
            print(heading)
            for key, value in top.items():
                print(f"{key}: ${value}")
            print("")
        except:
            print(heading)
            for key, value in total_expenses_by.items():
                print(f"{key}: ${value}")
            print("")
    
    
    def highest_expenses(self):
        day_expenses = {}
        for i in data:
            day = i['expense_date']
            if day != '':
                try:
                    expense = float(i['amount'])
                    if day in day_expenses:
                        day_expenses[day] += expense
                    else:
                        day_expenses[day] = expense
                except ValueError:
                    pass
        max_key = max(day_expenses, key=lambda k: day_expenses[k])
        print(f"Day with Highest Expenses: {max_key} with ${day_expenses[max_key]}")
        print("")

    def month_expense(self):
        expenses_monthly = {}
        for i in data:
            try:
                date = i['expense_date']
                date = datetime.strptime(date, "%Y-%m-%d")
                month = date.month
                amount = float(i['amount'])
                if month in expenses_monthly:
                    expenses_monthly[month].append(amount)
                else:
                    expenses_monthly[month] = [amount]
            except:
                pass
        print("Month-wise Total Expenses:")
        for key, value in expenses_monthly.items():
            x = sum(value)
            x = round(x, 2)
            print(f"{key}: ${x}")
        print("")


    def breakdown_method(delf):
        expenses_type = set()
        for i in data:
            x = i['expense_type']
            expenses_type.add(x)

        breakdown_list = {}
        for x in expenses_type:
            if x == '':
                continue
            else:
                method_list = {}
                for i in data:
                    expense_type = i['expense_type']
                    amount = i['amount']
                    payment_method = i['payment_method']
                    if expense_type != x:
                        continue
                    elif amount == '' or expense_type == '' or payment_method == '':
                        continue
                    else:
                        amount = float(amount)
                        if payment_method in method_list:
                            method_list[payment_method].append(amount)
                        else:
                            method_list[payment_method]=[amount]
                
                sum_method_list = {}
                for key, value in method_list.items():
                    sum_amount = sum(value)
                    sum_amount = round(sum_amount, 2)
                    sum_method_list[key] = sum_amount
                
                breakdown_list[x] = sum_method_list

        print("Expense Type Breakdown by Payment Method:")
        print(f"{'Expense Type':<15}{'Credit Card':>15}{'Cash':>15}{'Total':>15}")
        print("-" * 60)
        total_credit_card = 0
        total_cash = 0
        final_total = 0
        for key, value in breakdown_list.items():
            credit_card = value['Credit Card']
            total_credit_card = round((total_credit_card+credit_card) ,2)
            cash = value['Cash']
            total_cash = round((total_cash+cash), 2)
            total = round((credit_card + cash), 2)
            final_total = round((final_total + total), 2)
            print(f"{key:<15}{credit_card:>15,.2f}{cash:>15,.2f}{total:>15,.2f}")
        print("-" * 60)
        print(f"{'Total':<15}{total_credit_card:>15,.2f}{total_cash:>15,.2f}{final_total:>15,.2f}")
        print("")


file_path = 'expenses.csv'
data = csv_to_dicts(file_path)

task_1 = report(data)
task_1.total_expenses()
task_1.expenses_by(type="expense_type",heading="Total by Expense Type:")
task_1.expenses_by(type="payment_method",heading="Total by Payment Method:")
task_1.expenses_by(type="expense_type",heading="Top 3 Expense Types:",max=3)
task_1.highest_expenses()
task_1.month_expense()
task_1.breakdown_method()

