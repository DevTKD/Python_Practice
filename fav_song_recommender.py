import random
""""
🎶 Favorite Song Recommender
Ask the user for their mood or genre preference and recommend a song
"""

sad_music = [
    "Fix You by Coldplay",
    "Someone Like You by Adele",
    "Let Her Go by Passenger",
    "The Night We Met by Lord Huron",
    "I Will Always Love You by Whitney Houston",
    "Skinny Love by Bon Iver"
]

happy_music = [
    "Happy by Pharrell Williams",
    "Can’t Stop the Feeling! by Justin Timberlake",
    "Walking on Sunshine by Katrina and The Waves",
    "Uptown Funk by Mark Ronson ft. Bruno Mars",
    "Good as Hell by Lizzo",
    "Dancing Queen by ABBA"
]

mad_music = [
    "Smells Like Teen Spirit by Nirvana",
    "Break Stuff by Limp Bizkit",
    "You Oughta Know by Alanis Morissette",
    "Killing in the Name by Rage Against the Machine"
    "Before I Forget by Slipknot",
    "Irreplaceable by Beyoncé"
]

classical_music = [
    "Adagio for Strings by Samuel Barber",
    "Moonlight Sonata (1st Movement) by Ludwig van Beethoven",
    "Spring by Antonio Vivaldi",
    "Ode to Joy by Beethoven",
    "Dies Irae by Mozart",
    "In the Hall of the Mountain King"
]

soul_music = [
    "A Change Is Gonna Come by Sam Cooke",
    "I'd Rather Go Blind by Etta James",
    "Lovely Day by Bill Withers",
    "Let's Stay Together by Al Green",
    "Respect by Aretha Franklin",
    "Chain of Fools by Aretha Franklin"
]

jazz_music = [
    "Strange Fruit by Billie Holiday",
    "Round Midnight by Thelonious Monk",
    "Take Five by Dave Brubeck"
    "Cheek to Cheek by Elia Fitzgerald & Luis Armstrong",
    "Love Supreme by John Coltrane",
    "Moanin by Charles Mingus"
]

rock_music = [
    "Black by Pearl Jam",
    "Tears in Heaven by Eric Clapton",
    "Dont Stop Me Now by Queen",
    "Sweet Child O' Mine by Guns N' Roses",
    "Welcome to the Jungle by Guns N' Roses"
    "Breakthrough by Foo Fighters"
]


def music_selection(music_choice):
    if music_choice == "happy":
        return random.choice(happy_music)
    elif music_choice == "sad":
        return random.choice(sad_music)
    elif music_choice == "mad":
        return random.choice(mad_music)
    elif music_choice == "classical":
        return random.choice(classical_music)
    elif music_choice == "soul":
        return random.choice(soul_music)
    elif music_choice == "jazz":
        return random.choice(jazz_music)
    elif music_choice == "rock":
        return random.choice(rock_music)
    else:
        return "Invalid selection! Select a choice from the list."

user_music_choice= input("What is your mood (happy, sad or mad) or favorite music genre (Classical, Soul, Jazz, "
                     "or Rock)?: ").lower()
print("Your music recommendation is: ", music_selection(user_music_choice))