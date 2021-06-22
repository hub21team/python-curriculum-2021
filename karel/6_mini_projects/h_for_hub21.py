# version 1
from stanfordkarel import *


def main():
    pick_all_beepers()
    turn_back_to_beginning()
    write_letter_h()


def pick_all_beepers():
    move()
    pick_beeper()
    pick_beeper()
    pick_beeper()
    move()
    turn_left()
    move()
    pick_beeper()
    pick_beeper()
    pick_beeper()
    pick_beeper()
    turn_left()


def turn_back_to_beginning():
    while front_is_clear():
        move()
    turn_left()
    move()
    turn_left()


def write_letter_h():
    draw_rod()
    turn_right()
    move()
    turn_right()
    move()
    put_beeper()
    move()
    turn_left()
    move()
    draw_rod()


def draw_rod():
    turn_left()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
   


def turn_right():
    turn_left()
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program("h_for_hub21")


# version 2
from stanfordkarel import *

def main():
    pick_all_beepers()
    turn_back_to_beginning()
    write_letter_h()


def pick_all_beepers():
    move()
    pick_beeper()
    pick_beeper()
    pick_beeper()
    move()
    turn_left()
    move()
    pick_beeper()
    pick_beeper()
    pick_beeper()
    pick_beeper()
    turn_left()


def turn_back_to_beginning():
    while front_is_clear():
        move()
    turn_left()
    move()
    turn_left()


def write_letter_h():
    draw_rod()
    turn_right()
    move()
    turn_right()
    move()
    put_beeper()
    paint_corner(YELLOW)
    move()
    turn_left()
    move()
    draw_rod()


def draw_rod():
    turn_left()
    put_beeper()
    paint_corner(YELLOW)
    move()
    put_beeper()
    paint_corner(YELLOW)
    move()
    put_beeper()
    paint_corner(YELLOW)


def turn_right():
    turn_left()
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program("h_for_hub21")

