#imports
from requests import get
from random import choice

#HANGMANPICS FROM https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
HANGMANPICS = ["""
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]
#the next code gets words from the link, splits the list and choses random word
words_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = get(words_site)
words = response.content.decode("utf-8").split()
chosen_word = choice(words)

#this list shows as many underscores as the characters in the chosen_word variable
guessing_lst = []

for i in range(len(chosen_word)):
    guessing_lst.append('_')

wrong_counter = 0
while True:
    print(guessing_lst)
    current_guess = input("Guess a letter: ")
    for index, letter in enumerate(chosen_word):
        if current_guess == letter:
            guessing_lst[index] = current_guess
            if '_' not in guessing_lst:
                print("Congratulations! You guessed the word!")
                restart_game = input("Do you want to play again? (y/n): ")
                if restart_game.lower() == 'y':
                    chosen_word = choice(words)
                    guessing_lst = ['_' for i in range(len(chosen_word))]
                    wrong_counter = 0
                else:
                    break
    if current_guess not in chosen_word:
        print(HANGMANPICS[wrong_counter])
        if wrong_counter > len(HANGMANPICS) - 2:
            print(f"GAME OVER\nWORD: {chosen_word}")

            restart_game = input("Do you want to play again? (y/n)")
            if restart_game.lower() == 'y':
                chosen_word = choice(words)
                guessing_lst = ['_' for _ in range(len(chosen_word))]
                wrong_counter = 0
            else:
                break

        else:
            wrong_counter += 1
    #print(guessing_lst)