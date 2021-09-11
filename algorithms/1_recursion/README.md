# Ideas
* How function calls work in memory
* Recursion
* Recursive vs Iterative Solutions

# How Function Calls work in Memory

  When a function is called from a program, a part of the memory is reserved and the function parameters are copied and sent to that part of the memory for the function call. Even if the same function is called multiple times, each time, a different part of the memory is reserved and used to execute the function call.

# Recursion

  Recursion is the idea of calling a function from within itself. This is possible because each function call takes place in its own memory space, regardless of whether it is the same function or not.

  This technique is very useful because many maths and computer science problems have a recursive nature.

## Example : Factorial

  The problem is given a number $n$, calculate its factorial. The factorial of a number $n$ is defined as follows:

  $$n! = n (n - 1) (n-2) \dots (1)$$

  That is, the product of all integers from $n$ until $1$. **How can we calculate this using recursion ?**

  ```python
  def factorial(x):
    if x == 1:
      return 1
    return x * factorial(x - 1)
  ```

## Example : Fibonacci Sequence

  Fibonacci Sequence is a sequence of numbers that starts with $0$ and $1$, and after that each number in the sequence is the sum of the two previous numbers.

  $0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, \dots$

  we can write the $n^{th}$ element of the sequence as follows:

  $$ F(n) = F(n - 1) + F(n - 2)$$

  In code this translates to:
  ```python
  def fibonacci(n):
    if n == 0:
      return 0
    if n == 1:
      return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
  ```


# Recursive vs Iterative Solutions


  Most of the problems that can be solved using recursion can be also solved in a different way called the **iterative** approach.

  ```python
  def factorial(x):
    answer = 1
    for i in range(1, x + 1):
      answer *= i
    return answer  
  ```

  ```python
  def fibonacci(n):
    previous = 0
    before_previous = 1
    answer = 0
    for i in range(n - 2):
      answer = previous + before_previous
      before_previous = previous
      previous = answer
    return answer      
  ```

  **Which technique is better?** It depends on the problem.


# Problems

* N-Queens Problem: https://leetcode.com/problems/n-queens/
