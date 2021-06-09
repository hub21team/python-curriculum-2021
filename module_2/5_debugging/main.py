"""
(1) Using OR Operator, checking if a variable is equal to either one
of two numbers
"""
##--------Wrong--------##
num = 1
if num == 2 or 1:
    print('the number is 2 or 1')
else:
    print('the number is not 2 or 1')

##-------Fixed----------##
num = 1
if num in (1, 2):
    print('the number is 2 or 1')
else:
    print('the number is not 2 or 1')

"""
(2) Initializing variable every time in a loop
"""
##-----------Wrong-------------##
my_list = [5, 2, 12, 7, 3, 8]
for element in my_list:
    low = []
    if element < 5:
        low.append(element)
print(low)

##----------Fixed------------##
my_list = [5, 2, 12, 7, 3, 8]
low = []
for element in my_list:
    if element < 5:
        low.append(element)
print(low)

"""
(3) Mixing Between '=' and '=='
"""
##----------Wrong---------##

num = 8
if num = 8:
    print("Number is eight: ", num)
else:
    print("Number is not eight: ", num)

##-----------Fixed----------##
num = 8
if num == 8:
    print("Number is eight: ", num)
else:
    print("Number is not eight: ", num)

"""
(4) Foregtting to use parentheses when calling a function without
parameters. The program gets a string input. If the string is
'greet', it calls the greet function. If the string is 'quit',
it calls the quit function.
"""
##----------Wrong-------------##

def greet():
    print("Greeting")
def quit():
    print("Sayonara")
prompt = input("Please enter desired action (greet or quit)")
if prompt == 'greet':
    greet
elif prompt == 'quit':
    quit()

##-----------Fixed---------------##
def greet():
    print("Greeting")
def quit():
    print("Sayonara")
prompt = input("Please enter desired action (greet or quit)")
if prompt == 'greet':
    greet()
elif prompt == 'quit':
    quit()

"""
(5) Entering an infinite While loop because condition variable was
not updated.
"""
##--------------Wrong---------------##
i = 0
n = 10
name = 'Marco'
while i < n:
    print("hello", name)

##-------------Fixed----------------##
i = 0
n = 10
name = 'Marco'
while i < n:
    print("hello", name)
    i += 1

"""
(6) Implementing a loop using range with wrong bounds. The following
code should print all numbers from 1 to 13 inclusive.
"""
##-----------Wrong------------------##
for number in range(1, 20):
    print(number)

##-----------Fixed-----------------##
for number in range(1, 21):
    print(number)

"""
(7) Difference between using if-elif or using multiple ifs. The
following code should take a number from user which represents an
exam grade between 0 and 100, and the program should print a letter
grade depending on the grade as follows:
- if grade > 100 or grade < 0: error
- if 100 > grade >= 90: A
- if 90 > grade >= 80: B
- if 80 > grade >= 70: C
- if 70 > grade >= 60: D
- if 0 < grade < 60: F
"""
##--------------Wrong---------------##
grade = int(input("Enter Grade: "))
if grade < 0 or grade > 100:
    print("error")
if grade >= 90:
    print("A")
if grade >= 80:
    print("B")
if grade >= 70:
    print("C")
if grade >= 60:
    print("D")
if grade < 60:
    print("F")

##--------------Fixed---------------##
grade = int(input("Enter Grade: "))

if grade < 0 or grade > 100:
    print("error")
elif grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

"""
(8) FizzBuzz Test: Write a program that prints the numbers from 1 to
100 but for multiples of 3, it prints `Fizz` instead of the number
and for the multiples of 5, it prints `Buzz` instead of the number,
and for numbers which are multiples of both 3 and 5 print `FizzBuzz`
"""

##-------------Wrong----------------##
for number in range(1, 101):
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    else:
        print(number)

##-----------Fixed------------------##
for number in range(1, 101):
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

"""
(9) Forgetting returning values in function
"""
##------------------Wrong-------------------##
def add(x, y):
    answer = x + y
print(add(1, 2))

##-----------------Fixed-------------------##
def add(x, y):
    answer = x + y
    return answer
print(add(1, 2))


"""
(10) Forgetting to cast input type from string to int. The following
program should take 2 numbers as inputs and add them.
"""
##--------------Wrong-----------------------##
x = input("Enter first number. ")
y = input("Enter second number. ")
print(x + y)

##----------------Fixed-------------------##
x = int(input("Enter first number. "))
y = int(input("Enter second number. "))
print(x + y)
