import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (current_date)
print(f"Current date and time: {display_current_datetime()}")

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    future_date = datetime.datetime.now() + timedelta(days = number_of_days)
    return (future_date.strftime("%Y-%m-%d"))
print(f"Future date: {calculate_future_date()}")