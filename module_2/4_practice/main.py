
###------------------------------------------------- EASY -------------------------------------------------###

""" 
Find the statistics of the exam
Help the teacher calculate the statistics about her class. Write a function that takes the total grade of students in a class and returns the minimum, maximum and average of these grades. Then, define another function for teacher, which
Note: Try using tuples instead of lists in your function.
"""


import random


def statistics(class_grades):
    return min(class_grades), max(class_grades), sum(class_grades)/len(class_grades)


def teacher():
    grades = [90, 75, 63, 87, 91, 79]
    min_grade, max_grade, avg = statistics
    print(
        f"Dear class,\nHere are the statistics:\n\tMin: {min_grade} Max: {max_grade} Average: {avg}")

# teacher()


"""
Play with variables inside functions
Two friends Seyhan and Ceyhan argue about Python functions. Seyhan this that all functions can modify the values of variables while Ceyhan doesn't agree. To end the dispute once and for all between besties explore the behavior of functions on the input.
In order to heat up the competition we will proceed in three rounds.
1. Define basic variables of types `int, bool, string, list`  and a function `did_i_modify_var(var)`  which tries to change the value of `var` to 9, print  the value of the argument inside and outside the function to see how the function behaves.
2. Moving on, define two variables of types `list, dictionary`. Implement `did_i_modify_collection(var)` that tries to change the first element of the list to "new variable", you may use the same function for dictionary, in a way it will try to add "new_variable" to the key 0.
   Now, define a variable of type `tuple`, how does the function behave? 
3. Define a variable of type `set` and implement `did_i_modify_set(var)` that tries to add "new_element" string to `var`.
**Note:** we wrote a function `see_how_it_behaves` that takes variable and modifying function as parameters but if tutor feels like this may be confusing for the student, they may include print statements in the `did_i` functions.
"""


def did_i_modify_var(a):
    a = 9
    print("In the function ", a)


def did_i_modify_collection(lst):
    lst[0] = 9
    print("In the function ", lst)


def did_i_modify_set(s):
    s.add("new element")
    print("In the function ", s)


def see_how_it_behaves(var, func_to_try):
    """     run the func_to_try with var as argument and print the effect    """
    print("Before the function ", var)
    func_to_try(var)
    print("After the function ", var)
    print("-"*15)


my_vars = [3, True, 4.2, "Hello"]
for my_var in my_vars:
    see_how_it_behaves(my_var, did_i_modify_var)

my_lst = [1, 2]
see_how_it_behaves(my_lst, did_i_modify_collection)

my_dict = {1: "a", 2: "b"}
see_how_it_behaves(my_dict, did_i_modify_collection)

my_set = {1, 2}
see_how_it_behaves(my_set, did_i_modify_set)

# this will result in error
# my_tuple = (1, 2)
# see_how_it_behaves(my_tuple, did_i_modify_collection)

"""
Lists Com'n
Welcome to Seyhan vs. Ceyhan Round 2. Questioning their belief system from the beginning, they now want to know what happens if they set the value of a list to a new list. How about they do this in a function?
"""


def set_lst(lst):
    lst = [1, 2, 3]
    return lst


my_lst = [3, 4, 1]
print(my_lst)
print(set_lst(my_lst))
print(my_lst)

###------------------------------------------------- MEDIUM -------------------------------------------------###

"""
Rock, paper, scissors

Write a program that plays rock, paper, scissors with the user. Your program should pick randomly from the three options.

Several bonus challenges are but not limited to:
- Play until user enters `exit`
- Keep score for both players
- Try not to use more than 2 `if` and 1 `else` statement.
- Pick a strategy for the computer, you may find a compiled list [here](https://chessandpoker.com/rps_rock_paper_scissors_strategy.html)
"""
game_options = ["Rock", "Paper", "Scissors"]


def computer_pick():
    return random.choice(game_options)


def decide_winner(player_move, computer_move):
    """ pick the winner based on the choices from player_move and computer_move """
    if player_move == computer_move:
        print("It is a tie!")
        return 0.5, 0.5

    player_won = (player_move == "Rock" and computer_move == "Scissors") or (
        player_move == "Scissors" and computer_move == "Paper") or (player_move == "Paper" and computer_move == "Rock")
    if player_won:
        print("Player won")
        return 1, 0
    else:
        print("Computer won")
        return 0, 1


