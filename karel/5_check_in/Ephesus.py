from karel.stanfordkarel import *

"""

"""


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


def build_column():
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        move()

    if no_beepers_present():
        put_beeper()


def move_down():
    turn_around()
    while front_is_clear():
        move()
    # fix karel's face
    turn_left()


def move_to_next_column():
    for i in range(4):
        move()


def main():
    while front_is_clear():
        turn_left()
        build_column()
        move_down()
        move_to_next_column()
    turn_left()
    build_column()
    move_down()

# main()
