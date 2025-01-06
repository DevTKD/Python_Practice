from datetime import datetime

"""
⏳Days Until Your Birthday
Input your birthdate and calculate how many days are left until your next birthday.
"""

current_date = datetime.now()
birthday_input = input("Enter your birthdate (MM-DD): ")
birthday = datetime.strptime(birthday_input, "%m-%d").replace(year=current_date.year)

if birthday < current_date:
    birthday = birthday.replace(year=current_date.year + 1)

days_until_birthday = (birthday - current_date).days

print(f"You have {days_until_birthday} day(s) until your birthday!")
print("Feel free to start celebrating early! 🎊🎉")

