"""
📚Simple Word Counter
Enter a sentence, and the program counts the number of words and characters.
"""
user_input = input("Enter a word or phase: ")

word_count = len(user_input.split())
character_count = len(user_input)

print(f"Your word count is: {word_count}")
print(f"Your character count is: {character_count}")