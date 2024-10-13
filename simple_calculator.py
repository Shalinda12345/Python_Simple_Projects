# define the functions needed: add, sub, mul, div
#print options to the user
# ask for values
#call the function
#while loop to continue the program until the user wants to exit
from random import choice


def add(a, b):
    answer = a+b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a, b):
    answer = a-b
    print(str(a)+" - "+str(b)+" = "+str(answer) + "\n")

def mul(a, b):
    answer = a*b
    print(str(a)+" * "+str(b)+" = "+str(answer) + "\n")

def div(a, b):
    answer = a/b
    print(str(a)+" / "+str(b)+" = "+str(answer) + "\n")


while True:
    print("A. Addition")
    print("B. Substraction")
    print("C. Multiplication")
    print("D. Division")
    print("E, Exit")

    choice = input("Input your choice : ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("Input First Number"))
        b = int(input("Input the Second Number"))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("Input First Number"))
        b = int(input("Input the Second Number"))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("Input First Number"))
        b = int(input("Input the Second Number"))
        mul(a, b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("Input First Number"))
        b = int(input("Input the Second Number"))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("Program Ended")
        quit()