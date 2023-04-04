import pandas as pd

def calculate_profit_loss(filename):
    # Загрузка данных из Excel-файла
    data = pd.read_excel(filename)

    # Вычисление общих доходов и расходов
    total_income = data['Income'].sum()
    total_expenses = data['Expenses'].sum()

    # Вычисление прибыли или убытка
    net_income = total_income - total_expenses
    if net_income > 0:
        print(f"The company made a profit of {net_income}")
    else:
        print(f"The company had a loss of {net_income}")
        
# Пример использования функции
calculate_profit_loss('financial_data.xlsx')
