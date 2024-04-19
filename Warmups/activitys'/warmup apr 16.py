# Warm up Tuesday April 16th, 2024.

import random

# 1. In your own words, explain the difference between an Python For Loop and a
# Python While Loop.
#ans:the while loop will keep repeating as long as the condition is true while the for loop is used for 
#iterating over a sequence 

# 2. Create a loop that will iterate over a list of numbers. For evey number in your loop,
# it should multiply that number by 3. 
numbers = [1, 2, 3, 4, 5]

for num in numbers[:]:
     num *= 3
     print(num)
# 3. Use the following code snippet below to create a guessing game function. 
# The code below will generate a random number for you. You must write a loop that will
# ask the user to input their guess, if they guess incorrectly, the program will repeat 
# itself and ask the user to guess again. The program should continue to ask them to
# guess until they've gotten it correctly. Once they guess the correct number the program
# will congratulate them and the loop will stop. 

# generates a random number between 1 and 10
randomNumber = random.randint(1, 10)

print('Random number value is: {randomNumber}')


import random

def guessing_game():
    randomNumber = random.randint(1, 10)
    
    while True:
        guess = int(input("Guess the number (between 1 and 10): "))
        
        if guess == randomNumber:
            print("Congratulations! You guessed the correct number:", randomNumber)
            break
        else:
            print("Sorry, that's not the correct number. Try again.")

guessing_game()