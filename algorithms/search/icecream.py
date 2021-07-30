"""
Two friends like to pool their money and go to the ice cream parlor. They always choose two distinct flavors and they spend all of their money.

Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.

------
Example:  m=6 cost = [1, 3, 4, 5, 6]

The two flavors that cost 1 and 5 meet the criteria and they are at the indices 0 and 4.

Function Description

Complete the icecream_parlor function.

icecream_parlor has the following parameter(s):

int m: the amount of money they have to spend
int cost[n]: the cost of each flavor of ice cream
Returns

int[2]: the indices of the prices of the two flavors they buy, sorted ascending
Input Format

The first line contains an integer, t, the number of trips to the ice cream parlor. The next t sets of lines each describe a visit.

Each trip is described as follows:

The integer m, the amount of money they have pooled.
The integer n, the number of flavors offered at the time.
n space-separated integers denoting the cost of each flavor: .
Note: The index within the cost array represents the flavor of the ice cream purchased. cost[cost[0], cost[1], ..., cost[n-1]]

Constraints

1<= t <= 50,
2<= m <= 10^4
2 <= n <= 10^4
1 <= cost[i] <= 10^4, for all i in [0, n-1]

There will always be a unique solution.
Sample Input

STDIN       Function
-----       --------
2           t = 2
4           k = 4
5           cost[] size n = 5
1 4 5 3 2   cost = [1, 4, 5, 3, 2]
4           k = 4
4           cost[] size n = 4
2 2 4 3     cost=[2, 2,4, 3]
Sample Output

With 4 you may buy flavors 0 and 3 with costs 1, 3
With 4 you may buy flavors 0 and 1 with costs 2, 2
Explanation

Sunny and Johnny make the following two trips to the parlor:

The first time, they pool together m=4 dollars. Of the five flavors available that day, flavors 0 and 3  have a total cost of 1+3=4.
The second time, they pool together m=4  dollars. Of the four flavors available that day, flavors 0 and 1 have a total cost of 2+2=4.

Sample Output for all the test cases
icecream/input1.txt
For 4 you may buy flavors 0 ($1) and 3 ($3) at visit 0 in test case 1 
For 4 you may buy flavors 0 ($2) and 1 ($2) at visit 1 in test case 1
icecream/input2.txt
For 100 you may buy flavors 1 ($75) and 2 ($25) at visit 0 in test case 2 
For 200 you may buy flavors 0 ($150) and 3 ($50) at visit 1 in test case 2
For 8 you may buy flavors 3 ($4) and 4 ($4) at visit 2 in test case 2
For 542 you may buy flavors 28 ($221) and 45 ($321) at visit 3 in test case 2
For 789 you may buy flavors 10 ($104) and 55 ($685) at visit 4 in test case 2
For 101 you may buy flavors 3 ($54) and 4 ($47) at visit 5 in test case 2
For 35 you may buy flavors 39 ($9) and 45 ($26) at visit 6 in test case 2
For 890 you may buy flavors 15 ($292) and 34 ($598) at visit 7 in test case 2
For 163 you may buy flavors 54 ($48) and 73 ($115) at visit 8 in test case 2
For 295 you may buy flavors 6 ($118) and 8 ($177) at visit 9 in test case 2
icecream/input3.txt
For 100 you may buy flavors 1 ($75) and 2 ($25) at visit 0 in test case 3 
For 200 you may buy flavors 0 ($150) and 3 ($50) at visit 1 in test case 3 
For 8 you may buy flavors 3 ($4) and 4 ($4) at visit 2 in test case 3
For 542 you may buy flavors 28 ($221) and 45 ($321) at visit 3 in test case 3
For 789 you may buy flavors 10 ($104) and 55 ($685) at visit 4 in test case 3
For 101 you may buy flavors 83 ($47) and 239 ($54) at visit 5 in test case 3
For 929 you may buy flavors 412 ($207) and 583 ($722) at visit 6 in test case 3
For 718 you may buy flavors 27 ($566) and 79 ($152) at visit 7 in test case 3
For 28 you may buy flavors 379 ($7) and 632 ($21) at visit 8 in test case 3
For 74 you may buy flavors 189 ($32) and 241 ($42) at visit 9 in test case 3
For 470 you may buy flavors 449 ($368) and 666 ($102) at visit 10 in test case 3 
For 180 you may buy flavors 6 ($159) and 125 ($21) at visit 11 in test case 3
For 550 you may buy flavors 207 ($115) and 635 ($435) at visit 12 in test case 3
For 521 you may buy flavors 300 ($63) and 830 ($458) at visit 13 in test case 3
For 479 you may buy flavors 242 ($311) and 648 ($168) at visit 14 in test case 3
For 241 you may buy flavors 257 ($75) and 428 ($166) at visit 15 in test case 3 
For 212 you may buy flavors 17 ($111) and 48 ($101) at visit 16 in test case 3
For 365 you may buy flavors 6 ($292) and 31 ($73) at visit 17 in test case 3
For 548 you may buy flavors 749 ($92) and 964 ($456) at visit 18 in test case 3
For 124 you may buy flavors 195 ($89) and 717 ($35) at visit 19 in test case 3
For 677 you may buy flavors 291 ($530) and 1235 ($147) at visit 20 in test case 3
For 715 you may buy flavors 538 ($103) and 934 ($612) at visit 21 in test case 3
For 842 you may buy flavors 19 ($738) and 262 ($104) at visit 22 in test case 3 
For 832 you may buy flavors 29 ($814) and 106 ($18) at visit 23 in test case 3
For 685 you may buy flavors 2 ($432) and 93 ($253) at visit 24 in test case 3
For 882 you may buy flavors 424 ($284) and 483 ($598) at visit 25 in test case 3
For 946 you may buy flavors 622 ($197) and 922 ($749) at visit 26 in test case 3
For 803 you may buy flavors 218 ($222) and 655 ($581) at visit 27 in test case 3 
For 462 you may buy flavors 132 ($158) and 241 ($304) at visit 28 in test case 3
For 826 you may buy flavors 690 ($738) and 799 ($88) at visit 29 in test case 3
For 818 you may buy flavors 316 ($551) and 337 ($267) at visit 30 in test case 3
For 921 you may buy flavors 206 ($453) and 484 ($468) at visit 31 in test case 3
For 136 you may buy flavors 62 ($63) and 63 ($73) at visit 32 in test case 3
For 226 you may buy flavors 12 ($132) and 205 ($94) at visit 33 in test case 3
For 72 you may buy flavors 406 ($15) and 420 ($57) at visit 34 in test case 3
For 877 you may buy flavors 653 ($50) and 971 ($827) at visit 35 in test case 3
For 638 you may buy flavors 204 ($606) and 274 ($32) at visit 36 in test case 3
For 484 you may buy flavors 498 ($6) and 882 ($478) at visit 37 in test case 3
For 66 you may buy flavors 470 ($25) and 632 ($41) at visit 38 in test case 3
For 513 you may buy flavors 370 ($43) and 392 ($470) at visit 39 in test case 3
For 366 you may buy flavors 24 ($55) and 169 ($311) at visit 40 in test case 3
For 349 you may buy flavors 63 ($308) and 520 ($41) at visit 41 in test case 3
For 899 you may buy flavors 27 ($711) and 77 ($188) at visit 42 in test case 3
For 565 you may buy flavors 948 ($22) and 1589 ($543) at visit 43 in test case 3
For 942 you may buy flavors 0 ($534) and 1042 ($408) at visit 44 in test case 3
For 541 you may buy flavors 635 ($103) and 772 ($438) at visit 45 in test case 3
For 554 you may buy flavors 239 ($168) and 907 ($386) at visit 46 in test case 3
For 883 you may buy flavors 5 ($781) and 46 ($102) at visit 47 in test case 3
For 857 you may buy flavors 80 ($640) and 287 ($217) at visit 48 in test case 3
For 292 you may buy flavors 273 ($231) and 982 ($61) at visit 49 in test case 3
icecream/input4.txt
For 9 you may buy flavors 1 ($3) and 3 ($6) at visit 0 in test case 4
For 8 you may buy flavors 2 ($4) and 3 ($4) at visit 1 in test case 4
For 3 you may buy flavors 0 ($1) and 1 ($2) at visit 2 in test case 4

"""

