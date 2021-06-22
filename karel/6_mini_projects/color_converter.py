from stanfordkarel import *


def main():
    paint_street()
    while left_is_clear():
        reposition_to_west()
        paint_street()
        if right_is_clear():
            reposition_to_east()
            paint_street()
        else:
            turn_around()


def paint_street():
    convert_colors()
    while front_is_clear():
        move()
        convert_colors()


def convert_colors():
    if corner_color_is(RED):
        paint_corner(BLUE)
    else:
        if corner_color_is(BLUE):
            paint_corner(YELLOW)
        else:
            paint_corner(RED)


def reposition_to_west():
    turn_left()
    move()
    turn_left()


def reposition_to_east():
    turn_right()
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
    run_karel_program("color_converter_1")
