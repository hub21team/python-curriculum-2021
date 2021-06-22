# version 1
from stanfordkarel import *


def main():
    while front_is_clear():
        while beepers_present():
            move_beeper_to_next_corner()
        move()


def move_beeper_to_next_corner():
    pick_beeper()
    move()
    put_beeper()
    turn_around()
    move()
    turn_around()


def turn_around():
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program("carry_all_to_the_corner")



# version 2
from stanfordkarel import *


def main():
    paint_corners()
    while front_is_clear():
        while beepers_present():
            move_beeper_to_next_corner()
        move()


def move_beeper_to_next_corner():
    pick_beeper()
    move()
    put_beeper()
    turn_around()
    move()
    turn_around()


def turn_around():
    turn_left()
    turn_left()


def paint_corners():
    while front_is_clear():
        paint_one_corner()
        move()
    paint_one_corner()
    turn_around()
    while front_is_clear():
        move()
    turn_around()


def paint_one_corner():
    if no_beepers_present():
        paint_corner(GRAY)
    else:
        paint_corner(RED)


if __name__ == "__main__":
    run_karel_program("carry_all_to_the_corner")
