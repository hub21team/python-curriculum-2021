###------------------------------------------------- EASY -------------------------------------------------###

# Challenge1:
# Ask user to input a string and an index. Print the character at the given index to the console.
str1 = input("Enter a string: ")
index = int(input("Enter an index: "))
if index < len(str1):
    print(str1[index])
else:
    print("Index out of bounds")


# Challenge2:
# For the numbers up to 5, print the number, its square root, and number * (number + 1) in the same line.
for i in range(5):
    num_sqrt = i ** 0.5
    times = i * (i + 1)
    print("Number:", i, "Sqrt:", num_sqrt, "number * (number + 1):", times)


# Challenge3:
# You are playing a game with 2 of your friends. Your first friend tell you a sentence secretly, and your second friend
# tries to guess a word from that sentence. You should let your second friend know if he/she finds a word.
sentence = input("What is the secret sentence? ")
sentence = sentence.lower()

word = input("Guess a word from the secret sentence: ")
word = word.lower()
search = sentence.find(word)
if search >= 0:
    print("You guessed it!")
else:
    print("Sorry, not correct :(")

###------------------------------------------------- MEDIUM -------------------------------------------------###

# Challenge1:
# Your little sister is doing her math homework that requires her to sum the digits in a given number for 3 different
# numbers. You don't have time to check all her answers; so you decide to come up with a code where she enters the
# number and you return the sum of digits inside.
# 198 -> (1 + 9 + 8) = 18
for i in range(3):
    total = 0
    number = input("What is the number?:")
    for digit in number: # 198 -> "198"
      total = total + int(digit)
    print("Sum of numbers in", number, "is = ", total)


# Challenge2: 
# Ask the user to input a number ind tell if the number is prime or not.
x = int(input("Enter a number: "))
prime = True
for num in range(2, int(x**(1/2) + 1)):
    if x % num == 0:
        print("The number is not a prime")
        prime = False
        break
if prime:
  print("The number is prime")


# Challenge3: 
# Ask the user for a sentence to be converted to English letters. If there are any characters that are in
# Turkish alphabet and not in English aplhabet, you should convert them, e.g, ı -> i, ü -> u.
st = input("Enter a string ")
st = st.replace("ı","i")
st = st.replace("ü","u")
st = st.replace("ğ","g")
st = st.replace("ö","o")
st = st.replace("ç","c")
st = st.replace("ş","s")
print(st)


# Challenge4: 
# You are trying to write a sentence in reverse but it may be hard sometimes. Therefore, you decide to write
# a program that can reverse a sentence you enter!
st = input("The sentence to reverse: ")
rev = ""
for idx in range(len(st)):
    rev += st[len(st)-1-idx]
print(rev)


# Challenge5: 
# You are trying to find if there is two consecutive letters that are the same in a given sentence. Ask for
# a sentence from the user and output the indices that are consecutive and contains the same letter.
str1 = input("Enter a sentence to be searched: ")
for i in range(1, len(str1)):
    if str1[i] == str1[i-1]:
        print("The indices", str(i-1), str(i), " are the same letter: ", str1[i])

###------------------------------------------------- HARD -------------------------------------------------###

# Challenge1:
# You own an ice-cream shop. The flavors are chocolate, vanilla, strawberry, and cookie. Their prices are 4, 3, 3, and
# 2 $, respectively. When someone comes to your shop, you greet them first and you ask them how many scoops of ice
# cream they want. Later, you ask them the flavors one by one. When you finish asking, you should tell the total price
# they will pay.
#Hint! You can make use of lists and you can use .index(elt) method to find the index of elt in a list.
flavors_list = ["chocolate", "vanilla", "strawberry",  "cookie"]
price_list = [4, 3, 3, 2]
total_price = 0

num_of_flavors = int(input("Welcome! How many scoops of ice cream do you want? "))
for i in range(num_of_flavors):
    flavor = input("Which flavor do you want? ")
    index = flavors_list.index(flavor)
    total_price += price_list[index]
print("You should pay $", total_price)

# Challenge2:
# Take an input string from the user and take two indices i and j. Swap the characters of the string that are at the
# ith and jth indices. Print the new string to console with all lower-case letters.
str1 = input("Enter a string: ")
i = int(input("Enter the first index: "))
j = int(input("Enter the second index: "))

str1 = str1.lower()
new_str = str1[0:i] + str1[j] + str1[i+1:j] + str1[i] + str1[j+1:]
print(new_str)