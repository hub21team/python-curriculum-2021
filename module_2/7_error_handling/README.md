# Concepts

- Exception Handling

  - try / except

    ```
    try:
      # do some stuff
    except:
      # handle exception

    try:
      # do some stuff
    except Exception as e:
      # handle exception

    ```

## Exception Handling

When something goes wrong in the program, Python throws exception and remaining of our code fails to run. What if we want to continue to do remaining things in our code even if there is an exception? Or if we want to overcome the exception somehow?

Exceptions can be handled using `try` statement. You put the part that can cause an error inside `try` and handle the exception inside `except`.

For further debugging or to implement software for specific purposes we can specify the type of exception we would like to catch for example:
```python
 lst = [1, 2, 3]
 try:
   print(lst[3])
 except IndexError as e:
   print("There is a problem with the index")
```

# Challenges

## EASY

### Challenge 1:

Write a function `read_contents` that takes a filename and prints the content of the file to the console. Before calling this function, ask the user to specify the filename. Try calling your function with `exfile.txt` and another file name that is not present.  
**Note:** Be careful! User may input a filename that does not exist, therefore, you should handle this error case.

### Challenge 2:
You are given a mined code in the file `mine.py`, meaning that it is full of errors. Your job is not to correct them but use correct try/except statements with respect to specific Error types so that your code runs until the end. We picked these errors from Python built-in exceptions list, which can be found [here](https://docs.python.org/3/library/exceptions.html). First one is given as an example.

## MEDIUM

### Challenge 1:

You are writing a function named `find_squares` which takes a list as an input and prints the square of each element one by one. However, since you are a cautious coder, you decided to handle the cases where some or all elements are non-numeric. Also, if there is a problem with taking the square of an element, you should print the exception type to the console.

### Challenge 2:
Division is one of the core mathematical operations. Your job here is to implement `persistent_division()` function which should take two integers from the user and print their division. The function is persistent because it should be robust against possible errors so that it keeps asking for correct format of inputs until the whole operation can be performed error free. But, you shouldn't just write a single `except` statement, catch specific errors so that you can give feedback to the user. The most basic errors you shoud take precaution against are as follows:
- Division by zero
- Non-numerical input formats

## HARD

### Challenge 1:
Let's help the registrar's office manage their records. You are given a list of enrolled students names. Your job is to implement `get_grades(students_lst)` function which asks for students names until the user enters "exit". Then you should check if the student exists in the `students_lst`, if so ask the teacher students midterm1, mditerm2 and final grades. Make sure that the teacher enters 3 numbers, if not your program should keep asking. 

**Note:** As an extra challenge you may use different classes and replace `all_students` with a dictionary like `all_classes`. 

Sample run:
```
Hello, teacher. Welcome to the registrar's office. We will ask you the name of the student you would like to proccess and their three grades respectively. Enter exit to terminate program
Which student's information would you like to enter: Ali
This student is not enrolled in this class!
Which student's information would you like to enter: Aaron
Enter midterm1, midterm2, final grades with a space in between 90  h 7
Make sure you enter 3 grades, each a number
Enter midterm1, midterm2, final grades with a space in between 90
Make sure you enter 3 grades, each a number
Enter midterm1, midterm2, final grades with a space in between 90 78 84
Aaron 's grades were saved successfully!
Which student's information would you like to enter: Eden
Enter midterm1, midterm2, final grades with a space in between 87 88 79
Eden 's grades were saved successfully!
Which student's information would you like to enter: exit
{'Aaron': (90.0, 78.0, 84.0), 'Eden': (87.0, 88.0, 79.0)}
```
# Extra Scenarios
