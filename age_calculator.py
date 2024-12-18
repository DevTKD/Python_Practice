from datetime import datetime

"""
📅 Age Calculator
Input your birthdate and calculate your age in years, months, and days.
"""
current_date = datetime.now()
birthday_input = input("Enter your birthdate (YYYY-MM-DD): ")
birthday = datetime.strptime(birthday_input, "%Y-%m-%d")

# Calculate age
age = current_date.year - birthday.year
ageInMonths = current_date.month - birthday.month
ageInDays = current_date.day - birthday.day

print(f"Your exact ags is {age} years,  {ageInMonths} month(s), "
      f"and {ageInDays} day(s) old! You look good! 😉.")

print("Thank you for using the age calculator!")
print("Have a great day! 🌞")