# Naive solution


def naive_icecream_parlor(m, arr):
    for i in range(len(arr)-1):
        # use linear search to look if m- arr[i] is in the array
        for j in range(len(arr)-1, i, -1):
            if arr[i] + arr[j] == m:
                return (i, j)

# using binary search


def binary_search(arr, el, start, end, exclude=-1):
    if start > end:
        return -1
    mid = int((start+end) / 2)
    # by passing exclude argument we make sure that we didn't process the same cost twice
    if el == arr[mid] and mid != exclude:
        return mid
    elif el <= arr[mid]:
        return binary_search(arr, el, start, mid-1, exclude)
    else:
        return binary_search(arr, el, mid+1, end, exclude)


def icecream_parlor(m, arr):
    # the complexity depends on the sorting algorithm used
    enumerated = sorted(enumerate(arr), key=lambda t: t[1])
    # extract costs sorted
    arr = [t[1] for t in enumerated]
    for i in range(len(arr)):
        el_ind = binary_search(arr, m - arr[i], 0, len(arr)-1, i)
        if el_ind != -1:
            return sorted((enumerated[i][0], enumerated[el_ind][0]))


def icecream_exercise():
    # first parse inputs
    import os
    input_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "input", "icecream")
    test_case = 1
    for f in os.listdir(input_dir):
        input_file = os.path.join(input_dir, f)
        print(input_file)
        with open(input_file, "r") as fl:
            line_num = 0
            for line in fl:
                if line_num == 0:
                    t = int(line)
                    dollars = []
                    num_flavors = []
                    flavors = []
                elif line_num % 3 == 1:
                    dollars.append(int(line))
                elif line_num % 3 == 2:
                    num_flavors.append(int(line))
                else:
                    flavors.append([int(i) for i in line.split()])
                line_num += 1
            for iter in range(t):
                i, j = icecream_parlor(dollars[iter], flavors[iter])
                print(
                    f"For {dollars[iter]} you may buy flavors {i} (${flavors[iter][i]}) and {j} (${flavors[iter][j]}) at visit {iter} in test case {test_case} ")
            test_case += 1


icecream_exercise()