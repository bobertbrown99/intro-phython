correct_password = "Mario"
while True:
    user_input = input("Enter the password to access the website: ")

    
    if user_input == correct_password:
        print("Correct password! You can now view the website.")
        break  
    else:
        print("Incorrect password. Please try again.")