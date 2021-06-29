from karel.stanfordkarel import *
###------------------------------------------------- EASY -------------------------------------------------###
""" 
Take Karel to the End
Write a program that makes Karel move until the end of the street. 
"""


def move_to_the_end():
    while front_is_clear():
        move()


###------------------------------------------------- MEDIUM -------------------------------------------------###

"""
Dence Karel
Karel loves to the dance. Today's mood? Let's do the twist. 
Write a program that makes Karel walk across the dance floor (hmm, aka streets) but she must do a full turn at each step.  So Karel does a spin in each round,which is turn left once and keep going until her feet are on the ground again.
""""


def twist_karel():
    turn_left()
    while right_is_clear():
        turn_left()


def dance_karel():
    while front_is_clear():
        move()
        twist_karel()

# dance_karel()

###------------------------------------------------- HARD -------------------------------------------------###
"""
### Put Beeper and Climb
Karel tries to move to the top right corner of the world and but beepers along her way. You may assume that the worlds always have an odd number of streets and rows.*
Note that:
- Karel always begins at the bottom left corner of and empty world facing East.
- You may assume that the world is an odd number of columns across
- Karel's bag has infinite beepers.
- It does not matter which direction Karel ends up facing.
- The world is always square (the world's height is the same as its width)
*Note to tutor: you may ask the student to extend their code to work on an even numbered square world.
"""

def turn_right():
    for i in range(3):
        turn_left()


def step_up():
    put_beeper()
    turn_left()
    if front_is_clear():
        move()
        turn_right()


def put_beeper_and_climb():
    while front_is_clear():
        step_up()
        move()
    # extension
    if no_beepers_present():
        put_beeper()

# put_beeper_and_climb()
