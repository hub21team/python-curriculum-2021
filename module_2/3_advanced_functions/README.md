# Simple Functions

## Concepts

- Multiple input/output
- Parameter Passing
- Return values
- Complex Operations
- Scope and Global Variables


# Teaching Tips

- Students were introduced to the concept of functions, input and output (briefly for the latter) in Module 1.
- Tutor should emphasize the importance of writing clear comments especially since we are dealing with multiple inputs and outputs. 
- Based on the student when talking about parameter passing, it may be better if the tutor doesn't direclty name them parameter passing/call by reference etc. so that the student is not encoraged to memorize. 
- Our main goal here is to make them more comfortable with functions and revisit the concept with the recently introduced collections (dictionaries, sets, lists, etc.). Therefore, you can give a lot of examples and let the student explore different behaviors on their own. 
- Please also note that the following week is left aside for practicing data structures and functions. Therefore, you may balance the material in two weeks and solve more examples from Week 4 material as well.
### Multiple input, output
```python
def sum(a, b):
  return a+b
```

```python
def min_and_max(lst):
  return min(lst), max(lst)
```

### Parameter Passing
In Module 1, we drew the difference between argument and parameter but as students start to use different data types in their functions, this concept will likely continue to cause some confusion.

Without getting too much into the detail, tutor should draw student's attention to the function that modify arguments in place and brainstorm about the reasons behind the behavior. 

Tutors may read more on different parameter passing types (pass by reference, pass by value, call by reference, call by value) [here](https://www.geeksforgeeks.org/pass-by-reference-vs-value-in-python/). 

Here, as we modify the variables  we challenge the boxes idea from the very first lecture by introducing the addresses in the memory. A quick modification to the original analogy could be introducing labels pointing to the boxes. When we pass collection-like data types (list, dictionary, etc.) we pass the address of the variable (aka. label).

### Scope and Global Variables
Reiterate the idea of scope by referring to the early if/else topics from Module 1. 
```python
currency_rate = 5
material_in_tl = 200
material2_in_dollar = 21

def us_store(price_in_tl):
  dollar_price = price_in_tl / currency_rate
  return dollar_price

def tr_store(price_in_dollar):
  tl_price = price_in_dollar * currency_rate
  return tl_price

dollar_p = us_store(material_in_tl)
tl_p = tr_store(material2_in_dollar)
print("Total dollar price of first material", dollar_p)
print("Total tl price of first material", tl_p)
```
### Default Parameters
If time permits and the student is advanced, tutor may introduce default parameters.
