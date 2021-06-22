from stanfordkarel import *


def main():
    while front_is_clear():
        check_for_hole()
        move()
    check_for_hole()


def check_for_hole():
    if right_is_clear():
        fill_the_hole()


def fill_the_hole():
    turn_right()
    move()
    if no_beepers_present():
        put_beeper()
    turn_around()
    move()
    turn_right()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

if __name__ == "__main__":
    run_karel_program("road_repair_2")
