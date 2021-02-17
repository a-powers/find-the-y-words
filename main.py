import random
from replit import clear
from words import word_list

print("Most common words in the US dictionary.  Pick a letter and guess what the word is.")

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
guessed_all = False

#Create blanks
char_spaces = []
for _ in chosen_word:
    char_spaces += "_"


while not guessed_all:
    
    guess = input("Guess a letter.").lower()
    clear()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            char_spaces[position] = letter

    print(''.join(char_spaces))
    
    

    if char_spaces[position] != "_":
        guessed_all = True
        print("You did it, you win!")
    