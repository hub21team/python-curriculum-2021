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

##---------------------------- Medium ------------------------------##
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

##--------------- Hard --------------------------##
"""
Watermelon Challenge

Edward and Alphonso are two brothers who like watermelons too much. So they go and buy a watermelon and they want to divide it between them. The watermelon that they bought has weight `w`. Edward and Alphonso both like even numbers, and they are very good brothers so they don't care if the watermelon is not divided equally among them, they only care that each of them gets a watermelon piece whose weight is an even number. Even though they are good at their school, they need your help to tell them if the watermelon they bought can be divided to make them both happy. You should write a program that takes the weight of the watermelon `w` as an input. If they can divide the watermelon such that each of them gets an even number, then the program should print `yes`, otherwise the program should print `no`.
"""

w = int(input("Enter weight of watermelon"))

if w == 2:
    print("no")
else:
    if w % 2 == 0:
        print("yes")
    else:
        print("no")


"""
Solving equations

Write a program that can solve a quadratic equation of the form:

$$ax^2 + bx + c = 0$$

The input to the program is the 3 numbers `a`, `b`, and `c`, which are the coefficients of the equation variables.

* If a real solution does not exist, then print `no solutions`.
* If a single solution only exists, then print only 1 number.
* If two different solutions exist print the two solutions on the same line separated by a space.

**Hint:** Solutions to a quadratic equations are given using the following formula:

$$x_1 = \frac{-b + \sqrt{b^2 - 4ac}}{2a}$$
$$x_2 = \frac{-b - \sqrt{b^2 - 4ac}}{2a}$$
"""

a = int(input("Enter a."))
b = int(input("Enter b."))
c = int(input("Enter c."))

delta = (b ** 2 - 4*a*c)

if delta < 0:
    print("no solutions")
elif delta == 0:
    answer = -b / (2 * a)
    print(answer)
else:
    answer_1 = (-b + delta ** 0.5) / (2 * a)
    answer_2 = (-b - delta ** 0.5) / (s * a)
    print(answer_1, answer_2)
