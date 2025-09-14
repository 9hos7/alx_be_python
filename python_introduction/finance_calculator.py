#!/usr/bin/env python3

# finance_calculator.py

# Prompt the user for financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

annual_interest_rate = 5

# Project annual savings with 5% interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# Output results
print(f"\nYour monthly savings: ${monthly_savings:.2f}")
print(f"Projected savings after one year with interest: ${int(projected_savings)}")

