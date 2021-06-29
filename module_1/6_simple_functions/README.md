<!-- <style>
img {
    width: 35%;
    float: right;
    padding-left: 10px;
}
</style> -->

# Simple Functions

## Concepts

- What are functions
  - How to define functions
  - Calling functions
  - Functions that take information
  - Functions that give back information
- Pro tips for functions

### Functions

- _Deliberation:_ Why do we need functions? 
    - As we grow and learn more things as a programmer, our programs may get 
    complicated and sophisticated. How can we manage this? 
    An example question can be, how would you code my workout routine: 
    Lunges, Pushups, Squats, Lunges, Plank, ...
  <!-- ![Toaster](images/toaster.png) -->
  <img src="images/toaster.png" alt="Toaster" width="45%" align="right" style="padding-left: 10px;">
- Functions are like special toasters:
  - You put the bread, adjust the heating level and get a toasted bread.
    - What do you need to know to use a toaster?
      - What items are allowed in the toaster. For a regular toaster, bagels, simit, bread, etc. are okay but phone, remote control, fork will break the toaster.
      - You don't need to know the wiring, or heating mechanism inside the toaster as long as dangers and rules are clearly defined in the manual.
  - Once defined you can reuse them for the same funtionality.

- Functions allow us to encapsulate complex tasks. Once we define a function, we can reuse them in our code.
- We can even benefit from other people's codes -more on this next week: libraries-
- What are some functions we used so far?
  ```python
  input( ), print( ), int( ), str( )
  ```

#### How to define functions

- Similar to variables, in order to use a function we must define them first.
- Functions are _defined_ with `def` keyword in Python. 
There are 5 components and 1 important rule to function definition. 
    - `def` keyword tells Python that you are defining a function. 
    - Then we need to specify the name of the function. 
    - You can choose any name you want but names that reflect the functionality
     are better. 
     - Multiple words are separated by underscore (\_). 
     - Parantheses _()_ allow us to pass any necessary information to the function. 
     - Semicolon _:_ indicates that we are ready to define instructions. 
     - Body: the instructions to be performed by this function are defined in 
     the body. 
     - **Indentation:** Just like in control blocks and loops indentation is key to indicating the scope of the function.
  ```python 
  def my_function(): 
      # pass is a placeholder for your future code, it does nothing # functions must have at least 1 line of code 
      pass 
  ```
  **Note:** Quick debug exercises are included in `challenge_0.py` topractice function definitions.
- The following program will raise an error:

  ```python
  def my_empty_function():

  do_something
  ```

#### Calling functions

- In order for our function to execute we need to call it.

  ```python
  def say_hello():
      print("Hello")

  say_hello # this won't do anything, because without ( ) function is not executed
  say_hello()
  ```

### Functions that take information

- How about writing more customizable programs that act upon data?
- Here comes the importance of `( )` in the definition, we pass any necessary informationas parameters.
  ```python 
  def say_what_now(): 
      for i in range(5): 
          print("What?")     
  say_what_now() 
  ```

    ```python
    def say_what_now_2(repeat):
        for i in range(repeat):
            print("What?")
    # the following code will print 2 lines of "What?"
    say_what_now_2(2)
    # the following code won't print anything
    say_what_now_2(0)
    # the following code will raise TypeError
    say_what_now_2()
    ```

  **Note:** We will talk about _default parameters_ later in Module 2.

#### _Parameters_ and _arguments_:

- **Parameter** is a variable in the declaration of the function.
- **Argument** is a data you pass into function.
- Parameters act as a general way to refer to the information that will be passed to the function. Arguments on the other hand are that data. When you learn a task you learn it with general names. For example, you learn to sum any two numbers not just `2+3`. You put 2 as number1 and 3 as number2 when doing the actual operation.
  **Note:** Spend some time distinguishing between the parameters on the examples.
```python
def welcome_student(name):
    print("Welcome ", name)

welcome_student("Gül Sena")
```

### Functions that give back information

