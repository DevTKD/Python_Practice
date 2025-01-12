import re
"""
🔄Palindrome Checker:
 Check if a given string is a palindrome (reads the same backward and forward).
"""
while True:
    user_input = input("Enter a word or phrase (or type 'exit' to quit): ").lower()

    if user_input == "exit":
        break

    # Remove all non-alphanumeric characters
    cleaned_input = re.sub(r'[^a-z0-9]', '', user_input)

    # Check if the cleaned input is a palindrome
    if cleaned_input == cleaned_input[::-1]:
        print("This is a palindrome!")
    else:
        print("This is not a palindrome")
