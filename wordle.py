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
from termcolor import colored

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

def showKeyboard(not_present):

    line_1 = "qwertyuiop"
    line_2 = "asdfghjkl"
    line_3 = "zxcvbnm"

    letter_color = "white"
    present_format = "on_green"
    not_present_format = "on_red"

    for i in line_1:
        if i in not_present:
            text = colored(i, letter_color, not_present_format)
            print(text, end = "")
        else:
            text2 = colored(i,letter_color, present_format)
            print(text2, end = "")

    print("")

    for i in line_2:
        if i in not_present:
            text = colored(i, letter_color, not_present_format)
            print(text, end = "")
        else:
            text2 = colored(i,letter_color, present_format)
            print(text2, end = "")

    print("")
    print(" ", end = "")

    for i in line_3:
        if i in not_present:
            text = colored(i, letter_color, not_present_format)
            print(text, end = "")
        else:
            text2 = colored(i,letter_color, present_format)
            print(text2, end = "")
    print("")

try:
    while True:
        guess_array = []
        print_array = []
        word = randomWord()
        letters_not_present = ""

        #print(word)

        while True:
            
            print("\033[37m  _____")  
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
                        letters_not_present += guess[i] #add to letters not present string
                i += 1
            
            print_array.append(display_str)

            clear()

            for i in print_array: #print out the wordle display
                print("  ", end = "")
                print(i)

            showKeyboard(letters_not_present)
            
            if len(print_array) >= 6:
                if guess != word:
                    print(f"\033[37m YOU LOSE")
                    time.sleep(1)
                    print(f"The word was: {word}")
                    break
                else:
                    if guess == word:
                        print(f"\033[37m YOU WIN")
                        time.sleep(1)
                        break
                    
            if guess == word:
                print(f"\033[37mYOU WIN")
                time.sleep(1)
                break

        if input("enter y to play again, or any other character to exit: ") == "y":
            clear()
            continue
        else:
            clear()
            print("goodbye")
            time.sleep(1)
            clear()
            exit()
            
except KeyboardInterrupt:
    clear()
    exit()