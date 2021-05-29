# Guess Game

import random

print("Hello, What's your name?")
name = input()
name2 = name.capitalize()
range_nums = input("Enter the start and end values seperated with a space: ")
start_value = int(range_nums.split()[0])
end_value = int(range_nums.split()[1])
print("Hello", name2, "! I am thinking of a number between", start_value, "and", end_value, "guess what number it is!")

number = random.randint(start_value, end_value)
guess = int(input("Guess: "))
count = 1

while not (number == guess):
  count += 1
  if guess>number:
    print("Your guess is too high")
    guess = int(input("Guess: "))
  elif guess<number:
    print("Your guess is too low")
    guess = int(input("Guess: "))


print("You got it correct!", name2)
print("You guessed the number in", count, "tries!")



# Rock, Paper, Scissors

import random

options = ["rock", "paper", "scissors"]


def result(choice1, choice2):
    if choice1 == choice2:
        return "tie"
    if choice1 == "rock":
        if choice2 == "paper":
            return choice2
        if choice2 == "scissors":
            return choice1
    if choice1 == "paper":
        if choice2 == "rock":
            return choice1
        if choice2 == "scissors":
            return choice2
    if choice1 == "scissors":
        if choice2 == "paper":
            return choice1
        if choice2 == "rock":
            return choice2


player_score = 0
computer_score = 0

for i in range(1, 11):
    player = input("Pick rock, paper, or scissors: ")
    index = random.randint(0, 2)
    computer = options[index]
    print("computer chose", computer)

    if result(player, computer) == "tie":
        print("it's a tie!")
    elif result(player, computer) == player:
        player_score += 1
        print("You win!")
    elif result(player, computer) == computer:
        computer_score += 1
        print("You lose!")

    print()
    print("player:", player_score, "computer:", computer_score)
    print()

if player_score > computer_score:
    print("You won the game!")
elif player_score < computer_score:
    print("You lost the game!")
else:
    print("A tie!")

# Ancient Game of Nimm

player = 1
stones = 20
while stones > 0:
    print('There are {stones} stones left')
    amount = int(input('Player {player} would you like to remove 1 or 2 stones? '))
    while amount != 1 and amount != 2:
        amount = int(input('Please enter 1 or 2: '))
        print()
        stones -= amount
        if player == 1:
            player = 2
        else:
            player = 1
        print('Player {player} wins!')

# Hailstones

num = int(input("Enter number "))
steps = 0
while True:
    steps = steps+1
    if num % 2 != 0:
        print(num, "is odd , so i make 3n+1:", num*3 +1)
        num = num*3 + 1
    elif num % 2 == 0:
        print(num, "is even , so i take half:", num/2)
        num = num/2
    if num == 1:
        print("the process took", steps, "steps", "to reach 1")
        break


# Die Question

import random

results = []
average = []

for j in range(1,100):
  for i in range(1,100):
    side = random.randint(1,6)

    results.append(side)

    if 1 in results and 2 in results and 3 in results and 4 in results and 5 in results and 6 in results:
      results = []
      average.append(i)
      break

total = 0

for num in average:
  total += num

print(total/len(average))