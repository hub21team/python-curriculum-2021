###------------------------------------------------- EASY -------------------------------------------------###

# Challenge1:
my_list = [32, "Sylvain", "Hub21", True, False, "6-18", 99.14, 1998, "11"]
# You are given a non-empty list named 'my_list'. Ask the user the index of the element he/she wants to reach and
# return the element at that index.
index = int(input("Which element do you want to see? "))
if index < len(my_list):
    print("The element is: ", my_list[index])
else:
    print("Index out of bounds.")

# Challenge2:
vegies = ["eggplant", "pepper", "orange", "artichoke","potato", "pumpkin", "strawberry"]
# Your sister wanted you to help with her homework. She is learning the vegetables and supposed to write down 7
# different vegetables. She wants you to check if she did everything correctly. First, remove the elements that are not
# vegetables. For every element you remove, you should add a new element to the list. Later, check the length of the
# list to make sure you have 7 elements. Finally, tell all the vegetables to your sister so that she can write them
# down.
vegies.remove("orange")
vegies.append("cauliflower")
vegies.remove("strawberry")
vegies.append("lettuce")
print("Number of vegetables in the list: ", len(vegies))
print("The vegetables: ", vegies)

# Challenge3:
my_guesses = [10, 20, 30, 40, 50, 60]
my_friends_guesses = [17, 28, 50, 23, 10, 38]
# You and your friend try to guess the price of a hat your other friend bought. You have 6 chances and when you use all
# your chances, your friend with the hat says that "You both guessed it correctly!". 'my_guesses' and
# 'my_friends_guesses' contains the guesses. Checking both lists, try to find which values can be the price of the hat.
for elt in my_guesses:
    if elt in my_friends_guesses:
        print(elt, "is in both lists, so it may be the price of the hat!")

# Challenge4:
user_1_info = []
user_2_info = []
# You created a new app to suggest people new friends. To provide a more satisfying experience, you need to take some
# information from users and store them. Take name, age, and the hometown from two different users and store their
# information in the lists given above. If users have at least one thing in common (name or age or hometown), suggest
# them to be friends.
name = input("Name? ")
user_1_info.append(name)
age = int(input("Age? "))
user_1_info.append(age)
hometown = input("Hometown? ")
user_1_info.append(hometown)

name = input("Name? ")
user_2_info.append(name)
age = int(input("Age? "))
user_2_info.append(age)
hometown = input("Hometown? ")
user_2_info.append(hometown)

if user_1_info[0] == user_2_info[0] or user_1_info[1] == user_2_info[1] or user_1_info[2] == user_2_info[2]:
    print(user_2_info[0], ", you may want to be friends with", user_1_info[0])

# Challenge5:
possible_colors = ["white", "red", "black", "green", "yellow", "beige"]
# You are renewing the house and you mom asked you to choose a color to paint you room. But there are too many
# possibilities! You narrowed down your possibilities to 'possible_colors' and decided to get help from your dad. You
# will ask him for a color to paint your room and if that color is inside your list, you will tell your mother to paint
# the room to that color. Otherwise, you will choose the last color in your list as the color to paint your room.

color = input("Dad, which color would be the best for my room? ")
if color in possible_colors:
    print("Mom, we should paint my room to", color)
else:
    print("Mom, we should paint my room to", possible_colors[-1])

###------------------------------------------------- MEDIUM -------------------------------------------------###

# Challenge1:
number_list = []
# Take 3 numbers from the user that are between 1-1000 and add them to the 'number_list'.
# Later, find the maximum number in the list.
num = int(input("Enter the first number: "))
number_list.append(num)
num = int(input("Enter the second number: "))
number_list.append(num)
num = int(input("Enter the third number: "))
number_list.append(num)

max_num = 0
for number in number_list:
    if number > max_num:
        max_num = number
print("The biggest number is ", max_num)

