##----------------------Easy--------------------------##
"""
Write a program that asks the user for two as input, lets call them x and y, and then the program should print 4 numbers:

1) x + y
2) x - y
3) x * y
4) x / y
"""

x = int(input("Enter first number"))
y = int(input("Enter second number"))

print(x + y)
print(x - y)
print(x * y)
print(x / y)


"""
Write a program that reads a number which is today's temperature measusred in Celcius and then convert it to Fahrenheit. The formula is as follows:

F = 1.8 * C + 32

C is the temperature in Celcius
F is the temperature in Fahrenheit
"""

C = int(input("Enter temperature in Celcius"))

F = 1.8 * C + 32

print("Temperature in Fahrenheit is: ", F)


##-----------------------------Medium--------------------------------##

"""
We want to perform a division operation between 2 numbers a and b. If b does not divide a, then there will be a remainder of the division. Write a program that takes two numbers: a and b, and print 2 numbers:

1) The quotient (q), the result of dividing a / b without the remainder
2) The remainder (r) of the division.
"""

a = int(input("Enter first number"))
b = int(input("Enter second number"))

q = a // b
r = a % b

print("Quotient:", q)
print("Remainder:", r)
