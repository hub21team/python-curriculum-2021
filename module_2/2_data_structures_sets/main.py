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
produce = input("Which vegie of fruit would you like to learn about?")
while not (produce == "bored"):
  sister_set.add(produce)
  produce = input("Which vegie of fruit would you like to learn about?")

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