# Challenge2:
birthday_notes = []
# You are about to plan a birthday party for your best friend. First, you ask how many people are invited to the party,
# and then, what will be served at the party (cake or pizza). You will take notes and store your notes in the
# 'birthday_notes' list you have. Now, it's time to calculate how much money you need for the party food! If cake will
# be served, it is $10 / person, if pizza will be served, it is $7 / person. Also, beverage and other things will cost
# $50. Using only the birthday_notes, calculate how much money is needed for the birthday party.
num_guests = int(input("How many guests are invited? "))
birthday_notes.append(num_guests)
dish = input("Are we going to serve cake or pizza? ")
birthday_notes.append(dish)

total = 50
if birthday_notes[1] == "cake":
    total = 10 * birthday_notes[0]
elif birthday_notes[1] == "pizza":
    total = 7 * birthday_notes[0]
else:
    print("This food is not an option")
print("We will spend", total, "$ for the birthday.")

# Challenge3:
math_exam_notes = [92.8, 97]
# 'math_exam_notes' holds the grades for your first two math exams. To learn your final grade, you go to the teacher's
# office. First, ask your final grade and add it to your grade list. Later, find the average grade you will get from the
# course.
# Note: Your final grade does not have to be an integer.
final_grade = float(input("What is my final exam grade? "))
math_exam_notes.append(final_grade)
total_grades = 0
for elt in math_exam_notes:
    total_grades += elt
avg_grade = total_grades / len(math_exam_notes)
print("My average grade is:", avg_grade)

# Challenge4:
mixed = ["banana","apple","banana","apple","potato","carrot","potato","carrot","potato","carrot"]
# You have the mixed list, find how many vegetables and fruits there are in the mixed list and print it to
# the console.
vegies = ["potato","carrot"]
fruits = ["banana","apple"]

number_vegies = 0
number_fruits = 0

for loop in mixed:
  if loop in vegies:
    number_vegies = number_vegies + 1
  else:
    number_fruits = number_fruits + 1
print("there is", number_vegies, "of vegetables and", number_fruits, "of fruits.")


###------------------------------------------------- HARD -------------------------------------------------###

# Challenge1:
my_favorite_fruits = ["apple", "pear", "cherry", "banana"]
# You prepared an online test for your friends to see how well they know you. In one of the questions, you ask them to
# write one of your favorite fruits, all of which is listed in 'my_favorite_fruits'. If they know the answer,
# congragulate them and list your other favorite fruits. Otherwise, tell that they are wrong and list your favorite
# fruits one by one.
# Ex1: (if the answer is apple)
# Output1:
#   Correct! Here are the remaining fruits I like:
#   pear
#   cherry
#   banana

# Ex2: (if the answer is orange)
# Output2:
#   Not correct :(, possible answers are these:
#   apple
#   pear
#   cherry
#   banana
guess = input("Tell me one of my favorite fruits: ")
if guess in my_favorite_fruits:
    print("Correct! Here are the remaining fruits I like:")
    for elt in my_favorite_fruits:
        if guess != elt:
            print(elt)
else:
    print("Not correct :(, possible answers are these:")
    for elt in my_favorite_fruits:
        print(elt)



# Challenge2:
numbers = list(range(1, 1000))
special_numbers = []
# You are given the 'numbers' which contains the numbers from 1 to 1000. Special numbers are the ones having an integer
# square root. Find all the special numbers in 'numbers' and store them in special list. When you
# are finished, print special_numbers to the console.
for num in numbers:
  root = num**(0.5)
  if root == int(root):
    special_numbers.append(num)
print("Special numbers in range 1-1000: ", special_numbers)


# Challenge3:
topic_list = ["math", "french", "english", "arts", "sciences"]
# You have a friend who wants to do a job depending on the topic he/she likes. For all the topics in the 'topic_list',
# ask him/her if he/she likes the topic. After learning what he/she likes, for each topic he/she likes, suggest a job.
# Hint: You can use .index(elt) method to find the index of elt in the list.
job_list = ["Math Professor", "Tour guide", "Poet", "Painter", "Doctor"]
liked_topics = []
for topic in topic_list:
    question = "Do you like " + topic + "? "
    is_liked = input(question)
    if is_liked == "yes":
        liked_topics.append(topic)

for topic in liked_topics:
    index = topic_list.index(topic)
    job = job_list[index]
    print("You can be a ", job)