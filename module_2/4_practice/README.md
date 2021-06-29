# Practice Week

This week is intended for practice questions, if the tutor couldn't finish all the material from last week or feels the need to go back to some of the topics from [last week](../3_advanced_functions/README.md), they are free to do so. 

## Easy
### Find the statistics of the exam
Help the teacher calculate the statistics about her class. Write a function that takes the total grade of students in a class and returns the minimum, maximum and average of these grades. Then, define another function for teacher, which  
**Note:** Try using tuples instead of lists in your function.


### Play with variables inside functions
Two friends Seyhan and Ceyhan argue about Python functions. Seyhan this that all functions can modify the values of variables while Ceyhan doesn't agree. To end the dispute once and for all between besties explore the behavior of functions on the input.
In order to heat up the competition we will proceed in three rounds.
1. Define basic variables of types `int, bool, string, list`  and a function `did_i_modify_var(var)`  which tries to change the value of `var` to 9, print  the value of the argument inside and outside the function to see how the function behaves.
2. Moving on, define two variables of types `list, dictionary`. Implement `did_i_modify_collection(var)` that tries to change the first element of the list to "new variable", you may use the same function for dictionary, in a way it will try to add "new_variable" to the key 0.
   Now, define a variable of type `tuple`, how does the function behave? 
3. Define a variable of type `set` and implement `did_i_modify_set(var)` that tries to add "new_element" string to `var`.
**Note:** we wrote a function `see_how_it_behaves` that takes variable and modifying function as parameters but if tutor feels like this may be confusing for the student, they may include print statements in the `did_i` functions.

#### Lists, com'n
Welcome to Seyhan vs. Ceyhan Round 2. Questioning their belief system from the beginning, they now want to know what happens if they set the value of a list to a new list. How about they do this in a function?

## Medium
### Rock, paper, scissors
Write a program that plays rock, paper, scissors with the user. Your program should pick randomly from the three options.

Several bonus challenges are but not limited to:
- Play until user enters `exit`
- Keep score for both players
- Try not to use more than 2 `if` and 1 `else` statement.
- Pick a strategy for the computer, you may find a compiled list [here](https://chessandpoker.com/rps_rock_paper_scissors_strategy.html)

### Find your birthday in the year
Write a function that takes the user's birthdate (day-month) as input and calculates which day is it since the beginning of the year. Ignore the leap years.  
**Hint:** Defining a tuple/list of 12 elements may help! Or, even you may use dictionaries on the names of the months.

## Hard
### Don't be sad dear February 29
Now, re-do the exercise [*Find your birthday in the year*](#find-your-birthday-in-the-year) so that if it is a leap year, ie. multiple of 4

### Treasure Hunt
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
```