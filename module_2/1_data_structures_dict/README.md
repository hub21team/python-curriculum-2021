# Concepts

- Dictionaries
  - empty dictionary
    ```
    first_empty_dict = {}
    second_empty_dict = dict()
    ```
  - non-empty dictionary with pre-defined pairs
    ```
    first_dict = {1: "Hub21", 2: "Didem", 3: "Python"}
    second_dict = dict({1: "Hub21", 2: "Didem", 3: "Python"})
    ```
- Access elements
  ```
  str1 = first_dict[1]
  print(first_dict[2])
  ```
- Add / Remove / Change
  ```
  first_dict["new_key"] = 34
  del first_dict[3]
  elt = first_dict.pop("new_key") # try diff keys and observe the behavior
  first_dict[1] = "HUB21"
  ```
- Iteration on dictionaries using loops
  - iteration over key
    ```
    for key in first_dict:
        print(key)
    ```
  - iteration over value
    ```
    for val in first_dict.values():
        print(val)
    ```
  - iteration over key, value pairs
    ```
    for key, val in first_dict.items():
        print(key, "is", val)
    ```
- Nested Dictionaries
  ```
  first_dict["info_dict"] = {"name": Berkay, "job": "Developer"}
  ```

# Teaching Tips

- **How to explain dictionaries?**
  Previously, the student learned about lists. Therefore, it may be a good starting point to compare the lists to dictionaries and tell the avdantages and differences. Dictionaries are unordered; therefore, we cannot use index as we did in lists. However, we have keys to access values (key-value pairs), which can be more useful than lists.

# Challenges

## EASY

### Challenge1:

```
ages_of_recorded_users = {"Merve": 22, "Ece": 23, "Meryem": 20, "Arda": 25, "Berke": 8}
```

You stored the ages of your app's users as given above. However, two years passed and you realized that you did not write a code that updates people's ages. Now, you have to correct the peoples age before you integrate a new feature to your app. Print the changed dictionary to console to see the new ages.

### Challenge2:

You have met with a new person! As always, when you meet for the first time, you ask some questions. To simulate the meeting, ask him/her about his/her name, surname, age, and favorite food. Later, you tell your best friend about your new friend. She asks you one question about him/her. If you know the answer, you should say it. Otherwise, tell your best friend that you do not know the answer.

## MEDIUM

### Challenge1:

Ice cream example using dictionaries instead of lists. You own an ice-cream shop. The flavors are chocolate, vanilla, strawberry, and cookie. Their prices are 4, 3, 3, and 2 $, respectively. When someone comes to your shop, you greet them first and you ask them how many scoops of ice cream they want. Later, you ask them the flavors one by one. When you finish asking, you should tell the total price they will pay.

### Challenge2:

```
my_friends_favorites = {
  "Leyla" : {"movie" : "Harry Potter", "series": "Chilling Adventures of Sabrina", "color": "blue"},
  "Selin" : {"movie" : "Star Wars", "series": "Rick and Morty", "color": "pink"},
  "Didem" : {"movie" : "The Green Mile", "series": "Avatar", "color": "white"},
  "Nazir" : {"movie" : "The Mask of Zorro", "series": "Attack on Titan", "color": "turquoise"}}
```

You are a thoughtful friend and you keep notes about your friends to get them the best present for their birthdays! However, people's preferences may change after a while. Write a code that helps you change your 'my_friends_favorites'. First, you should ask which user you want to change, then which info you want to change about him/her, and update the user. If the name is not in 'my_friends_favorites', you should ask all the info and add it to your dictionary. Finally, output the final dictionary to the console.

### Challenge3:

```
mixed_dict = {
  "first": 10,
  "val": True,
  "second": 134.23,
  "name": "Merve",
  "list": [1, 2, 3],
  "num": 34}
```

For the mixed dictionary above, increase the value by one if the value is an integer or float, add "changed" to the end if it's a string, and reverse the truth value if it's a boolean. Otherwise, do not change the elements. When finished print the updated dictionary and number of changes.

## HARD

### Challenge1:

Create a dictionary that has the keys countries and values their capital. Ask the user which country's capital she wants to know and tell it to her. If she says "all", you should print all the countries and their capitals. If she says "add", you should ask for the key and value, and add it to the dictionary. If she says "delete", you should delete the key-value pair from dictionary if it exists. Continue until the user says "done" or "exit".  
**Note:** Be careful, the country she asks may not be in the list!

# Extra Scenarios
