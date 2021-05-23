
# Concepts
* Errors
* Boolean Variables
* Number Comparison
* If Statement
* If-Else Statement
* If-Elif Statement


# Errors

  Python, like other programming languages has a set of rules that we must follow when coding. If we write something in our code that violates any python rule, then when we run the program it will show us an **error**. For example, let's try running the following code:
  ```python
  x =
  ```
  It should show us the following :
  ```
  File "main.py", line 1
  x =
     ^
  SyntaxError: invalid syntax
  ```

  This output tells us that we have a `SyntaxError`, this means that we wrote something that the computer cannot understand. The mistake in this code is that the `=` symbol expects a variable name on its left and a correct expression in the right. Since we did not put anything on the right of the `=` symbol, we got this error.

  If you look at the error, you will see that the computer tells us where the error happened. It first says the file name `main.py`, and then it says in which line the error happened: `line 1`. Then, it prints the part of the code which contains the error and also a `^` sign below the part which needs to be inspected. In the last line, it explains the type of the error. This way, when we make a mistake, the computer helps us to find where the mistake is and fix it. Let's see more examples of errors:

  ### Example 1:
  ```python
  x = 3
  print x
  ```
  Error:
  ```
  File "main.py", line 2
    print x
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
  ```
  In this code, we forgot to write parentheses around the variable name we want to print. If we look at the error, it tells us very clearly what the issue. It also gives us a hint on how to fix the code.

  ### Example 2:
  ```python
  z = 14
  x = 1 + y
  print(x)
  ```
  Error:
  ```
  Traceback (most recent call last):
  File "main.py", line 2, in <module>
    x = 1 + y
NameError: name 'y' is not defined
  ```

  The error here is that we used the variable `y` without creating or initializing it before. The error shows us the line number, the code which contains y, and also explicitly says that `y` is not defined.

# Boolean Variables

  Previously, we saw that variables in python can store different types of information, like numbers, characters, and strings. Now we will learn about a new variable type called `boolean`. It is very simple, because a boolean variable can only store one of 2 values: `True` or `False`. Example:
  ```python
  x = True
  print(x)

  y = False
  print(y)
  ```

  You can think of this type like a light switch, it can be either on or off.

# Number Comparison

  **Why are boolean variables useful ?** Boolean variables are used to help us make checks. For example, remember how we can use the `input` command to store a value in a variable by writing it from the console ? Let's say we want to create two variables by taking their values from console and we want the person who is writing the number in the console to enter the same number for the first and second variables. We can do it using the following code:
  ```python
  x = input("Please enter the first number.")
  y = input("Please enter the second number.")
  ```
  Now, we want to check if the numbers stored in `x` and `y` are equal or not. How can we do that ?

  ### Idea 1 (simple without booleans)
  We can print them and look at their outputs to know if they are equal or not.
  ```python
  x = input("Please enter the first number.")
  y = input("Please enter the second number.")
  print(x)
  print(y)
  ```
  ### Idea 2 (using booleans)

  Another idea is to create a boolean variable, which is equal to `True` if the numbers are equal, and equal to `False` when the numbers are not equal. When we print the boolean variable, we will know if they were equal or not by printing only 1 variable instead of 2. **But how do we check if two variables are equal ?**. We can use the comparison operators.
  ```python
  x = int(input("Please enter the first number."))
  y = int(input("Please enter the second number."))

  is_equal = (x == y)
  print(is_equal)
  ```
  The `==` operator takes one value on its left and one value on its right. If the values on its sides are equal, then it becomes equal to `True`, or if they not equal it becomes a `False`.

  There are also operators that can help us check if a number is less than or greater than another number.

  * `!=`: Gives `True` if the two numbers are not equal. `False` otherwise.
  * `<`: Gives `True` if left number is less than right number. `False` otherwise.
  * `<=`: Gives `True` if left number is less than or equal to the right number. `False` otherwise.
  * `>`: Gives `True` if left number is greater than right number. `False` otherwise.
  * `>=`: Gives `True` if left number is greater than or equal to the right number. `False` otherwise.

  ```python
  x = int(input("Please enter the first number."))
  y = int(input("Please enter the second number."))

  equal = (x == y)
  print(equal)

  not_equal = (x != y)
  print(not_equal)

  less_than = (x < y)
  print(less_than)

  greater_than = (x > y)
  print(greater_than)

  less_than_or_equal = (x <= y)  
  print(less_than_or_equal)

  greater_than_or_equal = (x >= y)
  print(greater_than_or_equal)

  ```

  So if we want to summarize the usage of boolean variables, we can say that they are used to store the result of a comparison operation.

