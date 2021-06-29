################## Challenge ##################
""" 
You are given a mined code in the file `mine.py`, meaning that it is full 
of errors. Your job is not to correct them but use correct try/except 
statements with respect to specific Error types so that your code runs 
until the end. We picked these errors from Python built-in exceptions list,
which can be found [here](https://docs.python.org/3/library/exceptions.html). First one is given as an example.
"""
### Example
print("Here is a random number between 1 to 100")
print(random.randint(1, 100))

    
my_set = {i for i in range(19)}
print(my_set[2])

my_set.append(2)

my_dict = {i: i**2 for i in range(10)}
print(my_dict[10])


lst = [i for i in range(20, 30)]
ptinr(lst[20])


lst = [i for i in range(20, 30)]
print(lst[10])


open("Do I even exist?", "r")


from random import randoom


def my_infinite_function(a):
    print(a)
    my_infinite_function(a)

my_infinite_function(1)

print("Wohoo, congratualations you saved the program!!!")

################## Solution ##################
    
try:
    my_set = {i for i in range(19)}
    print(my_set[2])
# sets do not support indexing
except TypeError as e:
    print("Type Error", e)
except Exception as e:
    print(e)


try:
    my_set.append(2)
# sets don't have an append method
except AttributeError as e:
    print("Attribute Error", e)


my_dict = {i: i**2 for i in range(10)}
try:
    print(my_dict[10])
# my_dict doesn't have a key 10
except KeyError as e:
    print("Key Error", e)
except Exception as e:
    print(e)


try:
    lst = [i for i in range(20, 30)]
    ptinr(lst[20])
# ptinr is not defined, here note that lst[20] is also problematic but Python will raise an exception 
# with the first error and skip the rest of the program until the except statement
except NameError as e:
    print("Name Error", e)
except Exception as e:
    print(e)

try:
    lst = [i for i in range(20, 30)]
    print(lst[10])
# indices in lst go from 0 to 9
except IndexError as e:
    print("Index Error", e)
except Exception as e:
    print(e)

try:
    open("Do I even exist?", "r")
# Our operating system (aka OS) handles file input and output requests, since a file with the name "Do I even exist?" 
# doesn't exist OS raises an error
except OSError as e:
    print("OS Error", e)
except Exception as e:
    print(e)

try:
    from random import randoom
# randoom is not defined in random
except ImportError as e:
    print("Import Error:", e)
except Exception as e:
    print(e)


def my_infinite_function(a):
    print(a)
    my_infinite_function(a)

try:
    my_infinite_function(1)
# my_infinite_function calls itself (this is called recursion) and since there is no stopping condition 
# our program gives a RecursionError
except RecursionError as e:
    print("Recursion Error", e)
except Exception as e:
    print(e)