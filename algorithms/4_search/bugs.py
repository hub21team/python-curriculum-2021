"""
Problem
You are developer at XYZ company. 
- You like to call the bugs in your code as enemies. 
- You maintain an array A of the list of enemies in decreasing order of their difficulty i.e., the most difficult bug will be the first element of the array. 
- Initally, there is no bugs in the code. You are given N tasks. 
- Each task contains one of the following two types of operations:
    1. 1 P: Add a bug with difficulty P into the array A.
    2. 2: Sort the array in decreasing order and print the difficulty of (n / 3)th bug in the sorted array, 
    where n is the size of the array A. If the number of bugs is less than 3, print Not enough enemies.

Input Format:

First line contains an integer N, denoting the number of tasks.
The next N lines contain one of the two types of operations mentioned above.
 

Output Format:

- For every operation of type 2, print the difficulty of (n / 3)th bug in the sorted array,
 where n is the size of the array A. If the number of bugs is less than 3, print Not enough enemies.

Constraints:
 1 <= N <= 5*10^5
 1 <= P <= 10^9


Sample Input
10
1 1
1 7
2
1 9
1 21
1 8
1 5
2
1 9
2
Sample Output
Not enough enemies
9
9

Explanation
Task 1: Add 1 to the array. Current array is [1].
Task 2: Add 7 to the array. Current array is [7,1].
Task 3: Array size is less than 3. Output is "Not enough enemies".
Task 4: Add 9 to the array. Current array is [9,7,1].
Task 5: Add 21 to the array. Current array is [21,9,7,1].
Task 6: Add 8 to the array. Current array is [21,9,8,7,1].
Task 7: Add 5 to the array. Current array is [21,9,8,7,5,1].
Task 8: Array size is 6. n/3 is equal to 2. Number at rank 2 in array is 9. Output is 9.
Task 9: Add 9 to the array. Current array is [21,9,9,8,7,5,1].
Task 10: Array size is 7. n/3 is equal to 2. Number at rank 2 in array is 9. Output is 9.
"""



def binarySearch(arr, el, i, j):
    """
    finds the location that el should be inserted maintaining the decreasing order of he array
    """
    mid = int((i+j)/2)
    if j < i:
        return i
    elif arr[mid] == el:
        return mid
    elif arr[mid] < el:
        return binarySearch(arr, el, i, mid-1)
    else:
        return binarySearch(arr, el, mid+1, j)

def addBug(P):
    """ adds the bug of difficulty P into the array """
    loc = binarySearch(arr, P, 0, len(arr)-1)
    # faster than slicing 
    arr.insert(loc, P)

def handleOp2():
    if len(arr) < 3:
        print("Not enough enemies")
    else:
        print(arr[len(arr)//3-1])

def bugs_exercise():
    N = int(input())
    global arr
    arr = []
    for i in range(N):
        op = input()
        if op[0] == "1":
            P = int(op[2:])
            addBug(P)
        elif op[0] == "2":
            handleOp2()
        else:
            pass

bugs_exercise()