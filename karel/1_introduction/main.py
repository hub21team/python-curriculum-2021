"""
Introduction to basic commands

World: introduction.w
"""

from stanfordkarel import *

def main():
  move()
  move()
  turn_left()
  move()
  pick_beeper()
  move()

if __name__ == "__main__":
    run_karel_program()


"""
Excercise 1: An extension on the introduction example to make sure the student understands how to use the basic commands.

World: 1_exercise.w
"""
from stanfordkarel import *
def main():
  move()
  move()
  move()
  turn_left()
  move()
  pick_beeper()
  move()
  move()
  move()
  pick_beeper()
  turn_left()
  move()
  move()
  pick_beeper()

if __name__ == "__main__":
  run_karel_program()

"""
Exercise 2: Introducing Functions. The task is to take the beeper from (2, 1) to (5, 2) using the basic commands only.

World: 2_function_intro.w
"""
from stanfordkarel import *

def main():
  move()
  pick_beeper()
  move()
  turn_left()
  move()
  turn_left()
  turn_left()
  turn_left()
  move()
  move()
  put_beeper()

if __name__ == "__main__":
  run_karel_program()

"""
Exercise: 3 Same as exercise 2, but using a function turn_right()

World: 2_functio_intro.w
"""

from stanfordkarel import *

def turn_right():
  turn_left()
  turn_left()
  turn_left()

def main():
  move()
  pick_beeper()
  move()
  turn_left()
  move()
  turn_right()
  move()
  move()
  put_beeper()

if __name__ == "__main__":
  run_karel_program()

"""
Exercise 4: Practice Functions

World: 3_function_practice.w
"""
from stanfordkarel import *

def turn_right():
  turn_left()
  turn_left()
  turn_left()

def turn_around():
  turn_left()
  turn_left()

def move_2():
  move()
  move()

def move_3():
  move_2()
  move()

def main():
  move_2()
  turn_left()
  move()
  turn_left()
  move_2()
  pick_beeper()
  turn_around()
  move_2()
  turn_left()
  move_3()
  turn_right()
  move_3()
  pick_beeper()
  turn_around()
  move_3()
  move_2()
  pick_beeper()

if __name__ == "__main__":
  run_karel_program()
