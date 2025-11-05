import random

# Pick a word at random
word_list = ["loopy","heart","audio","laugh","trial","flare", "steak", "tooth", "chips", "relay", "plane", ]
hidden_word = random.choice(word_list)

print("WORDLE:")



# Repeat for 6 guesses
for i in range(6):
    # Guess a word
    guess_word = input("Enter a 5-letter guess: ").strip().lower()
    output = ""


    # First letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    



# First letter (in python, counting starts at 0 not 1)
    if guess_word[1] == hidden_word[1]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"



# First letter (in python, counting starts at 0 not 1)
    if guess_word[2] == hidden_word[2]:
        output += "🟩"
    elif guess_word[2] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"



# First letter (in python, counting starts at 0 not 1)
    if guess_word[3] == hidden_word[3]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"



# First letter (in python, counting starts at 0 not 1)
    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"


    # Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win!!! :D")
        break

print(f"You used {i+1} guesses")




















































