import os
import time
import random
from termcolor import colored
from keyboardPrint import showKeyboard

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
        word = str.upper(randomWord())
        letters_not_present = ""

        #print(word)

        while True:
            
            print("\033[37m  _____")  
            guess = str.upper(input("\033[37mGuess a word: "))
            
            while len(guess) < 5: #avoid error if guess is too short
                guess += "_"
            
            guess_array.append(guess)

            display_str = ""

            i = 0
            while i <= 4:
                if word[i] == guess[i]:
                    display_str += colored(guess[i], "green") #letter in correct place
                else:
                    if isThere(guess[i], word) == True:
                        display_str += colored(guess[i], "yellow") #letter in word
                    else:
                        display_str += colored(guess[i], "red") #letter nowhere
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
                    print(" YOU LOSE")
                    time.sleep(1)
                    print(f"The word was: {word}")
                    break
                else:
                    if guess == word:
                        print(" YOU WIN")
                        time.sleep(1)
                        break
                    
            if guess == word:
                print(" YOU WIN")
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