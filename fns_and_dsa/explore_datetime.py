from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in YYYY-MM-DD HH:MM:SS format"""
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    """Calculate and display the future date after adding the given number of days"""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print("Future Date:", future_date.strftime("%Y-%m-%d"))

# Part 1: Show current date and time
display_current_datetime()

# Part 2: Prompt user for number of days
try:
    num_days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(num_days)
except ValueError:
    print("Invalid input! Please enter an integer.")
