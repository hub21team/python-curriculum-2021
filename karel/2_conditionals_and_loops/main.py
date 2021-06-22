"""
Exercise 1: Decompositon

World: 1_decomposition.w
"""

#-------------- Naive Version ---------------------------#
from stanfordkarel import *

def turn_right():
  turn_left()
  turn_left()
  turn_left()

def turn_around():
  turn_left()
  turn_left()

def main():

  move()
  move()
  turn_right()
  move()
  put_beeper()
  turn_around()
  move()
  turn_right()
  move()
  move()
  move()
  turn_right()
  move()
  put_beeper()
  turn_around()
  move()
  turn_right()
  move()
  move()


if __name__ == "__main__":
  run_karel_program()

#------------ Decomposed Version --------------#
from stanfordkarel import *

def turn_right():
  turn_left()
  turn_left()
  turn_left()

def turn_around():
  turn_left()
  turn_left()

def fix_hole():
  turn_right()
  move()
  put_beeper()
  turn_around()
  move()
  turn_right()

def move_2():
  move()
  move()

def move_3():
  move_2()
  move()

def main():

  move_2()
  fix_hole()
  move_3()
  fix_hole()
  move_2()

if __name__ == "__main__":
  run_karel_program()


"""
Exercise 2: Decomposition Challenge


World: 2_decomposition.w
"""

def turn_right():
  turn_left()
  turn_left()
  turn_left()

def turn_around():
  turn_left()
  turn_left()

def fix_hole():
  turn_right()
  move()
  put_beeper()
  turn_around()
  move()
  turn_right()

def move_2():
  move()
  move()

def move_3():
  move_2()
  move()

def main():

  move_2()
  fix_hole()
  move_3()
  fix_hole()
  move()

  turn_left()
  move_2()
  fix_hole()
  move_2()
  fix_hole()
  move()

  turn_left()
  move_2()
  fix_hole()
  move_2()
  fix_hole()
  move()

  turn_left()
  move_2()
  fix_hole()
  move()


if __name__ == "__main__":
  run_karel_program()

"""
Exercise 3: Pick all the beepers in the same cell

World: 3_loop.w
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
Exercise 4: Pick all beepers

World: 4_loop_corners.w
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
Exercise 5: Pick all beepers from the corners

World: 5_nested_loops.w
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
