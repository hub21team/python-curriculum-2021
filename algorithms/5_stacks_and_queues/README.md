# Ideas
* Data Structures
* Stacks
* Queues

# Data Structures

A data structure is a strategy to store data. An array or list is an example of a data structure where data is stored in a linear way and each element has an index that can be accessed in $O(1)$.

# Stacks

  A way to store data such that the last element that is added to the stack can be accessed and removed first. Think of a stack of books, you can only take and see the book which is added last at the top of the stack.

  A list in python can be used as a stack by using the `append` and `pop` member functions.

  The stack supports 3 main operations
  1. Add an element: `append` in lists
  2. Remove the element at the top: `pop` in lists
  3. See the element at the top: `list[-1]`.

  ```python
  stack = []

  stack.append(1)
  stack.append(2)
  last = stack[-1]
  stack.pop()
  print(stack[-1])
  ```

# Queues

  A way to store data that resembles a cashier queue at the supermarket. The first element to enter the queue is the first element to leave.

  Queues can be implemented using `deque` from `collections`

  A queue can support the following operations:
  1. Add element to the end of the queue, done using `append` of `deque`
  2. Return and remove first element in the queue: using `popleft` from `deque`

  ```python

  from collections import deque

  queue = deque()
  queue.append(8)
  print(queue.popleft())
  ```

# Problems

## Stacks
* https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/
## Queues
* https://www.hackerearth.com/practice/data-structures/queues/basics-of-queues/practice-problems/
