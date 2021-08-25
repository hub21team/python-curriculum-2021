
"""
Sorting is useful as the first step in many different tasks. The most common task is to make finding things easier, but there are other uses as well. In this case, it will make it easier to determine which pair or pairs of elements have the smallest absolute difference between them.

Example:
arr=[5,2,3,4,1]
Sorted, arr=[1,2,3,4,5]. Several pairs have the minimum difference of 1:[(1,2),(2,3),(3,4),(4,5)]. Return the array [1,2,2,3,3,4,4,5].

Note:
As shown in the example, pairs may overlap.
Given a list of unsorted integers, arr, find the pair of elements that have the smallest absolute difference between them. If there are multiple pairs, find them all.


Function Description:
Complete the closestNumbers function in the editor below.

closestNumbers has the following parameter(s):
- int arr[n]: an array of integers

Returns:
- int[]: an array of integers as described


Input Format:
The first line contains a single integer n, the length of arr.
The second line contains n space-separated integers, arr[i].


Constraints:
- 2 <= n <=200000
- -10^7 <= arr[i] <= 10^7
- All a[i] are unique in arr.


Sample Input 0
10
-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854

Sample Output 0
-20 30

Explanation 0
(30) - (-20) = 50, which is the smallest difference.


Sample Input 1
12
-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854 -520 -470

Sample Output 1
-520 -470 -20 30

Explanation 1
(-470) - (-520) = 30 - (-20) = 50, which is the smallest difference.


Sample Input 2
4
5 4 3 2

Sample Output 2
2 3 3 4 4 5

Explanation 2
Here, the minimum difference is 1. Valid pairs are (2, 3), (3, 4), and (4, 5).
"""
def insertionSort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
      arr[j + 1] = key
      
def closest():
    N = int(input())
    ar = sorted(list(map(int, str(input()).split())))
    prs = ''
    mini = pow(10, 7) + 1
    for i in range(1, N):
        diff = abs(ar[i-1] - ar[i])
        if (diff <= mini):
            if (diff < mini):
                prs = ''
            mini = diff
            prs += str(ar[i-1]) + ' ' + str(ar[i]) + ' '
    print (prs)

closest()