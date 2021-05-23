# Concepts

- List definition
  - empty list
  - non-empty list
- Indexing
- Add / Delete
- Length
- Iteration on lists using loops
  - introduction to for loop

# Teaching Tips

- **How to explain lists?**
  It is crucial for the student to grasp the idea of lists and what they are used for. You can
  use variables to teach lists. As they learned previously, variables can store a piece of information. However, what if
  you need to store multiple pieces of information? Are you going to create thousands of variables? Instead, you can use
  lists which can store multiple bits of information.

- **How to explain for loop?**
  Since they will learn to apply multiple operations on the elements of lists, you can focus
  on the idea of applying multiple operations to some or each element of the list. For instance, are they going to write
  many lines of code if they want to print each element + 2 in a 20 element list? Let them think for a while and
  introduce the idea of iterating over elements one by one and the syntax of the for loop.

# Challenges

## EASY

### Challenge1:

```
my_list = [32, "Sylvain", "Hub21", True, False, "6-18", 99.14, 1998, "11"]
```

You are given a non-empty list named _my_list_. Ask the user the index of the element he/she wants to reach and return the element at that index.

### Challenge2:

```
vegies = ["eggplant", "pepper", "orange", "artichoke","potato", "pumpkin", "strawberry"]
```

Your sister wanted you to help with her homework. She is learning the vegetables and supposed to write down 7 different vegetables. She wants you to check if she did everything correctly. First, remove the elements that are not vegetables. For every element you remove, you should add a new element to the list. Later, check the length of the list to make sure you have 7 elements. Finally, tell all the vegetables to your sister so that she can write them down.

### Challenge3:

```
my_guesses = [10, 20, 30, 40, 50, 60]
my_friends_guesses = [17, 28, 50, 23, 10, 38]
```

You and your friend try to guess the price of a hat your other friend bought. You have 6 chances and when you use all your chances, your friend with the hat says that "You both guessed it correctly!". _my_guesses_ and _my_friends_guesses_ contains the guesses. Checking both lists, try to find which values can be the price of the hat.

### Challenge4:

```
user_1_info = []
user_2_info = []
```

You created a new app to suggest people new friends. To provide a more satisfying experience, you need to take some information from users and store them. Take name, age, and the hometown from two different users and store their information in the lists given above. If users have at least one thing in common (name or age or hometown), suggest them to be friends.

### Challenge5:

```
possible_colors = ["white", "red", "black", "green", "yellow", "beige"]
```

You are renewing the house and you mom asked you to choose a color to paint you room. But there are too many possibilities! You narrowed down your possibilities to _possible_colors_ and decided to get help from your dad. You will ask him for a color to paint your room and if that color is inside your list, you will tell your mother to paint the room to that color. Otherwise, you will choose the last color in your list as the color to paint your room.

## MEDIUM

### Challenge1:

```
number_list = []
```

Take 3 numbers from the user that are between 1-1000 and add them to the 'number_list'. Later, find the maximum number in the list.

### Challenge2:

```
birthday_notes = []
```

You are about to plan a birthday party for your best friend. First, you ask how many people are invited to the party, and then, what will be served at the party (cake or pizza). You will take notes and store your notes in the _birthday_notes_ list you have. Now, it's time to calculate how much money you need for the party food! If cake will be served, it is $10 / person, if pizza will be served, it is $7 / person. Also, beverage and other things will cost $50. Using only the _birthday_notes_, calculate how much money is needed for the birthday party.

### Challenge3:

```
math_exam_notes = [92.8, 97]
```

_math_exam_notes_ holds the grades for your first two math exams. To learn your final grade, you go to the teacher's office. First, ask your final grade and add it to your grade list. Later, find the average grade you will get from the course.
**Note:** Your final grade does not have to be an integer.

### Challenge4:

```
mixed = ["banana","apple","banana","apple","potato","carrot","potato","carrot","potato","carrot"]
```

You have the _mixed_ list, find how many vegetables and fruits there are in the mixed list and print it to the console.

## HARD

### Challenge1:

```
my_favorite_fruits = ["apple", "pear", "cherry", "banana"]
```

You prepared an online test for your friends to see how well they know you. In one of the questions, you ask them to write one of your favorite fruits, all of which is listed in _my_favorite_fruits_. If they know the answer, congragulate them and list your other favorite fruits. Otherwise, tell that they are wrong and list your favorite fruits one by one.

Ex1: (if the answer is apple)  
Output1:

> Correct! Here are the remaining fruits I like:  
>  pear  
>  cherry  
>  banana

Ex2: (if the answer is orange)  
Output2:

> Not correct :(, possible answers are these:  
>  apple  
>  pear  
>  cherry  
>  banana

### Challenge2:

```
numbers = list(range(1, 1000))
special_numbers = []
```

You are given the _numbers_ which contains the numbers from 1 to 1000. Special numbers are the ones having an integer square root. Find all the special numbers in _numbers_ and store them in _special_numbers_ list. When you are finished, print _special_numbers_ to the console.

### Challenge3:

```
topic_list = ["math", "french", "english", "arts", "sciences"]
```

You have a friend who wants to do a job depending on the topic he/she likes. For all the topics in the _topic_list_, ask him/her if he/she likes the topic. After learning what he/she likes, for each topic he/she likes, suggest a job.  
**Hint:** You can use _.index(elt)_ method to find the index of elt in the list.

# Extra Scenarios

**Understanding the for loop syntax:** One of the things that may be hard for a child to grasp is to syntax of the for
loop. When you write "for item in some_list", they may have the idea that they have to write "item" whenever they use
the for loop. You may want to emphasize that item is a temporary variable that holds the value of the element in that
iteration. Therefore, they can name it whatever they like, but it is better if they use an appropriate name :).
