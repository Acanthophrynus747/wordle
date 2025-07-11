'''
ANSI COLORS
[0;30m 	Black
[0;31m 	Red
[0;32m 	Green
[0;33m 	Yellow
[0;34m 	Blue
[0;35m 	Purple
[0;36m 	Cyan
[0;37m 	White
'''
import os
import time
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') #clear either the linux or windows way or linux way

def randomWord():
    with open("shuffled_real_wordles.txt") as f:
        lines = f.readlines()
        word = random.choice(lines).strip()
        return word

def isThere(char, word):
    for i in word:
        if char == i:
            return True
    return False

try:
    while True:
        guess_array = []
        print_array = []
        word = randomWord()

        while True:
            
            print("\033[37m_____")  
            guess = input("\033[37mGuess a word: ")
            
            while len(guess) < 5: #avoid error if guess is too short
                guess += "_"
            
            guess_array.append(guess)

            display_str = ""

            i = 0
            while i <= 4:
                if word[i] == guess[i]:
                    display_str += f"\033[32m{guess[i]}" #letter in correct place
                else:
                    if isThere(guess[i], word) == True:
                        display_str += f"\033[33m{guess[i]}" #letter in word
                    else:
                        display_str += f"\033[31m{guess[i]}" #letter nowhere
                i += 1
            
            print_array.append(display_str)

            clear()

            for i in print_array:
                print(i)
            
            if len(print_array) >= 6:
                print(f"\033[37mYOU LOSE")
                time.sleep(1)
                print(f"The word was: {word}")
                break

            if guess == word:
                print(f"\033[37mYOU WIN")
                time.sleep(1)
                break
        
        input = input("enter any character to exit: ")
        time.sleep(1)
        clear()
        exit()
            
except KeyboardInterrupt:
    clear()
    exit()