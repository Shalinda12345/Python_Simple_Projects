# ask the user if they want to generate a password
# if they do, ask for password length
# generate  password
# Print password
# If initial response is no exit program


import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("How long would you like your password to be? "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Do you want to generate a password? (Yes/No): ")

if option.lower() == "Yes".lower():
    generate_password()
elif option.lower() == "No".lower():
    print("Program Ended")
    quit()
else:
    print("Invalid Input, Please input Yes or No")
    quit()