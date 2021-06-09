###------------------------------------------------- EASY -------------------------------------------------###

# Challenge1:
ages_of_recorded_users = {"Merve": 22, "Ece": 23, "Meryem": 20, "Arda": 25, "Berke": 8}
# You stored the ages of your app's users as given above. However, two years passed and you realized that you did 
# not write a code that updates people's ages. Now, you have to correct the peoples age before you integrate a 
# new feature to your app.
# Print the changed dictionary to console to see the new ages.
for key in ages_of_recorded_users:
  ages_of_recorded_users[key] = ages_of_recorded_users[key] + 2
print(ages_of_recorded_users)


# Challenge2:
# You have met with a new person! As always, when you meet for the first time, you ask some questions. 
# To simulate the meeting, ask him/her about his/her name, surname, age, and favorite food. 
# Later, you tell your best friend about your new friend. She asks you one question about him/her. 
# If you know the answer, you should say it. Otherwise, tell your best friend that you do not know the answer.
info_dict = {}
info_dict["name"] = input("What is your name? ")
info_dict["surname"] = input("What is your surname? ")
info_dict["age"] = int(input("How old are you? "))
info_dict["favorite_food"] = input("What is your favorite food? ")

question = input("What do you want to know about my new friend? ")
if question in info_dict:
  print(info_dict[question])
else:
  print("I don't know about", question)


###------------------------------------------------- MEDIUM -------------------------------------------------###

# Challenge1:
# Ice cream example using dictionaries instead of lists.
# You own an ice-cream shop. The flavors are chocolate, vanilla, strawberry, and cookie. Their prices are 4, 3, 3, and 2 $, respectively. 
# When someone comes to your shop, you greet them first and you ask them how many scoops of ice cream they want. 
# Later, you ask them the flavors one by one. When you finish asking, you should tell the total price they will pay.
flavor_dict = {"chocolate": 4, "vanilla": 3, "strawberry": 3, "cookie": 2}
total_price = 0
while True:
  flavor = input("Hello, what flavor do you want?")
  if flavor == "exit":
    break
  total_price += flavor_dict[flavor]
print ("You should pay", total_price)


# Challenge2:
my_friends_favorites = {"Leyla" : {"movie" : "Harry Potter", "series": "Chilling Adventures of Sabrina", "color": "blue"},
                        "Selin" : {"movie" : "Star Wars", "series": "Rick and Morty", "color": "pink"},
                        "Didem" : {"movie" : "The Green Mile", "series": "Avatar", "color": "white"},
                        "Nazir" : {"movie" : "The Mask of Zorro", "series": "Attack on Titan", "color": "turquoise"}}
# You are a thoughtful friend and you keep notes about your friends to get them the best present for their birthdays! 
# However, people's preferences may change after a while. Write a code that helps you change your 'my_friends_favorites'.
# First, you should ask which user you want to change, then which info you want to change about him/her, and update the user.
# If the name is not in 'my_friends_favorites', you should ask all the info and add it to your dictionary. Finally, output the 
# final dictionary to the console.

key = input("Which user do you want to add/change? ")
if key in my_friends_favorites:
  key2 = input("Which info do you want to change? ")
  if key2 in my_friends_favorites[key]:
    val = input("What is the new favorite? ")
    my_friends_favorites[key][key2] = val
  else:
    print("Sorry, it is not recorded so you cannot change it")
else:
  movie = input("Favorite movie? ")
  series = input("Favorite series? ")
  color = input("Favorite color? ")
  my_friends_favorites[key] = {"movie" : movie, "series": series, "color": color}

# Challenge 3:
mixed_dict = {
  "first": 10, 
  "val": True, 
  "second": 134.23, 
  "name": "Merve", 
  "list": [1, 2, 3], 
  "num": 34}
# For the mixed dictionary above, increase the value by one if the value is an integer or float, 
# add "changed" to the end if it's a string, and reverse the truth value if it's a boolean. Otherwise, 
# do not change the elements. When finished print the updated dictionary and number of changes.
nb_changes = 0
for key in mixed_dict: 
  val = mixed_dict[key]
  if type(val) == int or type(val) == float:
    val += 1
    nb_changes += 1
  elif type(val) == str:
    val += "changed"
    nb_changes += 1
  elif type(val) == bool:
    val = not val
    nb_changes += 1
  mixed_dict[key] = val

print("Number of changes:", nb_changes)
print("Updated dictionary: ", mixed_dict)



###------------------------------------------------- HARD -------------------------------------------------###

# Challenge1:
# Create a dictionary that has the keys countries and values their capital. Ask the user which country's capital 
# she wants to know and tell it to her. If she says "all", you should print all the countries and their capitals. 
# If she says "add", you should ask for the key and value, and add it to the dictionary. If she says "delete", you 
# should delete the key-value pair from dictionary if it exists. Continue until the user says "done" or  "exit".
# Note: Be careful, the country she asks may not be in the list!
countries_dict = {"France": "Paris", "Portugal": "Lisbon", "Spain": "Madrid", "Italy": "Rome", "Germany": "Berlin", "Greece": "Athens", "UK": "London", "Mexico": "Mexico city", "Brazil": "Brasilia"}

while True:
  country = input("Which country's capital do you want to know? ")
  if country == "all":
    for country in countries_dict:
      print("The capital of", country, "is", countries_dict[country])
  elif country == "add":
    add_country = input("What country would you like to add? ")
    add_capital = input("What is its capital? ")
    countries_dict[add_country] = add_capital
  elif country == "delete":
    country_to_delete = input("Which country do you want to delete? ")
    countries_dict.pop(country_to_delete)
  elif country == "exit" or country == "done":
    break
  elif country in countries_dict:
    print(countries_dict[country])
  else:
    print("Sorry, I don't know this country.")
