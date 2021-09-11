# Ideas
* Motivation
* Big-O Notation

# Motivation

  We saw in the previous week that there can be different algorithms that can do the same thing, but are all these algorithms the same ?

  When creating an algorithm to solve a problem, there are 2 important things we need to know about the algorithm:

  1. How fast is the algorithm ?
  2. How much memory does the algorithm cost ?

  We need to find a way to measure the speed of each algorithm, as well as the amount of memory each algorithm takes.

  The speed and memory consumption of most of the algorithms depends on the size of the input to the algorithm. For example in the case of sorting, the time it takes the algorithm to sort the array increases as the size of the array increases.

  This is why we need Big-O Notation.

# Big-O Notation

  Big-O Notation is a notation used to represents the speed or memory consumption of an algorithm as a function of the input.

  **Intuitive Explanation**: If the input size to an algorithm is $n$, and we, for example, use a loop that iterates $n$ times to find the solution, then we say that the **time complexity** of the algorithm is $O(n)$ and it is read as "big O of n". If we use two nested loops each running for $n$ times, the time complexity of the solution is $O(n^2)$. Operations such as boolean, arithmetic, or assignment are assumed to take a constant amount of time, denoted as $O(1)$. The same logic applied to **memory complexity**


  **Mathematical Explanation**: We say that the worst-time complexity of an algorithm is $O(f(n))$, where $f(n)$ is a function of $n$, if the number of steps it takes to execute the algorithm is less than less than or equal to $c .f(n)$, where $c$ is a constant greater than 1. The same logic applies to the worst-case memory complexity.


# Practice
* https://www.geeksforgeeks.org/practice-questions-time-complexity-analysis/
* https://www.interviewbit.com/courses/programming/topics/time-complexity/
* https://medium.com/@manishsundriyal/overview-time-space-complexity-f973513b701e
* https://www.hackerearth.com/practice/basic-programming/complexity-analysis/time-and-space-complexity/tutorial/
* https://brilliant.org/practice/complexity-runtime-analysis-level-3/
