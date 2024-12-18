"""
🧮 Simple Calculator
A program to perform basic arithmetic operations (add, subtract, multiply, divide).
"""
def calculator():
    try:
        add = user_input_one + user_input_two
        sub = user_input_one - user_input_two
        multipy = user_input_one * user_input_two
        divide = user_input_one / user_input_two if user_input_two != 0 else "Error: Division by zero"

        if selected_math_operation == "+":
            print(add)
        elif selected_math_operation == "-":
            print(sub)
        elif selected_math_operation == "*":
            print(multipy)
        elif selected_math_operation == "/":
            print(divide)
        else:
            print("Incorrect Entry!")
    except Exception as e:
        print(f"An error occurred: {e}")

while True:
    try:
        user_input_one = int(input("Enter your first number: "))
        selected_math_operation = input("Enter either +, -, *, or /: ")
        user_input_two = int(input("Enter your second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue

    calculator()

    continue_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
    if continue_calculation != 'yes':
        print("Thanks for using the calculator! Goodbye!")
        break