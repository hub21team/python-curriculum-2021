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

# Challenges

## EASY

### Challenge 1:

Write a function `read_contents` that takes a filename and prints the content of the file to the console. Before calling this function, ask the user to specify the filename. Try calling your function with `exfile.txt` and another file name that is not present.  
**Note:** Be careful! User may input a filename that does not exist, therefore, you should handle this error case.

## MEDIUM

### Challenge1:

You are writing a function named `find_squares` which takes a list as an input and prints the square of each element one by one. However, since you are a cautious coder, you decided to handle the cases where some or all elements are non-numeric. Also, if there is a problem with taking the square of an element, you should print the exception type to the console.

## HARD

### Challenge 1:

# Extra Scenarios
