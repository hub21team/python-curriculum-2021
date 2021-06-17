"""
Exercise 1: Pick all the beepers in the same cell

World: 1_loop.w
"""
from stanfordkarel import *

def main():
  move()
  move()
  for i in range(23):
    pick_beeper()

if __name__ == "__main__":
    run_karel_program("1_loop")

"""
Exercise 2: Pick all beepers

World: 2_loop_corners.w
"""
from stanfordkarel import *

def main():

  for i in range(3):
    move()
    move()
    move()
    pick_beeper()
    turn_left()

if __name__ == "__main__":
    run_karel_program("2_loop_corners")


"""
Exercise 3: Pick all beepers from the corners

World: 3_nested_loops.w
"""
from stanfordkarel import *


def main():

  for i in range(3):
    move()
    move()
    move()
    for j in range(7):
      pick_beeper()
    turn_left()

if __name__ == "__main__":
    run_karel_program("3_nested_loops")


"""
Exercise 4: Flip the cells. If beeper exists, then remove it. If a beeper does not exist, then put one.

World: 4_flip_beepers.w
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

World: 5_challenge.w
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
