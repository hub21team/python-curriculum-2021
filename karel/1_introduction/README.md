# Concepts
* Introduction
* Main Function
* Comments
* Basic Karel Commands
* Functions
* Decomposition


# Introduction

Karel is a cool robot. It can move around the world. Karel has a bag in which it collects beepers. It can also take beepers from its bag and put them on the floor. Karel has a space it can move in which is surrounded by walls.

# Requirements
When you create a repl, make sure to Add "stanfordkarel" package from the cube on the left and add the following line to the beginning of your Karel programs, this way we can use the already defined Karel functions.
```python
from stanfordkarel import *
```

# Main functions

`def main()` block is like the green flag block in scratch. It contains the commands to be executed.

```python
def main():
  move()
```

The following is the entry point to our program, if we specifiy thepath to the world file inside  `run_karel_program`, Python will load that world and run or program in it.

```python
if __name__ == "__main__":
  run_karel_program(PATH_TO_WORLD)
```

# Comments

`#` symbol is used to comment out code. Color of comments is grey.
```python
# This is a comment
```


# Basic Karel Commands

A command is like a block in scratch but we just write it with words.

* `move()`: move karel forward.
* `turn_left()`: make karel turn counter clockwise.
* `pick_beeper()`: pickup a beeper and put it in the bag. If a beeper does not exist, karel gets an error.
* `put_beeper()`: Put beeper from karel's bag.

##  Exercise 0

  The task is to pick up the beeper. The goal is to introduce basic commands: `move()`, `turn_left()`, `pick_beeper()`. You may prepare this world beforehand or use the file `introduction.w`.

  ![Introduction World](images/introduction.png)

## Exercise 1

  The task is to collect all beepers. The goal is to make sure the student can use the basic commands introduced earlier. You may prepare this world before hand or use `1_exercise.w` file.

  ![function introduction](images/1_exercise.png)


# Introducing Functions

Exercise 2 will introduce a problem which requires karel to turn right. The student should implement it using 3 turn left commands. Exercise 3 will introduce the option of creating a function `turn_right()` to make the code simpler.

## Exercise 2

The task is take the beeper from (2, 1) and place it in the middle of the table at (5, 2). World used is `2_function_intro.w`.

![function introduction](images/2_function_intro.png)

## Exercise 3

This is the same as exercise 2, but the `turn_right()` function must be implemented and used.

![function introduction](images/2_function_intro.png)


## Exercise 4

  The task is to collect all the beepers. The code should not contain any two consective commands which are the same. Functions should be used to encapsulate repeated commands. World used is `3_function_practice.w`

  ![function introduction](images/3_function_practice.png)

# Accessing World Editor

Can be accessed to create worlds by running the following:

```python
from stanfordkarel.world_editor import run_world_editor

if __name__ == "__main__":
    run_world_editor()
```
