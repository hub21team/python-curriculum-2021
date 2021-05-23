""" in class examples """

# # Let's define a few functions

# # # Debug the following function definitions
# # 1. we should always use ( ) after the function name
# def my_function:
#     pass

# # 2. Indentation
# def my_function():
# print("Whaat")

# # 3. semicolon
# def my_buggy_function()
#     print("What's wrong this time?")

# # 4. def keyword
# hello():
#     print(hello)

# 5. the function is not called
def say_hello():
    print("hello")


# # Input examples from handout
# def say_what_now():
#     for i in range(3):
#         print("What?")
# say_what_now()

# # version 2, with parameters
# def say_what_now_2(repeat):
#     for i in range(repeat):
#         print("What?")
# # the following code will print 2 lines of "What?"
# say_what_now_2(2)
# # the following code won't print anything
# say_what_now_2(0)
# # the following code will raise Type error
# say_what_now_2()

# Debug the following examples


# # Parameters and arguments
# def print_sum(a, b):
#     print(str(a+b))


# num1 = float(input("Enter first number:"))
# num2 = float(input("Enter second number"))
# print_sum(num1, num2)

# # Scope
# def average(a, b):
#     avg = (a+b)/2


# # average(2, 5)
# # print(avg) # this will raise NameError => because avg is only defined in average

# # Return
# print(average(2, 5))  # this will print None


# def average_with_return(a, b):
#     avg = (a+b)/2
#     return avg
# print(average_with_return(2, 5))