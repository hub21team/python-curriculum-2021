# Concepts

- While Loops
  - while loop syntax
  - iterations with while loops
  - difference between while and for
  - forever loop  
  - break statement
  - continue statement
  

# Teaching Tips

- **Why iteration is so important?**
  The power to repeat a set of instructions, 
  is where the full power of computing comes from. 
  Really, without it, we wouldn't have computers. 
  Show how easy and fast it is to do sth for
  hundreds of many times.
  
- **Understanding of Flow of Control**
  - if I make a method call in my loop body, that method is run then Python keeps executing statements after the call
  - if my condition stops being true somewhere in the loop body, that doesn’t make me magically jump out
  - The condition is checked after every iteration
  
- **Give a real life example**
  - I eat while I'm hungry. So I'll stop eating once I'm not hungry anymore.
 ```
 while hungry:
    eat()
``` 


# Challenges

## EASY

### Challenge1:

Show the while True loop
 ```
 while True:
    print("student's name here")
``` 

### Challenge2:

Make a list containing numbers between 1 to 100 first using for loop and then while loop

### Challenge3:


Define x = 5, and increase x until it becomes 10. Do this with while True loop to show how the break statement works.

## MEDIUM

### Challenge1:

Are we there yet challenge -
ask are we there yet until users gives yes as an answer


### Challenge2:

Find factorial of given number


## HARD

### Challenge1:

 Write a program that asks for student's grades, store them in a list and compute the average of the grades
 **Hint!** You should make use of lists and the append method

### Challenge2:

Write a program that asks the user for an input of non-decreasing numbers until the user inputs an increasing number, 
at which point the program will report the length of the sequence of non-decreasing numbers.

