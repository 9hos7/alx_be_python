monthly_income = float(input("Enter your monthly income: "))
monthly_expense = float(input("Enter your monthly expense: "))

monthly_savings = float(monthly_income - monthly_expense)

annual_interest = 5

annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f'Your monthly savings are ${monthly_savings}')

print(f'Projected savings after one year, with interest, is ${int(annual_savings)}.')