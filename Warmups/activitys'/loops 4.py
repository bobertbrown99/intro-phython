#a while loop is a type of loop that will repeat a set of instrutions so long as the looping condition is true
#For Loop is a type of loop that is used for iterating over a sequence

# forloop can be used for grades or something for example:Imagine you have a list of student scores and you want to calculate the average score. You would iterate over each score using 
#a for loop to sum them up and then divide by the total number of scores to find the average

#a while loop: Consider a game where the player has to guess a secret number you would prompt the player 
# to enter their guess check if it matches the secret number and continue looping until the correct guess is made.

for i in range(1, 21):
    if i % 2 == 0:
        print("Your number", i, "is even")