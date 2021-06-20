
from karel.stanfordkarel import *


"""
## Hospital Karel
Karel begins at the left end of the first row. Her job is to build hospitals along her way to the end of the row. 
- Hospitals' starting locations are marked with a beeper. 
- The hospitals consist of six beefers, piled into two columns of three beepers. 
- Karel should complete the program at the end of the row facing East.
- Karel has infinite number of beepers in her bag.
"""


def turn_right():
    for i in range(3):
        turn_left()


def make_column():
    """
    Precondition: Karel begins at the start of a column, and is facing in the direction it needs to move
    Postcondition: Karel ends at the end of a column
    """
    put_beeper()
    for i in range(2):
        move()
        put_beeper()


def build_hospital():
    """
    Precondition: Karel is facing east and Karel is at the base of the first column of the hospital
    Postcondition: Karel is facing east at the bottom of the second column of the hostpital
    """
    turn_left()
    make_column()
    turn_right()
    move()
    turn_right()
    make_column()
    turn_left()


# walk across the world, checking for beepers
while front_is_clear():
    if beepers_present():
        pick_beeper()
        build_hospital()
    if front_is_clear():
        move()
