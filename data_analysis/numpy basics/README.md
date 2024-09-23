# Ideas
* What is a Dataset
* Constructing and Manipulating Datasets with NumPy 
* NumPy Operations

# What is a Dataset?

  A collection of related sets of information that is composed of separate elements but can be manipulated as a unit by a computer.
  
  We can construct and manipulate single-variable datasets using Python's NumPy library.
  
# NumPy Library

  NumPy stands for Numerical Python and it is the universal standard for working with numerical data in Python.
  
  The NumPy library contains multidimensional array and matrix data structures which enables us to construct and manipulate datasets.
  
  It provides $ndarray$, a homogeneous n-dimensional array object, with methods to efficiently operate on it.
  NumPy can be used to perform a wide variety of mathematical operations on arrays. 
  
  To be able to use it you need to install the library:  
  ```python
  import numpy as np
  ```
  

## Why we need NumPy's ndarray and not use lists?

  NumPy arrays are faster and more compact than Python lists. 
  An array consumes less memory and is convenient to use. NumPy uses much less memory to store data and it provides a mechanism of specifying the data types. 
  This allows the code to be optimized even further.


  NumPy's ndarrays are powerful data structures that guarantee *efficient* calculations with not only arrays but also matrices.
  
  It also supplies an enormous library of high-level mathematical functions that operate on these arrays and matrices.
  
  
  Note: While a Python list can contain different data types within a single list, all of the elements in a NumPy array should be homogeneous. 
  The mathematical operations that are meant to be performed on arrays would be extremely inefficient if the arrays weren’t homogeneous.
  

## What is an array?

  An array is a grid of values and it contains information about the raw data, how to locate an element, and how to interpret an element.
  
  The elements are all of the same type, referred to as the array dtype.
  
###Initializing an array
  
  1. One way we can initialize NumPy arrays is from Python lists.
	  Here is how to initialize a single-variable dataset.  
	  
	  ```python
		my_list = [23.4, 78.8, 90.9, 2, 54.5, 345]
		my_list_np = np.array(my_list) 
	  ```
	  or
	  
	   ```python
		  a = np.array([1, 2, 3, 4, 5, 6])
		```  
	   
	   We can also initialize two- or higher-dimensional dataset by using nested lists.
	   two- or higher-dimensional arrays can be inferred as matrices.
		  
	   **2d Numpy array -> 2x2 matrix**
	   
	   ```python
		  matrix1 = np.array([[1,2,3],[4,5,6]])

		  matrix2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
		``` 
	2. Another way to initialize NumPy arrays is by using functions **.zeros()** or **.ones()**
	
		Besides creating an array this functions also fills with 0’s or 1's:
		
		```python
		  np.zeros(2)
  		  >>> array([0., 0.])
		
		  np.ones(2)
		  >>> array([1., 1.])
		``` 	
	
	3. You can also create an empty array:
		
		The function empty creates an array whose initial content is random and depends on the state of the memory.
		The reason to use empty over zeros (or something similar) is speed - just make sure to fill every element afterwards!
		
		```python
		  # Create an empty array with 2 elements
		  np.empty(2) 
		  >>> array([3.14, 42.  ])  # may vary
		```
	4. Lastly, you can create an array with a range of elements:
	   
	   ```python
		  np.arange(4)
		  >>> array([0, 1, 2, 3])
		```
		
		And even an array that contains a range of evenly spaced intervals. 
		
		To do this, you will specify the first number, last number, and the step size.

		```pyhton
		  np.arange(2, 9, 2)
		  >>> array([2, 4, 6, 8])	
		```
		
###Accessing/Indexing specific element
	
	1. To get a specific element from an array use *arr[r,c]* here r specifies row number and c column number.
	```pyhton
		print(arr[1,2])	
	```
	
	2. To get all elements of a Row or Column *:* is used to specify that we need to fetch every element.
	```pyhton
		print(arr[1,:])	#to print all columns of row 1
		print(arr[:,2])	#to print all rows with column 2
	```
	3. Accessing multiple rows and columns at a time
	```pyhton
		print(arr[[1:3,1:3]])	#here we are defining ranges for both rows and columns, same idea as we had in python lists
	```
####Scalar operation
	The scalar operations (+,-,*,/) will operate with scalar to element of an array
	```pyhton
		arr = [2,4,6,8,10]
		print(arr/2)
		>>> arr = [1,2,3,4,5]
	```
	
# Challenges

	##Challenge 1
	
	Loti Pierre is a fictional (mostly) movie review site where four good friends and movie reviewers, Chris, Melissa, Laura, and Kevin watch movies and give them ratings on a scale of 0 to 100.
	For three movies, ask them their ratings and store in an array.

	##Challenge 2
	
	Use your array from Challenge 1, turn 0-100 scale into 5 star rating scale by manipulating the array.
	
	##Challenge 3
	
	Again by using the array from Challenge 1:
	* Find Laura's ratings for each movie.
	* Let's say we find that we have very similar taste to Melissa, so we only want to see movies that she gives a good rating to. Find all the movies that Melissa has rated as good. You can assume good movies are the ones with rating with higher than 80.
	
	