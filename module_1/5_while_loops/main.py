###------------------------------------------------- EASY -------------------------------------------------###

# show the while true loop


# make a list containing numbers between 1 to 100 first using for loop and then while loop
list = []
for number in range(1, 101):
  list.append(number)

list2 = []
number = 0
while number<100:
  number += 1
  list2.append(number)

# define x = 5, and increase x until it becomes 10.
x = 5
while x<10:
  x += 1
  if x==8:
    break

###------------------------------------------------- MEDIUM -------------------------------------------------###


# Are we there yet challenge
# ask are we there yet until get yes as an answer
answer = input("Are we there yet?")
while not answer == "yes":
  answer = input("Are we there yet?")
print("Yay we are there!")


# find factorial of given number
i = int(input("enter a number: "))
result = 1
x = 1
while x < i:
  x += 1
  result = result * x
print(result)


# Write a program that asks for student's grades, store them in a list and compute the average

score_list = []
while True:
  score = float(input("Enter score (0 to stop): "))
  if score == 0:
    break
  score_list.append(score)

total = 0
average = 0
for score in score_list:
  total += score

average = total/len(score_list)
print("your average score is " + str(average))

###------------------------------------------------- HARD -------------------------------------------------###


# optional guess number challenge
#generate a random number, store it in the variable secret_number
import random
secret_number = random.randint(1, 99)
print("I am thinking of a number between 1 and 99…")

#get our first guess from the user
guess = int(input("Enter a guess: "))

# True if guess is not equal to secret number
while guess != secret_number:
   # True if guess is less than secret number
   if guess < secret_number:
      print("Your guess is too low")
   else:
      print("Your guess is too high")
   print("") # an empty line

   # get another guess from the user
   guess = int(input("Enter a new guess: "))

print("Congrats! The number was: " + str(secret_number))


print("Enter a sequence of non-decreasing numbers.")
current = int(input('Enter a number: '))
previous = -1
length = 0
while current > previous:
  length = length + 1
  previous = int(input('Enter a number: '))
  current = int(input('Enter a number: '))
  print('The length of the sequence is ' + length)