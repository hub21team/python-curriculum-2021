# Simple Functions

## Concepts

- Multiple input/output
- Parameter Passing
- Return values
- Complex Operations

### Multiple input, output

### Parameter Passing
In Module 1, we drew the difference between argument and parameter but as students start to use different data types in their functions, this concept will likely continue to cause some confusion.

Without getting too much into the detail, tutor should draw student's attention to the function that modify arguments in place and brainstorm about the reasons behind the behavior. 

Tutors may read more on different parameter passing types (pass by reference, pass by value, call by reference, call by value) [here](https://www.geeksforgeeks.org/pass-by-reference-vs-value-in-python/). 

Here, as we modify the variables  we challenge the boxes idea from the very first lecture by introducing the addresses in the memory. A quick modification to the original analogy could be introducing labels pointing to the boxes. When we pass collection-like data types (list, dictionary, etc.) we pass the address of the variable (aka. label).

### Default Parameters
If time permits and the student is advanced, tutor may introduce default parameters.

# Teaching Tips

- Students were introduced to the concept of functions, input and output (briefly for the latter) in Module 1.
- Tutor should emphasize the importance of writing clear comments especially since we are dealing with multiple inputs and outputs. 
- Based on the student when talking about parameter passing, it may be better if the tutor doesn't direclty name them parameter passing/call by reference etc. so that the student is not encoraged to memorize. 
- Our main goal here is to make them more comfortable with functions and revisit the concept with the recently introduced collections (dictionaries, sets, lists, etc.). Therefore, you can give a lot of examples and let the student explore different behaviors on their own. 

## Challenges

### Easy

#### Play with variables inside functions
Two friends Seyhan and Ceyhan argue about Python functions. Seyhan this that all functions can modify the values of variables while Ceyhan doesn't agree. To end the dispute once and for all between besties explore the behavior of functions on the input.
In order to heat up the competition we will proceed in three rounds.
1. Define basic variables of types `int, bool, string, list`  and a function `did_i_modify_var(var)`  which tries to change the value of `var` to 9, print  the value of the argument inside and outside the function to see how the function behaves.
2. Moving on, define two variables of types `list, dictionary`. Implement `did_i_modify_collection(var)` that tries to change the first element of the list to "new variable", you may use the same function for dictionary, in a way it will try to add "new_variable" to the key 0.
   Now, define a variable of type `tuple`, how does the function behave? 
3. Define a variable of type `set` and implement `did_i_modify_set(var)` that tries to add "new_element" string to `var`.
**Note:** we wrote a function `see_how_it_behaves` that takes variable and modifying function as parameters but if tutor feels like this may be confusing for the student, they may include print statements in the `did_i` functions.

#### Lists, com'n

#### Eat it fast
Two siblings, 
### Medium

#### 


### Hard

#### 

# Credits:

