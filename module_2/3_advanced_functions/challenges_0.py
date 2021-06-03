###------------------------------------------------- EASY -------------------------------------------------###

""" 
Play with variables inside functions

Two friends Seyhan and Ceyhan argue about Python functions. Seyhan this that all functions can modify the values of variables while Ceyhan doesn't agree. To end the dispute once and for all between besties explore the behavior of functions on the input.
In order to heat up the competition we will proceed in three rounds.
1. Define basic variables of types `int, bool, string, list`  and a function `did_i_modify_var(var)`  which tries to change the value of `var` to 9, print  the value of the argument inside and outside the function to see how the function behaves.
2. Moving on, define two variables of types `list, dictionary`. Implement `did_i_modify_collection(var)` that tries to change the first element of the list to "new variable", you may use the same function for dictionary, in a way it will try to add "new_variable" to the key 0.
   Now, define a variable of type `tuple`, how does the function behave? 
3. Define a variable of type `set` and implement `did_i_modify_set(var)` that tries to add "new_element" string to `var`.
"""

def did_i_modify_var(a):
    a = 9
    print("In the function ", a)


def did_i_modify_collection(lst):
    lst[0] = 9
    print("In the function ", lst)


def did_i_modify_set(s):
    s.add("new element")
    print("In the function ", s)


def see_how_it_behaves(var, func_to_try: function):
    """     run the func_to_try with var as argument and print the effect    """
    print("Before the function ", var)
    func_to_try(var)
    print("After the function ", var)
    print("-"*15)


my_vars = [3, True, 4.2, "Hello"]
for my_var in my_vars:
    see_how_it_behaves(my_var, did_i_modify_var)

my_lst = [1, 2]
see_how_it_behaves(my_lst, did_i_modify_collection)

my_dict = {1: "a", 2: "b"}
see_how_it_behaves(my_dict, did_i_modify_collection)

my_set = {1, 2}
see_how_it_behaves(my_set, did_i_modify_set)

# this will result in error
# my_tuple = (1, 2)
# see_how_it_behaves(my_tuple, did_i_modify_collection)

def set_lst(lst):
    lst = [1, 2, 3]
    return lst