# Concepts
* Errors
* Boolean Variables
* Number Comparison
* If Statement
* If-Else Statement
* If-Elif Statement


# Teaching Tips
* Since errors are the things that programmers encounter the most, it might be a good idea to spend some time introducing different types of errors and how to understand and fix them.
* When introducing boolean variables, the students will probably wonder about the usage and usefulness of boolean variables, therefore creating a story or a context in which they appear useful or necessary is a good way to start. In the `Number Comparison` section below, there is a suggestion on how to introduce boolean variables. They are introduced as variables that store the results of numerical checks. Any other (more creative) way introduced by the tutor would be helpful.
* One idea while introducing `if-else` and `if-elif` statement after introducing `if` is to use an example in which `if-else` and `if-elif` improve upon the `if` block.

# Errors

  If we write something in our code that violates any python rule, then when we run the program it will show us an **error**. For example, let's try running the following code:
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

  A boolean variable can only store one of 2 values: `True` or `False`. Example:
  ```python
  x = True
  print(x)

  y = False
  print(y)
  ```

  You can think of this type like a light switch, it can be either on or off.

# Number Comparison

  Let's say we want to create two variables by taking their values from console and we want the person who is writing the number in the console to enter the same number for the first and second variables. We can do it using the following code:
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

  Here is a suggested analogy that might be useful to simplify the idea of conditionals, but the tutor may feel free to use any method as seen fit.

  Image you are in a car and you arrive at a traffic light. The thing we should do is to look at color of the traffic light, right ? If the light is red, we should stop. If the light is yellow, we should prepare to move. If the light is green, we should move. The color of the light is called a condition, because we want to look at it and then depending on its color we take different actions. So in a conditional, we have 2 components: A condition, and an action. We look at the conditions, and depending on which condition is true or happening, we decide to do different things. This is something the we might need to do in programming.

Format

  ```python
  if condition :
    do something
  ```

  ## Indentation

  After we write the `if` statement, we need to press `tab` and then write the commands which we want to execute if the condition is true. This `tab` is called `indentation`. It helps us separate between the commands which depend on the conditions and the commands which do not. We will see an example to understand this point.

  Let's try to improve the previous program. We want to take two number as input. If the first number is greater than the second number we want to print: `First number is greater than second number.`. If second number is greater we want to print: `Second number is greater than first number.`. If they are equal we want to print: `Both numbers are equal.`

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

  **Suggested intro example:** Jean loves the number 8, so he wants us to write a program that takes a number as an input from console. If the number is equal to 8, we must print `Horraaay ! The input is equal to 8`. If the number is not equal to 8, we must print: `Sorry, Number is not equal to 8`. There are several ways to do so. (ask student to think about how we can do it with what we have learned so far, the expected response is to use equals and not equals commands to check equality).

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

# Challenges

## EASY

### Challenge 1: Traffic Lights

Write a program that simulates what we should do at a traffic light. We will write a program that takes the light color as an input `red`, `yellow`, or `green`, and depending on the light color we will print the required actions: `move`, `stop`, `prepare to move`. Use If-Elif Statements.

## MEDIUM

### Challenge 2: Calculator

Sasha wants to impress her friends by creating a calculator program, but sasha does not know how to write programs in python, so she asks for your help. Sasha wants to make a calculator that does only 4 basic arithmetic operations:
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)

The program should take 3 inputs from the console:
- The first number
- The second number
- a character for the arithmetic operation '+', '-', '*', or '/'


## Hard

### Challenge 3: Watermelon

Edward and Alphonso are two brothers who like watermelons too much. So they go and buy a watermelon and they want to divide it between them. The watermelon that they bought has weight `w`. Edward and Alphonso both like even numbers, and they are very good brothers so they don't care if the watermelon is not divided equally among them, they only care that each of them gets a watermelon piece whose weight is an even number. Even though they are good at their school, they need your help to tell them if the watermelon they bought can be divided to make them both happy. You should write a program that takes the weight of the watermelon `w` as an input. If they can divide the watermelon such that each of them gets an even number, then the program should print `yes`, otherwise the program should print `no`.

### Challenge 4: Solving Equations

Write a program that can solve a quadratic equation of the form:

$$ax^2 + bx + c = 0$$

The input to the program is the 3 numbers `a`, `b`, and `c`, which are the coefficients of the equation variables.

* If a real solution does not exist, then print `no solutions`.
* If a single solution only exists, then print only 1 number.
* If two different solutions exist print the two solutions on the same line separated by a space.

**Hint:** Solutions to a quadratic equations are given using the following formula:

$$x_1 = \frac{-b + \sqrt{b^2 - 4ac}}{2a}$$
$$x_2 = \frac{-b - \sqrt{b^2 - 4ac}}{2a}$$ 