# If Statement

  Now let's talk about what a conditional is. Here is a suggested analogy that might be useful to simplify the idea of conditionals, but the tutor may feel free to use any method as seen fit.

  Image you are in a car and you arrive at a traffic light. The thing we should do is to look at color of the traffic light, right ? If the light is red, we should stop. If the light is yellow, we should prepare to move. If the light is green, we should move. The color of the light is called a condition, because we want to look at it and then depending on its color we take different actions. So in a conditional, we have 2 components: A condition, and an action. We look at the conditions, and depending on which condition is true or happening, we decide to do different things. This is something the we might need to do in programming.

  We can use the `if` statement to write a condition and an action. For condition we want to see if something is `True` or `False`. This means that the condition must be either a boolean variable, or a comparison operation which gives a boolean result. We write it as follows:

  ```python
  if condition :
    do something
  ```

  After we write the `if` statement, we need to press `tab` and then write the commands which we want to execute if the condition is true. This `tab` is called `indentation`. It helps us separate between the commands which depend on the conditions and the commands which do not. We will see an example to understand this point.

  Let's take an example. Let's try to improve our previous program. We want to take two number as input. If the first number is greater than the second number we want to print: `First number is greater than second number.`. If second number is greater we want to print: `Second number is greater than first number.`. If they are equal we want to print: `Both numbers are equal.`

  ```python
  x = int(input("Please enter the first number."))
  y = int(input("Please enter the second number."))

  if x > y:
    print("First number is greater than second number")

  if y > x:
    print("Second number is greater than first number.")

  if x == y:
    print("Both numbers are equal.")
  ```
  Notice that depending on the numbers we choose, only one of the messages is being printed. Also, notice that after an if statement, the commands after it start from the beginning of the line (without a tab). So, when write an if statement, all commands that are below it with a tab, are executed if the condition is true.

# If-Else Statement

  Let's start with an example. Jean loves the number 8, so he wants us to write a program that takes a number as an input from console. If the number is equal to 8, we must print `Horraaay ! The input is equal to 8`. If the number is not equal to 8, we must print: `Sorry, Number is not equal to 8`. There are several ways to do so. (ask student to think about how we can do it with what we have learned so far, the expected response is to use equals and not equals commands to check equality).

  To do this, we can use a new more advanced if command called if-else. It has the following format:
  ```python
  if condition_is_true:
    do something
  else:
    do something else
  ```
  if-else works as follows: it first checks the condition in if, if the condition is true, then it is executed and the command under else is ignored.

  ```python
  num = int(input("Enter a number."))

  if num == 8:
    print("Horraaay ! The input is equal to 8`.")
  else:
    print("Sorry, Number is not equal to 8")
  ```

# If-Elif Statement

  If-Elif statement can be used to check multiple conditions. Its format is:

  ```python
  if condition_is_true:
    do_something
  elif second_condition_is_true:
    do_another_thing
  elif third_condition_is_true:
    do_even_another_thing
  ...
  ```

  Let's write the program where we compare two numbers again using if-elif:

  ```python
  x = int(input("Please enter the first number."))
  y = int(input("Please enter the second number."))

  if x > y:
    print("First number is greater than second number")
  elif y > x:
    print("Second number is greater than first number.")
  elif x == y:
    print("Both numbers are equal.")
  ```

  **How is this different from using multiple if statements after one another**. This is a question that the student will probably ask. The answers is that in terms what they do, they can do the exact same thing, but the difference is how the computer understands them and executes them. Let's pretend to be a computer for a moment and see how the computer sees the code and runs it. (A good strategy at this point is to walk the student line by line for both codes with elif and without elif, and focus on the point that for elif, if one of the conditions is True, the computer ignores all other elifs after it)


# Boolean Operators
