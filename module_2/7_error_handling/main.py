###------------------------------------------------- EASY -------------------------------------------------###

# Challenge 1
def read_contents(filename):
    try:
        with open(filename) as f:
            content = f.read()
            print(content)
    except:
        print("An error occured.")
        print("Please check that you have the correct filename.")

# filename = input("Enter file to be read: ")
# read_contents(filename)

# Challenge 2
# See mine.py

###------------------------------------------------- MEDIUM -------------------------------------------------###

# Challenge 1
def find_squares(lst):
    for elt in lst:
        try:
            sqr = elt ** 2
            print("Square of", elt, "is", sqr)
        except Exception as e:
            print("Sorry,", e.__class__, "occured :(")
        
lst1 = [1, 2, 3]
lst2 = [1, "arda", 'x', 14, 12.34]

# find_squares(lst1)
# find_squares(lst2)

# Challenge 2
"""

Division is one of the core mathematical operations. Your job here is to implement `persistent_division()` function 
which should take two integers from the user and print their division. The function is persistent because it should be 
robust against possible errors so that it keeps asking for correct format of inputs until the whole operation can be 
performed error free. But, you shouldn't just write a single `except` statement, catch specific errors so that you 
can give feedback to the user. The most basic errors you shoud take precaution against are as follows:
- Division by zero
- Non-numerical input formats
"""

def persistent_division():
    while True:
        try:
            x = int(input("enter first number: "))
            y = int(input("enter second number: "))
            print(x, '/', y, '=', x/y)
            break
        except ZeroDivisionError:
            print("Can't divide by 0!")
        except ValueError:
            print("That doesn't look like a number!")
        except:
            print("Something unexpected happend!")

# persistent_division()

###------------------------------------------------- HARD -------------------------------------------------###

# Challenge 1
"""
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
"""
all_students = ["Aaron", "Eden", "Jane", "Juliet", "Stephen", "Michael", "Minerva", "Hera"]


def get_grades(students_lst):
    grades = {}
    print("Hello, teacher. Welcome to the registrar's office. We will ask you the name of the student you would like to proccess and their three grades respectively. Enter exit to terminate program")
    ### Your code here
    student_name = input("Which student's information would you like to enter: ")
    while student_name != "exit":
        # here a simple if and else would also work but for the sake of error handling we used assert
        try:
            assert student_name in students_lst
        except AssertionError as e:
            print("This student is not enrolled in this class!")
        else:
            while True:
                try:
                    midterm1, midterm2, final = (float(i) for i in input("Enter midterm1, midterm2, final grades with a space in between ").split())
                    grades[student_name] = (midterm1, midterm2, final)
                    print(student_name, "'s grades were saved successfully!")
                    break
                except ValueError as e:
                    print("Make sure you enter 3 grades, each a number")
                except Exception as e:
                    print(e)
        student_name = input("Which student's information would you like to enter: ")
    #### End of your code
    print(grades)
    return grades

get_grades(all_students)
