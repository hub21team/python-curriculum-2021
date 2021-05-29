# Projects

1.  Guess Game  
2.  Rock, Paper, Scissors
3.  Ancient Game of Nimm
4.  Hailstones
5.  Dice Probability 


# Guess Game

Guess Game is one of the most popular projects that a beginner
programmer can build, Feel free to read how the game goes.

Below are the steps:

Build a Number guessing game, in which the user selects a range.
Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
Some random integer will be selected by the system and the user has to
guess that integer in the minimum number of guesses
Analysis:
If the User inputs range, let’s say from 1 to 100.
And compiler randomly selected 42 as the integer. And now the guessing
game started, so the user entered 50 as his/her first guess.
The compiler shows “Try Again! You guessed too high”. 
That’s mean the random number (i.e., 42) doesn’t fall in the range
from 50 to 100. That’s the importance of guessing half of the range. 
And again, the user guesses half of 50 (Could you tell me why?). 
So the half of 50 is 25. The user enters 25 as his/her second guess. 
This time compiler will show, “Try Again! You guessed too small”. 
That’s mean the integers less than 25 (from 1 to 25) are useless to 
be guessed. Now the range for user guessing is shorter, i.e., from 
25 to 50. Intelligently! The user guessed half of this range, so that, 
user guessed 37 as his/her third guess. 
This time again the compiler shows the output, 
“Try Again! You guessed too small”. 
For the user, the guessing range is getting smaller by each guess. 
Now, the guessing range for user is from 37 to 50, 
for which the user guessed 43 as his/her fourth guess. 
This time the compiler will show an output 
“Try Again! You guessed too high”. So, the new guessing range 
for users will be from 37 to 43, 
again for which the user guessed the half of this range, 
that is, 40 as his/her fifth guess.  
This time the compiler shows the output, 
“Try Again! You guessed too small”. 
Leaving the guess even smaller such that from 41 to 43. 
And now the user guessed 41 as his/her sixth guess. 
Which is wrong and shows output “Try Again! You guessed too small”. 
And finally, the User Guessed the right number which is 42 as his/her 
seventh guess.

    Hello, What's your name?
    Ece
    Enter the start and end values seperated with a space: 5 40
    Hello Ece ! I am thinking of a number between 5 and 40 guess what number it is!
    Guess: 20
    Your guess is too high
    Guess: 10
    You got it correct Ece!
    You guessed the number in 2 tries!

# Rock, Paper, Scissors

You may have played rock paper scissors before. Maybe you’ve used it to decide who pays for dinner or who gets first choice of players for a team.

If you’re unfamiliar, rock paper scissors is a hand game for two or more players. Participants say “rock, paper, scissors” and then simultaneously form their hands into the shape of a rock (a fist), a piece of paper (palm facing downward), or a pair of scissors (two fingers extended). The rules are straightforward:

Rock smashes scissors.
Paper covers rock.
Scissors cut paper.

Now that you have the rules down, you can start thinking about how they might translate to Python code.
![img.png](img.png)

Find Below a sample output:

    Pick rock, paper, or scissors: paper
    computer chose scissors
    You lose!

    player: 0 computer: 1

    Pick rock, paper, or scissors: rock
    computer chose scissors
    You win!

    player: 1 computer: 1

    Pick rock, paper, or scissors: scissors
    computer chose scissors
    it's a tie!

    player: 1 computer: 1

# Ancient Game of Nimm

Nimm is an ancient game of strategy that is named after the old German word for "take." It is also called Tiouk Tiouk in West Africa and Tsynshidzi in China. Players alternate taking stones until there are zero left.

The game of Nimm goes as follows:

  - The game starts with a pile of 20 stones between the players.

  - The two players alternate turns.

  - On a given turn, a player may take either 1 or 2 stone from the center pile.

  - The two players continue until the center pile has run out of stones.

  - The last player to take a stone loses.


Here's a sample execution:


    There are 20 stones left
    Player 1 would you like to remove 1 or 2 stones? 2

    There are 18 stones left
    Player 2 would you like to remove 1 or 2 stones? 2
    
    There are 16 stones left
    Player 1 would you like to remove 1 or 2 stones? 1
    
    There are 15 stones left
    Player 2 would you like to remove 1 or 2 stones? 2
    
    There are 13 stones left
    Player 1 would you like to remove 1 or 2 stones? 2
    
    There are 11 stones left
    Player 2 would you like to remove 1 or 2 stones? 1
    
    There are 10 stones left
    Player 1 would you like to remove 1 or 2 stones? 2
    
    There are 8 stones left
    Player 2 would you like to remove 1 or 2 stones? -1
    Please enter 1 or 2: 2
    
    There are 6 stones left
    Player 1 would you like to remove 1 or 2 stones? 2
    
    There are 4 stones left
    Player 2 would you like to remove 1 or 2 stones? 2
    
    There are 2 stones left
    Player 1 would you like to remove 1 or 2 stones? 1
    
    There are 1 stones left
    Player 2 would you like to remove 1 or 2 stones? 1
    
    Player 1 wins!

# Hailstones

Hailstones is based on a problem in Douglas Hofstadter’s
Pulitzer-prize-winning book Gödel, Escher, Bach. 
That book contains many interesting mathematical puzzles, 
many of which can be expressed in the form of computer programs. 
In Chapter XII, Hofstadter mentions a wonderful problem that is 
well within the scope of what you know. The problem can be 
expressed as follows:

- Pick some positive integer and call it n.
- If n is even, divide it by two.
- If n is odd, multiply it by three and add one.
- Continue this process until n is equal to one.
- On page 401 of the Vintage edition of his book, 
  Hofstadter illustrates this process with the following example, 
  starting with the number 15:
  
      15 is odd, so I make 3n+1: 46
  
      46 is even, so I take half: 23
  
      23 is odd, so I make 3n+1: 70
  
      70 is even, so I take half: 35
  
      35 is odd, so I make 3n+1: 106
  
      106 is even, so I take half: 53
  
      53 is odd, so I make 3n+1: 160
  
      160 is even, so I take half: 80
  
      80 is even, so I take half: 40
  
      40 is even, so I take half: 20
  
      20 is even, so I take half: 10
  
      10 is even, so I take half: 5
  
      5 is odd, so I make 3n+1: 16
  
      16 is even, so I take half: 8
  
      8 is even, so I take half: 4
  
      4 is even, so I take half: 2
  
      2 is even, so I take half: 1

# Dice Probability  

The question is: How many times do I need to throw a die to get all the sides at least once at average?
This is a problem from a university level mathematics course called Probability Theory.
To further explain the problem, Say you have a fair die.

You roll it once and observe a 5.

You roll it again and observe a 3. 

You roll it yet again and get a 4. 

In three throws you’ve observed 3 of the possible sides.
So you have to keep rolling to see the other 3. 
How many rolls would it take to see all six sides at least once?
Calculating the expected number of times we have to roll a die, 
requires solid mathematical knowledge. But, we gained enough programming knowledge so far, 
we can simulate this rolling of a die, even though it won't be a proper solution, 
we are able to find the result. 
      
    The answer is: 14.7. 

So, we expect to roll a die about 15 times on average 
before we observe all sides at least once.

We can use this same line of thinking to answer such 
“real-life” questions as how many boxes of cereal 
would you have to buy to collect the latest series of 
cheap plastic toys, assuming the toys are randomly added 
to the cereal in a uniform manner. Of course 
if you’re desperate to collect the precious toys and 
have a modicum of patience, the answer is probably 0. 
You’d just wait to buy the whole set on eBay.