- What if we want to use the information from a function?
- Define a simple mathematical function, eg. `average` and create a variable inside. Try to access this variable outside the function.
  **Note:** This point will be confusing to most of the students at first but it is really important. Build upon the [_parameter/argument_](#parameters-and-arguments) discussion and the notion of scope. If the student is struggling, suggest basic exercises to practice.
```python
def average(a, b):
    avg = (a+b)/2

print(average(2, 5)) # this will print None
```

- **Return** We use return to give back information.

  - Let's revisit the previous example:

    ```python
    def average_with_return(a, b):
        avg = (a+b)/2
        return avg

    avg = average_with_return(2, 5)
    print(avg) # 3.5
    ```

### Pro tips for functions

- Don't try to achieve everything in a giant function. Decompose your problem and define functions for subtasks.
- Functions should be easy to understand and reusable.
- Use comments to explain the functionality and how you achieve it.

# Teaching Tips
- If the student followed _Python Module 0 - Karel_ then the tutor may remind the student the concept of _decomposition_ and spend less time in the beginning.
- Based on the students interests, the **toaster analogy** may be changed to different tools or concepts. Some examples include but are not limited to hairdresser actions, meat grinder, mathematical functions (although they lack the abstraction to some level), cooking, daily tasks, habits, Siri/virtual assistant actions etc.
- Students usually struggle establishing the **syntax** of using functions, they may do mistakes. Try to *explain the error* (Indentation, Type, Syntax, etc.) to the student so that they can internalize the concept rather than memorize rules.
- One of the most confused concept in functions is the **scope**, make sure you spend enough time explaining it. You may refer to the variable definition and conditional blocks to build on the previous material.
  - One suggestion is to try to use different names for parameters and variables that you pass to the function and note that.
  - You may use deliberate errors to draw student's attention to common mistakes, like trying to accesss a variable defined in the function.
  - Students may struggle with this for several weeks, you may reiterate the idea while writing code to make sure the student understands the concepts.

## Challenges

### Easy

#### Greet a student

Write a function `greet_single_student(name)` that greets a student by their name.
<!-- ![Alien](https://cdn.pixabay.com/photo/2016/12/13/21/20/alien-1905155_960_720.png) -->

<img src="https://cdn.pixabay.com/photo/2016/12/13/21/20/alien-1905155_960_720.png" alt="Alien" width="40%" align="right" style="padding-left: 10px;" >

#### Toast for an alien

- Prompt an alien how to prepare a toast.
- Identify subtasks, eg. open refrigerator, take bread, take cheese, cut bread slice, cut cheese slice, put in toaster, etc.
  **Note:** This is usually a fun exercise when done together with the student. Play the oblivious alien to make sure the student learns to define every variable and function.

### Medium

#### Greet students

- Write a program that greets students in the class using `greet_single_student(name)` function you previously defined. Your program should take student names as input until user prompts empty string `''`.
- Sample Execution:
  ```bash
  What is your name? Gül Sena
  Hello,  Gül Sena ! Welcome to our class.
  What is your name? Merve
  Hello,  Merve ! Welcome to our class.
  What is your name? Ece
  Hello,  Ece ! Welcome to our class.
  What is your name?
  Let's start the class
  ```

#### Compare to 5 and print:

Write a function `compare_to_5(a)` which compares the parameter `a` to 5 and prints if it is larger, less than or equal to 5.

#### Compare two numbers and print:

Write a function `compare(a, b)` which compares the parameter `a` to `b` and prints if it is larger, less than or equal to `b`.

#### Average of functions

Write a function `average_of_list(lst)` that prints the average of a list of numbers.
**Bonus:** Make sure your function doesn't break when it is used with an empty list.

### Hard

#### Mama's Bakery:

<!-- ![Lemon cheesecake](https://cdn.pixabay.com/photo/2012/04/05/00/49/pie-25428_1280.png) -->
<img src="https://cdn.pixabay.com/photo/2012/04/05/00/49/pie-25428_1280.png" alt="Lemon cheesecake" width="30%" align="left" style="padding-right: 10px;" >
Let's manage a bakery. The bakery sells special lemon cheesecakes and they are so delicious that customers usually want to buy more than available.

- Write a function that takes as input total number of slices and price per slice respectively.
- Inform each customer about how many slices are left and take their order.
  - If the customer wants to buy more than available sell them the amount left, and inform them about the situation.
- Update your records so that we can keep track of the amount of available cheesecakes.
- Inform customer about the total price.
- Repeat until you run out of cheesecakes.
  **Note:** You may change the setting and product based on student's interests

Sample execution:

```bash
Welcome to Mama's bakery, İstanbul! Today's special menu item is our lemon cheesecake.

Greetings, we have 10 units left of our cheesecake. How many units would you like to buy? 5
That would be 50  TLs.
Greetings, we have 5 units left of our cheesecake. How many units would you like to buy? 6
Excuse me, I will only be able to sell 5 slices to you.
That would be 50  TLs.
Thank you, we are out of cheesecakes, we will see you next time!
```

#### Mama's Bakery v.2

<!-- ![Baked goods](https://cdn.pixabay.com/photo/2017/07/12/15/06/bakery-2497232_1280.png) -->
<img src="https://cdn.pixabay.com/photo/2017/07/12/15/06/bakery-2497232_1280.png" alt="Baked goods" align="right" width="30%" style="padding-right: 10px;" >
Mama's Bakery grew so quickly that they are now selling apple pie and cookies too. Modify your previous program to serve the updated bakery.
**Hint:** Use previous program as a way to sell a single kind of product.
Sample execution:

```bash
Welcome to Updated Mama's bakery, İstanbul! Today's special menu items are ['lemon cheesecake', 'apple pie', 'cookies']

Now selling lemon cheesecake
Greetings, we have 10 left of our lemon cheesecake. How many units would you like to buy? 3
That would be 30  TLs.
Greetings, we have 7 left of our lemon cheesecake. How many units would you like to buy? 4
That would be 40  TLs.
Greetings, we have 3 left of our lemon cheesecake. How many units would you like to buy? 4
Excuse me, I will only be able to sell 3 units to you.
That would be 30  TLs.

Now selling apple pie
Greetings, we have 15 left of our apple pie. How many units would you like to buy? 10
That would be 90  TLs.
Greetings, we have 5 left of our apple pie. How many units would you like to buy? 3
That would be 27  TLs.
Greetings, we have 2 left of our apple pie. How many units would you like to buy? 9
Excuse me, I will only be able to sell 2 units to you.
That would be 18  TLs.

Now selling cookies
Greetings, we have 5 left of our cookies. How many units would you like to buy? 5
That would be 25  TLs.
Thank you, we are out of cheesecakes, we will see you next time!
```

# Credits:

- Code in Place 2021 [Lecture 7](https://codeinplace2020.github.io/faqs/7-Functions.pdf)
- CS 101: Merhaba, Dünya! [Lecture 4](https://cs101-merhabadunya.github.io/dersler/ders4)
- Images are taken from [pixabay](pixabay.com)
