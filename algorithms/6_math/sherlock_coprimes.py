"""
Problem
Recently Watson learned the concept of coprime numbers and now he wonders given an array A1, A2 . . . AN 
what is the size of the largest subset of the array such that the each pair of elements in the subset is coprime.

Watson asks Sherlock for help and in turn Sherlock needs you.

Input
First line contains T, the number of test cases.
Each test case contains N in one line, number of elements in the array.
Next line contains N space separated elements A1, A2 . . . AN.

Output
For each test case, output the required answer in one line.

Constraints:
1 ≤ T ≤ 10
25% test data: 1 ≤ N ≤ 10
75% test data: 1 ≤ N ≤ 50
1 ≤ Ai ≤ 50

Sample Input
1
5
2 3 2 3 2
Sample Output
2

Explanation
The largest subset would be taking one of A[0], A[1], A[2] and taking one of A[3], A[4].
"""

primes = []


def solve_dp(A, row, mask, dp):
    if row == len(A):
        return 0

    if (row, mask) in dp:
        return dp[(row, mask)]

    dp[(row, mask)] = solve_dp(A, row+1, mask, dp)
    pMask = 0
    for col in range(len(primes)):
        if A[row] % primes[col] == 0:
            pMask |= (1 << col)

    if not (mask & pMask):
        dp[(row, mask)] = max(dp[(row, mask)],
                              1 + solve_dp(A, row+1, mask | pMask, dp))

    return dp[(row, mask)]


def sherlock(arr):
    m = 51
    sieve_primality = [0 for _ in range(m)]

    for i in range(2, m):
        if not sieve_primality[i]:
            primes.append(i)
            for j in range(i*i, m, i):
                sieve_primality[j] = 1

    dp = {}
    return solve_dp(arr, 0, 0, dp)


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        print(sherlock(arr))
