from __future__ import print_function
def elevator(floor):
    floors = {
        'M': 'lobby',
        'B': 'basement',
        'R': 'rooftop',
        1: 'gym',
        2: 'restaurant',
        3: 'workspace',
        4: 'living quarters'
    }

    if floor in floors:
        return floors[floor]
    else:
        return "The floor you entered does not exist. Please enter another number."

user_input = input("Enter a floor number: ")
print(elevator(user_input))

def amusement_park(height, age):
    if height >= 5.2 and age >= 14:
        print('You can ride roller coaster 1.')
    elif height < 5.2 and age >= 14:
        print("You can ride roller coaster 2.")
    elif height < 5.2 and age < 14:
        print("You can ride roller coaster 3.")
    else:
        print("You entered your information incorrectly.")


user_height = float(input("Enter your height in feet: "))
user_age = int(input("Enter your age: "))
amusement_park(user_height, user_age)
print(result)
