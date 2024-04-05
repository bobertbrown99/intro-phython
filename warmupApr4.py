#1:in your own words describe what a phython While Loop is 
#ans:a while loop is a type of loop that will repeat a set of instrutions so long as the looping condition is true
#2:What does an iterator do in a phython loop
#ans:The object that produces successive items or values from its associated iterable
#3:how would you fix this code to prevent it from spamming hello?
#ans:you can use a control flow statement such as a for loop or a while loop to iterate over the elements 
#that you want to process, and use a break statement or a return statement to exit the loop when you are finished.

msg = 'hello'

while msg == 'hello':
    print(msg)
    msg = input('type a new message:')
    if msg == goodbye: