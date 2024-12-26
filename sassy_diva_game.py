import random
"""
💋Sassy Diva Game: 
Ask any yes or no question and see what answer the Sassy Diva has for you!
"""

response_options = {
  1: "Yes, but dont mess it up!",
	2: "Nope. Try again in your next life.",
	3: 'Maybe… if you are lucky.',
	4: "Yes, queen! Go for it!",
	5: "Absolutely not. Who raised you?",
	6: "Sure… if you enjoy chaos.",
	7: "No way, sugar. Move on.",
	8: "Yes, but only because I’m feeling generous.",
	9: "Don’t count on it, darling",
	10: "Yes, but it’ll cost you.",
	11: "Ask me again, and I might block you.",
	12: "Nope. Not happening in this universe.",
	13: "Yes, but keep it classy, please.",
	14: "Oh, honey, you already know the answer.",
	15: "Yes, but brace yourself for the drama.",
	16: "Not today, not tomorrow, not ever.",
	17: "Of course, but you owe me one.",
	18: "Nope. Better luck next time, champ.",
	19: "Yes, but don’t make me regret it.",
	20: "It’s a yes, but only because I like you."
}

user_question = input("Enter a yes or no question: ")
random_response = random.randint(1, 20)
print(response_options[random_response])