# Midterm quiz. 
# Create a new python document called midtermquiz.py
# Complete the following questions.
# Once you have comepleted your quiz, commit and sync your work to your GitHub. 

#RULES
# This quiz is open book; you may use your notes, google (only if you are viewing arcticles about python), W3schools only. Any other website
# is prohibitied.
# No phones are allowed during the quiz. refusal to put away a phone will result in failure.
# There is no talking during the quiz. If you complete the quiz, notify the instructor that you
# have finished. Once that is done, you are free to use your device and browse the web quitely. 

# Good Luck

# 1. In your own words, describe what the difference
# between a function arguement and a function parameter. ans: a function parameter is the variable 
#that is used in the function and the function arguement is the value that is passed to the function

# 2. In your own words, describe what each of the following errors means.
# Write your response using complete sentences.

# syntax error ans:A syntax error means the computer cant understand the code you wrote
# type error ans: a type error is like when you use a data that doesn't work with the function
# name error ans: a name error is when you use a varible that doesn't exist

# 3. What function would I use if I wanted to convert an integer data type into 
# a string data type? ans: you would use str() to convert the integer to a string

# 4. What function would I use if I wanted to change a float data type into a 
# an integer data type? ans: you would use int() to convert it into an integer

# 5. Describe three (3) Variable naming rules. Write your response in complete sentences. 
#ans: 1. there are no limit on the length of the variable name
# 2. you can only use letters numbers and underscores
# 3. you cannot use a number for the first part of the variable name

# 6. Name the operator family each of these symbols are a part of 
# and describe how each of these sybmols are used. Write your response
# using complete sentences. 
#symbols
# = ans: assignment operator it is used to give a value to a variable
# == ans: equality operator its used to compare two values to eachother
# =! ans: not equal operator its used to compare two values to eachouther

# 7. You have been hired as an engineer to develop a car speed detection system.
# the car company would like to create a function where if the user goes over a certain
# speed it will notify them to change gears. The client has provided you with the following
# guidelines on how they would like the gear system to work:
# if the driver is going over 20mph, alert the driver to shift to gear 1
# if the the driver is going over 30mph, alert the driver to shift to gear 2
# if the driver is going over 40mph, alert the driver to shift to gear 3
# if the driver is going over 70mph, alert the driver to shift back to gear 1.
# the client would like you to pass in the speed that the user is going as an argument. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.
#ans: 1. if else statements because you need to check if the driver is going over a certain speed
# 2. speed because you need to pass in the speed that the user is going
# 3. gear because you need to alert the driver to shift to a certain gear
def notify_gear_change(speed):
    if speed > 70:
        print("Shift back to gear 1")
    elif speed > 40:
        print("Shift to gear 3")
    elif speed > 30:
        print("Shift to gear 2")
    elif speed > 20:
        print("Shift to gear 1")
    else:
        print("Maintain current gear")
(speed(80))
# 8. You have been hired as an engineer to develop a fitness meal plan program. 
# your function should take in two (2) arguements; the day of the week, and the time of the day.
# depending on the time of the day; either morning or afternoon, the meal plan will change. 
# the client has provided you with the following meal plan information
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

# monday morning= 2 eggs and an apple
# monday afternoon= bbq grilled chicken and broccoli

# tuesday morning= oatmeal with strawberries and blueberries
# tuesday afternoon= baked chicken with kale

# wednesday morning= fruit salad
# wednesday afternoon= curry goat with rice and cabbage

# thursday morning= pancakes and turkey sausage
# thursday afternoon= eggplant pasta

# friday morning= steak and eggs
# friday afternoon= cheesburger and fries

# saturday morning= oatmeal
# saturday night= baked chicken with string beans

# sunday morning = oatmeal
# sunday night = steak and spinach

#ans: 1. if else statements because you need to check the day and time of the day
# 2. day because you need to check the day of the week
# 3. time because you need to check the time of the day
def meal_plan(day, time):
    if day == "monday":
        if time == "morning":
            return "2 eggs and an apple"
        elif time == "afternoon":
            return "bbq grilled chicken and broccoli"
    elif day == "tuesday":
        if time == "morning":
            return "oatmeal with strawberries and blueberries"
        elif time == "afternoon":
            return "baked chicken with kale"
    elif day == "wednesday":
        if time == "morning":
            return "fruit salad"
        elif time == "afternoon":
            return "curry goat with rice and cabbage"
    elif day == "thursday":
        if time == "morning":
            return "pancakes and turkey sausage"
        elif time == "afternoon":
            return "eggplant pasta"
    elif day == "friday":
        if time == "morning":
            return "steak and eggs"
        elif time == "afternoon":
            return "cheesburger and fries"
    elif day == "saturday":
        if time == "morning":
            return "oatmeal"
        elif time == "night":
            return "baked chicken with string beans"
    elif day == "sunday":
        if time == "morning":
            return "oatmeal"
        elif time == "night":
            return "steak and spinach"
    return "Invalid day or time"

# 9. You have been hired as an enineer to develop a school to develop an academic honors system.
# the client would like to check if the user has gotten above an 85% overall grade or has
# has accomplished passing the SAT. The client would like you to pass this information in as
# arguements. If either of these situations are true the student has made the academic honors list
# if only passing the SAT is true, congratulate the user but inform them they did not make the list.
# if they only scored above 85%, congratulate the user but inform them they did not make the list.
# if none of the conditions are met, inform them to continue studying and try again next semester. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

#ans: 1. if else statements because you need to check if the user has gotten above an 85% overall grade or not
# 2. grade because you need to check if the user has gotten above an 85% overall grade 
# 3. SAT because you need to check if the user has accomplished passing the SAT
def academic_honors(grade, sat):
    if grade > 85 or sat == "pass":
        return "lets goooo you have made the academic honors list"
    elif sat == "pass":
        return "lets goooo You have passed the SAT but you did not make the list lil bro"
    elif grade > 85:
        return "lets goooo you have scored above 85% to bad you didnt make the list though"
    else:
        return "i think you should just go home and study and try again next semester"


# 10. Create a function that will check the temperature outside. If the user enters
# a number above 60 degrees it is warm outside, if the enter a number above 80 degrees it is hot outside.
# if the user enters a number below 50 degrees it is cold outside. and if the tempeature is above 50 degrees,
# tell the user it's not warm but it's also not too cold. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.