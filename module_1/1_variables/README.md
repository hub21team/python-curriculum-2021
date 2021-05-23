# Introduction to IDE

First thing to do is to introduce the environment which the student will use to code in python. Introduction needs to cover how to open the IDE and create a python script and get it ready for coding.

# Variables

The first concept the student needs to learn is variables. There are several ways to explain what a variable is in simple terms. One way is suggested here but the tutor shall feel free to use any other way as seen fit.

A **variable** is like a box. A box can fit stuff inside it. Variables in python are boxes that can contain numbers, letters, or words. All variables or boxes have the same shape from outside. Therefore, we need a name to distinguish boxes or variables from each other. Hence, each variable has a name that we can use to see what is stored inside the variable. Each variable (box) in python usually contains a single thing (number, letter, or word), but some variables can contains a collection of things (referring to lists). (The student might be curious about whether a variable (box) can contain more than one thing, in this case it might be helpful to say that there are variables that contain more than one element but we will talk about them later).

# Variable Initialization

Now let's show the student how a variable can be created in python. To create a variable, we need to do 2 things:

1. Choose a name for the variable.
2. Put a value inside the variable. (The simplest would be to put a number.)

Let's create our first variable in which we will put the student's age. At this point we can show that the `=` symbol is used to create a variable. We write the name of the variable on the left of the `=` symbol and the value we want to put inside the variable on its right.

```python
age = 11
```
This way, now we have a box inside the computer named `age` and has `11` inside it.

**Rules for Naming Variables:**
1. Cannot start with number.
2. Can contain alphabetic (lower case and upper case) and numerical characters
3. Can contain underscore symbol: `_`

# Output

  Now, what if we want to see what is stored in a variable inside the computer ? We want a way for the computer to show us what is inside the variables. For this we can use the `print` statements. We can use it as follows:

  ```python
  age = 11
  print(age)
  ```

  At this point, we can introduce the console and the screen using which the computer can show us things, like variable values or sometimes words. We can use the `print` statement to make the computer show us words and sentences through the console.

  ```python
  print("Hello World! My name is Willy Tybur and I am learning Python")
  ```
  The student might also want to try printing different sentences and see them on the console.

# Input

  There is another way to put a value inside a variable, and we can actually do it using the console! So, not only the computer can show us things through the console, we can also give it values to store for us from the console using `input` command.

  ```python
  age = input("What is Your Age ?")
  print(age)
  ```
  Inside the `input` command, we can write a question to help us know what the computer wants us to give it. Then we can print the variable and check if the computer indeed stored the value we gave it from the console.

# Variable Types

  We have seen so far that the variables in python can store numbers. Now we might ask the question: What things other than numbers that can be stored in variables ? We have the following types:

  ```python
  # Integers
  age = 11

  # float: Decimal Numbers
  height = 168.7

  # Characters
  grade = 'A'

  # strings: (words and sentences)
  # Note that strings can be enclosed by both single and double quotes
  name1 = 'Kenny Ackerman'
  name2 = "Karl Fritz"

  # Booleans (we will learn more about this next week)
  a = True
  b = False
  ```

# Value Assignment

  Now let's ask the following question: Is there a way to change the value stored inside a variable after initializing it ? Yes, we can use the same symbol `=` to put a new value inside a variable. See how the variable value changes in the following example:

  ```python
  height = 15
  print(age)

  height = 60
  print(height)
  ```

  We can even change the variable to a different type in python:

  ```python
  var = 2000
  print(var)

  var = 139.5
  print(var)

  var = "walls"
  print(var)
  ```

# Arithmetic Operations

  In python, we can do mathematical operations on variables. The operations we can do are:
  1. `+`: addition
  2. `-`: subtraction
  3. `*`: multiplication
  4. `/`: division

  Examples:
  ```python
  x = 1 + 2
  print(x)

  y = 7 - 4
  print(y)

  z = 4 * 5
  print(z)

  w = 10 / 2
  print(w)
  ```

  Also, if we have variables which store numbers, we can apply the arithmetic operations directly on the variables instead of writing the numbers directly.
  ```python
  x = 10
  y = 2

  z = x + y
  print(z)

  z = x * y
  print(z)

  z = x / y
  print(z)
  ```

  We can also use many arithmetic operations together.
  ```python
  x = 2
  y = 3
  z = x + 2 - y
  print(z)

  z = x * y / 2
  print(z)
  ```

  When we use arithmetic operations like `+`, `-` with `*`, `/`, we need to pay attention to the order operations. Here is an example that might cause confusion. (You may ask the student what do they think the output should be)
  ```python
  x = 2 * 3 + 5
  print(x)
  ```
  Order of operations in python is like mathematics:
  1. Operations within Brackets
  2. Multiplication and Division
  3. Addition and Subtraction

  So we can also use brackets in case we want the program to perform some operation before another one:

  (Here we can show a contrast between the outcome of this operations and the previous one where multiplication was prioritized over addition)
  ```python
  x = 2 * (3 + 5)
  print(x)
  ```

# Code Comments

In python, while we write code, we can also write notes that the computer cannot see. This is useful when we want to explain what our code does.

```python
# This code creates variables that store the age and name of a person.
age = 13
name = "Annie Leonhart"
```

# Type Casting

  In python, sometimes we can change the type of a variable to another similar variable. For example, we know that `1` is an integer right ? What about `1.0` ? Is it an integer or float ? To us, we know that is is an integer, but for python whenever it sees a decimal point in a number it assumes it's a float number.

  There is a very helpful command in python that let's us know what python thinks the type of the variable is. The command is called `type`. Example:

  ```python
  num_1 = 8
  print(type(num_1))

  num_2 = 8.0
  print(type(num_2))
  ```

  So when we define a variable with `8.0`, python considers it as float. What if we want python to consider this number as integer instead of float ? We can do something called `type casting`.

  If we want to change a number from `float` to `int` we can use the `int` command.

  ```python
  num = 8.0
  print(type(num))

  num_int = int(num)
  print(type(num_int))
  ```

  Let's look at a cooler example now. Look at this string.
  ```python
  num_str = "13"
  print(type(str))
  ```

  Its type is string but it looks like a number. This is because we can define words that contain numerical characters. Do you think we can change this string like looks like an integer to an integer variable ? Yes we can! We can also use the `int` command we used previously to change the type from float to integer:

  ```python
  num_str = "13"
  print(type(num_str))
  num_int = int(num_str)
  print(type(num_int))
  ```

  Another important example is the `input` function. Anything that is given to the computer through console is stored as a string. Even numbers !! Try running this code.

  ```python
  num = input("please enter a number")
  print(type(num))
  ```

  See ?! Even if we input a number, it is stored as a string. To solve this problem, we also use casting by using the `int` command.

  ```python
  num = int(input("please enter a number"))
  print(type(num))
  ```
