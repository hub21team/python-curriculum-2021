# Concepts

- File Input Output

  - open / close

    ```
    # first way
    f = open('trial.txt', 'r')
    ...
    f.close()

    # second way
    with open('trial.txt', 'r') as f:
      ...
    ```

  - modes ('r', 'w', 'r+', ...)
  - read

    ```
    # one way (all data)
    data = f.read()
    print(data)

    # another way (by word)
    with open('trial.txt') as f:
    data = f.read()
    data = data.split() # splits my data to words
    for elt in data:
      print(elt)

    # yet another way (by line)
    with open('trial.txt') as f:
    data = f.readlines()
    for line in data:
      line = line.strip() # removes all the space or new line characters in the beginning or end of the line
      print(line)
    ```

  - write

    ```
    line = "some text"
    line2 = "some another text"
    with open('trial2.txt', 'w') as f:
      f.write(line)
      f.write(line2)

    ```

## Reading and Writing Files

`open()` returns a file object, and is most commonly used with two arguments: `open(filename, mode)`.

```
f = open('filename', 'r')
```

**first argument:** filename that will be modified/read.  
**modes:**

- 'r': only read
- 'w': only write (overwrites the file if there is already one)
- 'a': append to the end of the file
- 'r+': both read and write (gives error if file does not exist)
- 'w+': both write and read (overwrites the file if there is already one)
- 'a+': both read and append
- If nothing is given for the mode argument, 'r' is assumed by computer.

It is good practice to use the `with` keyword when dealing with file objects. The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point. Using with is also much shorter than writing equivalent try-finally blocks:

```
with open('filename') as f:
    file_data = f.read()
```

We can check that the file has been automatically closed, `f.closed` will return `True`.  
If you’re not using the `with` keyword, then you should call `f.close()` to close the file and immediately free up any system resources used by it.

Warning Calling `f.write()` without using the with keyword or calling `f.close()` might result in the arguments of `f.write()` not being completely written to the disk, even if the program exits successfully.  
After a file object is closed, either by a with statement or by calling `f.close()`, attempts to use the file object will automatically fail.

```
f.close()
f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```

# Challenges

## EASY

### Challenge 1:

Write a program to prompt for a file name, and then read through the file line-by-line.
Note: the file name in the directory is Daffodils.txt - a beautiful lyric by William Wordsworth and its content is,

```
I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze.

Continuous as the stars that shine
and twinkle on the Milky Way,
They stretched in never-ending line
along the margin of a bay:
Ten thousand saw I at a glance,
tossing their heads in sprightly dance.

The waves beside them danced; but they
Out-did the sparkling waves in glee:
A poet could not but be gay,
in such a jocund company:
I gazed—and gazed—but little thought
what wealth the show to me had brought:

For oft, when on my couch I lie
In vacant or in pensive mood,
They flash upon that inward eye
Which is the bliss of solitude;
And then my heart with pleasure fills,
And dances with the daffodils.
```

### Challenge 2:

Create a file called hub21.txt.
Add these lines to the file:

```
Coding is the key to the future.
There is no skill more important in the 21st century than coding.
That’s why we’re dedicated to ensuring coding is accessible to all students including geographically and socioeconomically disadvantaged communities.
```

And then print the content of hub21.txt.

## MEDIUM

### Challenge1:

```
“And once the storm is over,
you won’t remember how you made it
through, how you managed to survive.
You won’t even be sure,
whether the storm is really over.
But one thing is certain.
When you come out of the storm,
you won’t be the same person who walked in.
That’s what this storm’s all about.”

― Haruki Murakami, Kafka on the Shore
```

First, create a txt file with the content above, and then count how many
"you" that text has and print the number on the console.

### Challenge 2:

Your school decided to purchase 20 books for the library, and they asked everyone to put a book name with the author, publish data, and rating information to the requested books page. However, since there are too much books, they need to have a way of choosing the books somehow! You suggested that they can sort the books in alphabethical order and purchase the first 20 books. Now, you have to give them the sorted version of the `books.txt` file as `books_sorted.txt`.

## HARD

### Challenge 1:

Write a function named `count_occurances` that takes a filename as an input and finds the number of occurances for each word in the file. Finally, the function should return this information.  
**Hint:** First, think about what would be the best way to store occurance information.
**Note:** Think about the special characters in a text which can corrupt the words such as `.`, `,`, `"` etc. Find a way to eliminate them so that the program can divide words correctly.

### Challenge 2:

** Note to Tutor: ** If you have not solved MEDIUM Challenge 2 together, please also provide the back story and `books_sorted.txt` file.

School has given you back the file `books_sorted.txt` and told you that you should fix the errors because the same bookname occurs multiple times, and also heading of the file where it says:

```
Book Name, Author, Published at, Rating
```

is also sorted when it should not be. Fix the problems and submit the new version as `books_sorted_fixed.txt`.

# Extra Scenarios
