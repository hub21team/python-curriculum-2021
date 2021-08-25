
"""
HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent by a client on a particular day is greater than or equal to 2 * the client's median spending for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.

Given the number of trailing days d and a client's total daily expenditures for a period of n days, determine the number of times the client will receive a notification over all n days.

Example:
expenditure = [10,20,30,40,50]
d = 3

On the first three days, they just collect spending data. At day 4, trailing expenditures are [10,20,30]. The median is 20 and the day's expenditure is 40. Because 40 >= 2*20, there will be a notice. The next day, trailing expenditures are [20,30,40] and the expenditures are 50. This is less than 2*30 so no notice will be sent. Over the period, there was one notice sent.

Note: The median of a list of numbers can be found by first sorting the numbers ascending. If there is an odd number of values, the middle one is picked. If there is an even number of values, the median is then defined to be the average of the two middle values.


Function Description:

activityNotifications has the following parameter(s):

int expenditure[n]: daily expenditures
int d: the lookback days for median spending


Returns:

int: the number of notices sent


Input Format:
The first line contains two space-separated integers n and d, the number of days of transaction data, and the number of trailing days' data used to calculate median spending respectively.
The second line contains n space-separated non-negative integers where each integer i denotes expenditure[i].

Constraints:
1 <= n <= 2*10^5
1 <= d <= n
0 <= expenditure[i] <= 200

Sample Input 1:
9 5
2 3 4 2 3 6 8 4 5

Sample Output 1:
2

Sample Input 2:
5 4
1 2 3 4 4

Sample Output 2:
0
"""

def insertionSort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
      arr[j + 1] = key


def find_median(freq, d):
    mid_val, mid_p1_val = None, None
    total = 0
    sorted(freq)
    for val, count in enumerate(freq):
        total += count
        if mid_val is None and total >= (d+1)//2:
            mid_val = val
        if mid_p1_val is None and total >= (d+2)//2:
            mid_p1_val = val
            break
            
    if d%2 == 0:
        return (mid_val + mid_p1_val)/2
    else:
        return mid_val


def activityNotifications(exp, d):
  freq = [0] * 201
  notice = 0
  for i, val in enumerate(exp):
      if i >= d and val >= find_median(freq, d) * 2:
          notice += 1

          
      freq[val] += 1
      if i >= d:
          freq[exp[i-d]] -= 1
  print(notice)

n, d = [int(x) for x in input().split()]
exp = [int(x) for x in input().split()]
activityNotifications(exp,d)