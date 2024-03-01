#in your own owrds describe what phython conditional statements are (if/ELSE); more specifically, try to describe how they work.
#answer: basicallly conditional statements are just a way to guide your code and make your code act on what you want it to do 3

def check_highscore():
    userScore= input('what is your current score?)')
    if userScore > 3000:
     print('congrats. You got the high score!')
    else:
        print('sorry. you didnt get the high score try again')

check_highscore(2000)
