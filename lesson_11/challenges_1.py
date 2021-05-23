""" easy """


def greet_single_student(name):
    print("Hello,", name, "! Welcome to our class.")


""" toast for the alien """


def greet_alien():
    print("Hello, my name is Gül Sena.\nI will teach you to make a toast")


def describe_ingredient(ingredient_name, description):
    print("Now, I am going to explain", ingredient_name, "to you.")
    print(description)


def take_ingredient_from_refrigerator(ingredient_name):
    print("Open the refrigerator.")
    print("Now take", ingredient_name)


def prepare():
    describe_ingredient("bread", "Bread is the soft spongelike rectangle.")
    describe_ingredient("cheese", "Cheese is the mushy solid rectangle.")
    describe_ingredient(
        "knife", "Knife is the object on the counter with sharp edges, be careful.")
    take_ingredient_from_refrigerator("bread")
    take_ingredient_from_refrigerator("cheese")


def cut_and_place(ingredient):
    print("Use the knife to cut a thin slice of", ingredient)
    print("Put", ingredient, " on the plate")


def make_toast():
    cut_and_place("bread")
    cut_and_place("cheese")
    cut_and_place("bread")


def teach_toast_making():
    greet_alien()
    prepare()
    make_toast()


# teach_toast_making()
""" medium """
""" 
Write a program that greets students in the class. Your program should take student names as input until user prompts empty string ''. 
"""


def greet_students():
    student_name = input("What is your name? ")
    while student_name != '':
        greet_single_student(student_name)
        student_name = input("What is your name? ")
    print("Let's start the class")


greet_students()

""" Compare to 5 and print """


def compare_to_5(a):
    if a < 5:
        print(a, " is less than 5")
    elif a > 5:
        print(a, " is greater than 5")
    else:
        print("They are equal!")


compare_to_5(-1)
compare_to_5(999)
compare_to_5(5)

""" Compare two numbers and print """


def compare(a, b):
    if a < b:
        print(a, " is less than", b)
    elif a > b:
        print(a, " is greater than", b)
    else:
        print("They are equal!")


compare(1, 9)
compare(1, -99)
compare(3, 3)

""" Write a function average_of_list(lst) that prints the average of a list of numbers. """


def average_of_list(lst):
    sum = 0
    for num in lst:
        sum += num
    return sum / len(lst)


average_of_list([1, 3, 4])
""" hard """
""" mama's bakery """


def mamas_bakery(total_slices, slice_price):
    print("Welcome to Mama's bakery, İstanbul! Today's special menu item is our lemon cheesecake.")
    while total_slices > 0:
        to_sell = int(input("Greetings, we have "+str(total_slices) +
                            " units left of our cheesecake. How many units would you like to buy? "))
        if to_sell > total_slices:
            to_sell = total_slices
            print("Excuse me, I will only be able to sell",
                  to_sell, "slices to you.")
        print("That would be", to_sell*slice_price, " TLs.")
        total_slices -= to_sell
    print("Thank you, we are out of cheesecakes, we will see you next time!")


mamas_bakery(10, 10)


""" mama's bakery v2 """
def sell_item(item, total_units, unit_price):
    while total_units > 0:
        to_sell = int(input("Greetings, we have " + str(total_units) +
                            " left of our " + str(item) + ". How many units would you like to buy? "))
        if to_sell > total_units:
            to_sell = total_units
            print("Excuse me, I will only be able to sell",
                  to_sell, "units to you.")
        total_units -= to_sell

        print("That would be", to_sell*unit_price, " TLs.")


def mamas_bakery_v2(items, total_units, unit_prices):
    print("Welcome to Updated Mama's bakery, İstanbul! Today's special menu items are", items)
    for i in range(len(items)):
        print("\nNow selling", items[i])
        sell_item(items[i], total_units[i], unit_prices[i])
    print("Thank you, we are out of cheesecakes, we will see you next time!")


items = ["lemon cheesecake", "apple pie", "cookies"]
total_units = [10, 15, 5]
unit_prices = [10, 9, 5]
mamas_bakery_v2(items, total_units, unit_prices)
