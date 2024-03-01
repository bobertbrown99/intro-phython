#in your own words describe what python conditional statements are (if/ELSE); more specifically, try to describe how they work.
#answer: basically conditional statements are just a way to guide your code and make your code act on what you want it to do 3

def check_highscore():
    userScore = int(input('what is your current score? '))
    if userScore > 3000:
        print('congrats. You got the high score!')
    else:
        print('sorry. you didnt get the high score try again')

check_highscore(3000)
