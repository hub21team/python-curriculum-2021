"""
A new deadly virus has infected large population of a planet. A brilliant scientist has discovered a new strain of virus which can cure this disease. Vaccine produced from this virus has various strength depending on midichlorians count. 

A person is cured only if midichlorians count in vaccine batch is more than midichlorians count of person. 
A doctor receives a new set of report which contains midichlorians count of each infected patient, Practo stores all vaccine doctor has and their midichlorians count. 

You need to determine if doctor can save all patients with the vaccines he has. The number of vaccines and patients are equal.


Input Format:
First line contains the number of vaccines - N. Second line contains N integers, which are strength of vaccines. Third line contains N integers, which are midichlorians count of patients.


Output Format:
Print a single line containing 'Yes' or 'No'


Input Constraint:
1 < N < 10
Strength of vaccines and midichlorians count of patients fit in integer


Sample Input:
5
123 146 454 542 456
100 328 248 689 200

Sample Output:
No
"""


#Explanation:

#Sort the vaccines and midichlorians in ascending order using either bubble or insertion sort 
#Make sure to implement your sorting function
#Then start a loop from the first patient and compare the vaccine with the midichlorian:
#If the corresponding midichlorian for any patient is stronger than the vaccine: Just print "No" as the doctor can't save all patients.
#If you complete the loop and every patient vaccine is stronger that the corresponding midichlorian so print "Yes".

def bubbleSort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]

def savePatient():
  N=int(input())
  k=1
  arr1=[int(i) for i in input().split()]
  arr2=[int(i) for i in input().split()]

  bubbleSort(arr1)
  bubbleSort(arr2)

  for i in range(N):
    if(arr1[i]<arr2[i]):
      k=1
    else:
      k=0
      break
  if k==1:
    print("Yes")
  else:
    print('No')

savePatient()