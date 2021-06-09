###------------------------------------------------- EASY -------------------------------------------------###

# Challenge1:
number_list = [1, 1, 9, 19, 28, 9, 9, 9, 30, 30, 12, 3, 12, 3, 12, 3, 4, 5, 11, 11]
# Find all the unique numbers in the list, print them and tell how many unique number there is. 
# Also, find the difference between the maximum and minimum number.
set1 = set(number_list)
max1 = max(set1)
min1 = min(set1)
difference = max1 - min1
print("The number of unique elements: ", len(set1))
print("Unique elements:", set1)
print("The difference is between min and max: ", difference)


# Challenge2:
# Note to the tutor: Please ask about his/her favorite series and add some of them to the 'netlix_tv_series' set beforehand.
netlix_tv_series = set(["Avatar the Last Airbender", "The Legend of Korra", "Sword Art Online", "Friends", "How I Met Your Mother?", "Rick and Morty"])
# You want to watch some of your favorite TV series again. Therefore, you decided to subscribe to Netflix if at least 2 of your 
# TV series are streamed. First, create a set of your favorite TV series and then if you decide to subscribe, tell your friends about 
# your decision.
my_fav_series = set(["Friends", "Master of None", "Westworld", "The Legend of Korra"])
if len(my_fav_series & netlix_tv_series) >= 2:
    print("I decided to subscribe to Netflix!")


###------------------------------------------------- MEDIUM -------------------------------------------------###

# Challenge1:
fruit_set = set(["cherry", "banana", "apple", "pear", "peach", "melon", "apricot", "orange", "lemon", "blackberry", "blueberry", "raspberry", "strawberry", "kiwi", "mango", "pineapple"])
vegie_set = set(["garlic", "onion", "artichokes", "broccoli", "cauliflower", "mushrooms", "lettuce", "spinach", "beetroot", "carrot", "celeriac", "turnip", "beans", "peas", "asparagus", "potatoes"])
# Your little sister is about to learn the different vegetables and fruits. 
# First, ask her what elements she wants to learn untiil she says that she is "bored". 
# Later, for all the unique elements she said, tell if it's a fruit or vegetable. 
sister_set = set()

product = input("Which vegie of fruit would you like to learn about? ")
while product != "bored":
  sister_set.add(product)
  product = input("Which vegie of fruit would you like to learn about? ")

for element in sister_set:
  if element in fruit_set:
    print(element, "is a fruit.")
  elif element in vegie_set:
    print(element, "is a vegetable.")
  else: 
    print("Sorry I don't know this element.", element)


# Challenge2:
# First create a set of your favorite activities. Also, you have two close friends and you want to do something 
# all together. Therefore, ask your first friend what she likes to do until she says "done". Later, do the same 
# for your second friend, and come up with what you can do together.
my_set = set(["playing basketball", "watching TV", "sleeping", "coding", "swimming"])
set1 = set()
activities = input("What is your favorite activity? ")
while not (activities == "done"):
  set1.add(activities)
  activities = input("What is your another favorite activity? ")

set2 = set()
activities = input("What is your favorite activity? ")
while not (activities == "done"):
  set2.add(activities)
  activities = input("What is your another favorite activity? ")

final_set = my_set & set1 & set2
print("We can do", final_set, "together")



###------------------------------------------------- HARD -------------------------------------------------###

# Challenge1:
market_1 = set(["cheese", "olive", "pepper", "tomato", "bread", "garlic", "beer"])
market_2 = set(["cake", "pasta", "ice cream", "brownie", "bread"])
# You will do the shopping for this week's groceries. You ask your mom to tell you what she needs for this week and take a note of each item. 
# Later, you go the the first market and buy all the things you can find there. If there is some items left in your grocery list, 
# you go to the second market and purchase it from there. Finally, when you go back home, tell your mother is you could not find some items 
# and how many markets you had to visit.
groceries_list = set()
element = input("What do I need to buy? ")
while not (element == "done"):
  groceries_list.add(element) 
  element = input("What do I need to buy next? ")

not_found_groceries = groceries_list.difference(market_1)
nb_market = 1

if len(not_found_groceries) != 0:
  not_found_groceries2 = not_found_groceries.difference(market_2)
  nb_market = 2
  if len(not_found_groceries2) != 0:
    print ("I could not find", not_found_groceries2)
print("I went to", nb_market, "markets")



###----------------------------------------------- OPTIONAL (TUPLES) -----------------------------------------------###


# Challenge1:
my_fav_sports = ["Swimming", "Tennis", "Volleyball", "Ice skating", "Running"]
my_friends_fav_sports = ["Ice skating", "Baseball", "Diving", "Fencing", "Sailing"]

common_sports = []
for sport in my_fav_sports:
  if sport in my_friends_fav_sports:
    common_sports.append(sport)
print("We can do", common_sports)
# When you go through your previous codes, you came across this one where you compare your and your friend's
# favorite sports to find out what you can do together. However, since you learned tuples, you know that for 
# some of the lists in this code, it is better to use tuples. Change your code accordingly.

my_fav = tuple(my_fav_sports)
friends_fav = tuple(my_friends_fav_sports)

common_sports = []
for sport in my_fav_sports:
  if sport in my_friends_fav_sports:
    common_sports.append(sport)
print("We can do", common_sports)

# Challenge2:
names = ["Tiffanie", "Merve", "Ece", "Nazir", "Berk", "Utku", "Gül Sena", "Meryem"]
associations = [[1, 1, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 0, 1, 1, 0],
                [0, 1, 1, 0, 1, 1, 0, 1],
                [0, 1, 1, 1, 1, 1, 0, 1],
                [0, 1, 1, 1, 0, 0, 1, 0],
                [0, 1, 0, 0, 1, 1, 0, 1]]
# You are given a list of names and associatons. associations list contains the information about
# people's relations. If one person knows the other, e.g. 2nd person in the list knows the 3rd person,
# associations[1][2] and  associations[2][1] will be 1, otherwise 0. You are writing a code where a user
# can ask if one person knows the other. Since users will use names, you have to first find their indices 
# in the list and then using those, you will obtain the results from associations. 
# You realized that you can use dictionaries and tuples to make your code more efficient. Utilize those 
# and names of persons to come up with a solution.
# Note: Since a person obviously knows himself/herself, do not include it in your dictionary. Also, if you 
# have a person X and person Y, if they know each other, you only need to add their relations once.
# Hint! tuples can be used as keys for a dictionary.
assoc_dict = {}
for i in range(len(names)):
  for j in range(len(names)):
    if i != j:
      if not ((names[i], names[j]) in assoc_dict or (names[j], names[i]) in assoc_dict):
        assoc_dict[(names[i], names[j])] = associations[i][j]

print("dict: ", assoc_dict)

person1 = input("Which person do you want to know about? ")
person2 = input("Relation with who? ")

if (person1, person2) in assoc_dict:
  if assoc_dict[(person1, person2)] == 1:
    print("They know each other")
  else:
    print("They don't know each other")
elif (person2, person1) in assoc_dict:
  if assoc_dict[(person2, person1)] == 1:
    print("They know each other")
  else:
    print("They don't know each other")
else:
  print("I have no info about", person1, "and", person2)