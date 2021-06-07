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

# Extra Scenarios
