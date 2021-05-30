##-------------------------------------Easy---------------------------------##

"""
Write a program that simulates what we should do at a traffic light. We will write a program that takes the light color as an input `red`, `yellow`, or `green`, and depending on the light color we will print the required actions: `move`, `stop`, `prepare to move`. Use If-Elif Statements.
"""

light_color = input("Please enter light color")

if light_color == "red":
    print("stop")
elif light_color == "yellow":
    print("prepare to move")
elif light_color == "green":
    print("move")

"""
Calculator Challenge

Sasha wants to impress her friends by creating a calculator program, but sasha does not know how to write programs in python, so she asks for your help. Sasha wants to make a calculator that does only 4 basic arithmetic operations:
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)

The program should take 3 inputs from the console:
- The first number
- The second number
- a character for the arithmetic operation '+', '-', '*', or '/'
"""

num_1 = int(input("Enter first number"))
num_2 = int(input("Enter second number"))

op = input("Enter desired operation")

if op == '+':
    answer = num_1 + num_2
elif op == '-':
    answer = num_1 - num_2
elif op == '*':
    answer = num_1 * num_2
elif op == '/':
    answer = num_1 / num_2
else:
    print("The input operation is not correct.")

print(answer)
