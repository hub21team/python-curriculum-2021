# Concepts
* What is a condition
* New Condition Functions

# What is a Condition

A condition is a function that helps us check if something is happening or not.

```
if somthing_happens:
  do somthing:
else:
  do something else
```

# New Condition Functions

|Condition|Opposite| What it checks |
|---------|--------|--------------- |
|`front_is_clear()` | `front_is_blocked()` | Is there a wall in front of Karel?|
|`beepers_present()` | `no_beepers_present()` | Are there beepers in this place?|
|`left_is_clear()` | `left_is_blocked()` | Is there a wall to Karel’s left?|
|`right_is_clear()`| `right_is_blocked()`| Is there a wall to Karel’s right?|
|`beepers_in_bag()`| `no_beepers_in_bag()`| Does Karel have any beepers in its bag?|
|`facing_north()`| `not_facing_north()`| Is Karel facing north?|
|`facing_south()`| `not_facing_south()`| Is Karel facing south?|
|`facing_east()`| `not_facing_east()`| Is Karel facing east?|
|`facing_west()`| `not_facing_west()`| Is Karel facing west?|


# Exercise 1:

The task is to go from left to right and if a cell does not have a beeper, karel should put a beeper, if a beeper already exists, then karel should remove it. World to be used is `1_flip_beepers.w`

![loop_corners](images/1_flip_beepers.png)


# Challenge 1: Maze

The task is to reach the center of the maze after picking up all the beepers on the way. World to be used is `2_challenge.w`. There are many ways to solve it, the student may realize that in this maze karel will visit all cells exactly once. Since the maze size is 8x8, then karel will move exactly 63 steps, which is the number of times the loop should iterate. Then, while moving karel can pickup the beepers by checking if they exist. Also, when the front is blocked, all karel needs to do is to turn left.

![maze](images/2_challenge.png)
