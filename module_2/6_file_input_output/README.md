# Concepts

- File Input Output


## Reading and Writing Files
`open()` returns a file object, and is most commonly used with two arguments: `open(filename, mode)`.

```
f = open('filename', 'r')
```
The first argument is a string containing the filename. The second argument is another string containing a few characters describing the way in which the file will be used. mode can be 'r' when the file will only be read, 'w' for only writing (an existing file with the same name will be erased), and 'a' opens the file for appending; any data written to the file is automatically added to the end. 'r+' opens the file for both reading and writing. The mode argument is optional; 'r' will be assumed if it’s omitted.

It is good practice to use the with keyword when dealing with file objects. The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point. Using with is also much shorter than writing equivalent try-finally blocks:

```
with open('filename') as f:
    file_data = f.read()
```

We can check that the file has been automatically closed.
`
f.closed
`
will return
`True`
If you’re not using the with keyword, then you should call `
f.close()
` to close the file and immediately free up any system resources used by it.

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

````
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
````


### Challenge 2:

Create a file called hub21.txt.
Add these lines to the file:
````
Coding is the key to the future.
There is no skill more important in the 21st century than coding. 
That’s why we’re dedicated to ensuring coding is accessible to all students including geographically and socioeconomically disadvantaged communities. 
````
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

## HARD

# Extra Scenarios
