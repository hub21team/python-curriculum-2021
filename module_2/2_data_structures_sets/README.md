# Concepts

- Sets

  - empty set
    ```
    first_empty_set = set()
    ```
  - non-empty set with pre-defined elements
    ```
    first_set = set([22, "Hello", 14.09, "7-17"])
    ```
  - Access elements
    ```
    elt in first_set
    ```
    **Note** Indexing cannot be used for sets
  - Add / Remove
    ```
    first_set.add(11)
    first_set.remove("Hello")
    first_set.discard(22)
    first_set.pop()
    first_set.clear()
    ```
  - Iteration on sets using loops

    ```
    for elt in first_set:
        # do sth here
    ```

  - Other operations
    ```
    .intersection()
    .difference()
    | (or - union)
    & (and - intersection)
    ...
    ```

## Optional

- Tuples
  - empty tuple
    ```
    first_empty_tuple = ()
    ```
  - non-empty tuple
    ```
    first_tuple = ("Hub", "21")
    second_tuple = tuple([2021, 17, 21, "Hey"])
    third_tuple = ((1, 2, 3), "Python", ("a", "b"))
    ```
  - unpacking
    ```
    str1, str2 = first_tuple
    ```
  - indexing
    ```
    first_elt = second_tuple[0]
    c, d = second_tuple[1:3]
    ```

# Teaching Tips

- **How to explain sets?**
  Previously, the student learned about lists. Therefore, it may be a good starting point to compare the lists to sets and tell the avdantages and differences. Unlike lists, sets are unordered; therefore, we cannot use index as we did in lists. Most importantly, sets have no duplicate elements. You may explain the importance of containing no duplicates through real life examples such as grocery list, or invited guest lists.
  You may ask the student to add the same element again and check the behavior of the set. Also, you may show what happens when you discard/remove an element that is not in the set.

- **How to explain tuples?**
  They are almost like lists but immutable, meaning that they cannot be changed while lists can be changed. Suggest student to try the following code and find out the reason of error together:
  ```
  second_tuple[2] = 24
  ```
  If you can use tuples instead of lists, you should do it! Because tuples have many advantages:
  - access to elements are better
  - consumes less space in memory
  - iterations may be faster
    However, if you need to delete or change elements, using lists may be a better idea!
  ```
  import timeit
  print(timeit.timeit('x=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)', number=500000))
  print(timeit.timeit('x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]', number=500000))
  ```

# Challenges

## EASY

### Challenge1:

```
number_list = [1, 1, 9, 19, 28, 9, 9, 9, 30, 30, 12, 3, 12, 3, 12, 3, 4, 5, 11, 11]
```

Find all the unique numbers in the list, print them and tell how many unique number there is.
Also, find the difference between the maximum and minimum number.

### Challenge2:

**Note:** Please ask about his/her favorite series and add some of them to the 'netlix_tv_series' set beforehand.

```
netlix_tv_series = set(["Avatar the Last Airbender", "The Legend of Korra", "Sword Art Online", "Friends", "How I Met Your Mother?", "Rick and Morty"])
```

You want to watch some of your favorite TV series again. Therefore, you decided to subscribe to Netflix if at least 2 of your TV series are streamed. First, create a set of your favorite TV series and then if you decide to subscribe, tell your friends about your decision.

## MEDIUM

### Challenge1:

```
fruit_set = set(["cherry", "banana", "apple", "pear", "peach", "melon", "apricot", "orange", "lemon", "blackberry", "blueberry", "raspberry", "strawberry", "kiwi", "mango", "pineapple"])
vegie_set = set(["garlic", "onion", "artichokes", "broccoli", "cauliflower", "mushrooms", "lettuce", "spinach", "beetroot", "carrot", "celeriac", "turnip", "beans", "peas", "asparagus", "potatoes"])
```

Your little sister is about to learn the different vegetables and fruits. First, ask her what elements she wants to learn untiil she says that she is "bored". Later, for all the unique elements she said, tell if it's a fruit or vegetable.

### Challenge2:

First create a set of your favorite activities. Also, you have two close friends and you want to do something all together. Therefore, ask your first friend what she likes to do until she says "done". Later, do the same for your second friend, and come up with what you can do together.

## HARD

### Challenge1:

```
market_1 = set(["cheese", "olive", "pepper", "tomato", "bread", "garlic", "beer"])
market_2 = set(["cake", "pasta", "ice cream", "brownie", "bread"])
```

You will do the shopping for this week's groceries. You ask your mom to tell you what she needs for this week and take a note of each item. Later, you go the the first market and buy all the things you can find there. If there is some items left in your grocery list, you go to the second market and purchase it from there. Finally, when you go back home, tell your mother is you could not find some items and how many markets you had to visit.

## Tuple Challenges

### Challenge1:

```
my_fav_sports = ["Swimming", "Tennis", "Volleyball", "Ice skating", "Running"]
my_friends_fav_sports = ["Ice skating", "Baseball", "Diving", "Fencing", "Sailing"]

common_sports = []
for sport in my_fav_sports:
  if sport in my_friends_fav_sports:
    common_sports.append(sport)
print("We can do", common_sports)
```

When you go through your previous codes, you came across this one where you compare your and your friend's favorite sports to find out what you can do together. However, since you learned tuples, you know that for some of the lists in this code, it is better to use tuples. Change your code accordingly.

### Challenge2:

```
names = ["Tiffanie", "Merve", "Ece", "Nazir", "Berk", "Utku", "Gül Sena", "Meryem"]
associations = [[1, 1, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 0, 1, 1, 0],
                [0, 1, 1, 0, 1, 1, 0, 1],
                [0, 1, 1, 1, 1, 1, 0, 1],
                [0, 1, 1, 1, 0, 0, 1, 0],
                [0, 1, 0, 0, 1, 1, 0, 1]]
```

You are given a list of names and associatons. associations list contains the information about people's relations. If one person knows the other, e.g. 2nd person in the list knows the 3rd person, `associations[1][2]` and `associations[2][1]` will be 1, otherwise 0. You are writing a code where a user can ask if one person knows the other. Since users will use names, you have to first find their indices in the list and then using those, you will obtain the results from associations. You realized that you can use dictionaries and tuples to make your code more efficient. Utilize those and names of persons to come up with a solution.  
**Note:** Since a person obviously knows himself/herself, do not include it in your dictionary. Also, if you have a person X and person Y, if they know each other, you only need to add their relations once.  
**Hint!** tuples can be used as keys for a dictionary.

# Extra Scenarios
