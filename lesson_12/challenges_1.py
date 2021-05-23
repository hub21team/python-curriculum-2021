from math import factorial
import math
import random
""" Easy """

""" Square root """
# x = float(input("Enter a number to take square root of: "))
# print(math.sqrt(x))

""" Calculate the perimeter of a circle """


def perimeter(r):
    perim = 2*math.pi*r
    # print("Perimeter is", perim)
    return perim


# radius = float(input("What is the radius of the wheel? "))
# print(perimeter(radius))

""" Medium """
""" Combination & Permutation Formulas """


def my_factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result


def my_combination(n, k):
    return my_factorial(n) / (my_factorial(k)*my_factorial(n-k))


def my_permutation(n, k):
    return my_factorial(n) / my_factorial(n-k)


def combination(n, k):
    return factorial(n) / (factorial(k)*factorial(n-k))


def permutation(n, k):
    return factorial(n) / factorial(n-k)


# print(combination(3, 2))

""" Hard """


def guess_the_number():
    my_number = random.randint(1, 20)
    print("Welcome to guess the number game, let's play...")
    guess = int(input("What is your guess? "))
    while guess != my_number:
        if guess < my_number:
            print("Go higher.")
        elif guess > my_number:  # here else also works
            print("Go lower.")
        guess = int(input("What is your next guess? "))
    print("Congratulations, my number was indeed", my_number)


# guess_the_number()

""" Pick a random person and ask them a random question """
people = ["Ece", "Gül Sena", "Haldun", "Haydar", "Merve", "Nazir", "Sylvain"]
questions = ["How old are you?", "Where are you from?",
             "What is you favorite color?", "Do you have any siblings?"]


def break_the_ice():
    for i in range(5):
        person = random.choice(people)
        question = random.choice(questions)
        print("Hey,", person, question)


break_the_ice()

""" bingo """


def announce_winner(player1_numbers, player2_numbers):
    if len(player1_numbers) > 0:
        print("Player 2 won.")
    elif len(player2_numbers) > 0:
        print("Player 1 won.")
    else:
        print("It's a tie!")


def play_bingo(player1_numbers, player2_numbers):
    while len(player1_numbers) > 0 and len(player2_numbers) > 0:
        next_num = random.randint(1, 10)
        print("The number drawn from the bag is", next_num)
        if next_num in player1_numbers:
            print("Player 1 has the number.")
            player1_numbers.remove(next_num)
        if next_num in player2_numbers:
            player2_numbers.remove(next_num)
            print("Player 2 has the number.")
    announce_winner(player1_numbers, player2_numbers)


def bingo():
    print("Alright, let's play bingo! I am going to assign your cards now:")
    # prepare the boards
    player1_hand = random.sample(range(1, 11), 6)  # [1, 3, 2, 9, 8, 4]
    player2_hand = random.sample(range(1, 11), 6)  # [4, 7, 6, 10, 1]
    print("Player 1, your card is as follows: ", player1_hand)
    print("Player 2, your card is as follows: ", player2_hand)
    play_bingo(player1_hand, player2_hand)


bingo()