def rock_paper_scissors():
    """ play rock, paper, and scissors with the user """
    choice = input("What is your choice: ")
    player_score, computer_score = 0, 0
    while choice != "exit":
        while choice.capitalize() not in game_options:
            choice = input(
                "Really? Please enter a valid choice: ", game_options)
        computer_choice = computer_pick()
        p, c = decide_winner(choice, computer_choice)
        player_score += p
        computer_score += c
        choice = input("What is your choice: ")


# rock_paper_scissors()


""""
Find your birthday in the year
Write a function that takes the user's birthdate (day-month) as input and calculates which day is it since the beginning of the year.
"""


def calculate_which_day(day, month):
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = day
    for passed_month in range(month):
        total_days += days_in_months[passed_month]
    return total_days


def birthday_exercise():
    day = int(input("Enter your birth day: "))
    month = int(input("Enter your bith month: "))
    print("You were born in the", calculate_which_day(day, month), " th day")

# birthday_exercise()

###------------------------------------------------- HARD -------------------------------------------------###


def calculate_which_day2(day, month, year):
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # update february in case of a leap year
    if year % 4 == 0:
        days_in_months[1] = 29
    total_days = day
    for passed_month in range(month):
        total_days += days_in_months[passed_month]
    return total_days


def birthday_exercise2():
    day = int(input("Enter your birth day: "))
    month = int(input("Enter your bith month: "))
    year = int(input("Enter your birth year: "))
    print("You were born in the", calculate_which_day(
        day, month, year), " th day")


# birthday_exercise2()
"""
Treasure Hunt
If we were to meet in person than we could have played an epic Treasure Hunt, luckily we can program the hunt by ourselves.
1. Your first clue is your name, find the first vowel in it. But remember to define a function so you can find anyone's name. If your name has no vowels you may use an 'a'. You are given a list of vowels for ease.
2. Now pick your second_clue as the word starting with the vowel from Part 1 in the `second_hint_words` list.
3. Your third_clue is the character in the middle of your second_clue. If the word has event number of letters, you may choose either one as the middle letter.
4. Your fourth clue is a number, find the ASCII value of your third_clue. You may think of the ASCII code as the numeric representation of a character
**Hint:** You may use the `ord` function.
5. Now, your fifth and final clue is a tuple! Take fourth_clue to the power your age (get your birth year as input and calculate your age) modulo (total number of days in a leap year - todal days of the week) + a random angle from a triangle
The two numbers represent the longitude and latitude of your next vacation after covid ends! Is it somewhere you wanted to go?  
**Hint:** You may use `datetime` library:
```python
from datetime import datetime
currentYear = datetime.now().year
```"""
# sample execution
vowels = ['a', 'e', 'u', 'ü', 'i', 'ı', 'o', 'ö']
second_hint_words = ['alligator', 'elephant', 'umbrella',
                     'üniversite', 'instagram', 'ığdır', 'occupation', 'öğrenci']
LONGITUDE_RANGE = 360
LATITUDE_RANGE = 180


def first_vowel(name):
    # first convert every letter to lower
    name = name.lower()
    for ch in name:
        if ch in vowels:
            return ch
    print("Wow you don't have any vowels in your name, so I am giving you an a")
    return 'a'


def find_second_hint(vowel):
    for word in second_hint_words:
        if word.startswith(vowel):
            return word
    return second_hint_words[0]


def find_the_middle_char(word):
    n = len(word)
    middle = int(n/2)
    return word[middle]


def find_fifth_clue(fourth):
    birthyear = int(input("Which year were you born in?"))
    age = 2021 - birthyear
    modulo = 366-7
    lng = fourth**age % modulo
    lat = random.randint(0, 180)
    return (lng, lat)


first_clue = "Gül Sena"
vowel = first_vowel(first_clue)
second_clue = find_second_hint(vowel)
third_clue = find_the_middle_char(second_clue)
fourth_clue = ord(third_clue)
fifth_clue = find_fifth_clue(fourth_clue)
print("After covid ends, I am going to ", fifth_clue)
