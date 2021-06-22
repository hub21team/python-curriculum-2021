"""
Exercise 1: Flip the cells. If beeper exists, then remove it. If a beeper does not exist, then put one.

World: 1_flip_beepers.w
"""

from stanfordkarel import *


def main():

  for i in range(7):
    move()
    if beepers_present():
      pick_beeper()
    else:
      put_beeper()


if __name__ == "__main__":
    run_karel_program("4_flip_beepers")


"""
Challenge: Go to the center of the maze and pick up all beepers on the way.

World: 2_challenge.w
"""

from stanfordkarel import *

def main():

  for i in range(63):
    move()
    if beepers_present():
      pick_beeper()
    if front_is_blocked():
      turn_left()


if __name__ == "__main__":
    run_karel_program("5_challenge")
