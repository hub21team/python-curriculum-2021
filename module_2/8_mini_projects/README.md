# Problems
* Data Structures Problem
* Advanced Functions Problem
* File Input Output
* Error Handling



# Project 1: Dice Rolling Race

  In this project, you will create a game in which you will create play in a race against the computer using Dice! First, the program will ask you to enter the size of the race court. The race court is straight line of cells and in a single step the player can move from one step to another in one direction. The size of the race court is the number of cells in the court such that the first cell is the start position of the players and the last cell is the target cell and whoever reaches (or exceeds) it first wins the race. Therefore, the size of the cell must be at least equal to 3. If the user enters a court size less than three then keep asking again until they enter a valid size value.

  In order to move, you and the computer will take turns. In each turn, the player will throw a 6-faced dice and then move with a number of steps equal to the number appearing on the dice. (hint: the dice throw is a random process that produces numbers between 1 and 6).

  In your turn, the program should wait for you to enter the word `throw` as input. The computer turn will be played immediately after your turn. You always start first in the game. When the game ends you should announce who is the winner by printing one of the following
  * `Computer won the race!`
  * `You won the race!`

  After each throw, you should print the number of steps each player moved and their current position.

# Project 2: Phonebook

In this project, you will create a phonebook app that stores phone numbers and emails of your friends. The app should allow the user to add, modify, delete, show, and fetch phone numbers and emails from the phonebook.

The app should always print all the options available to the users, and after an action is finished, it should show all the options again. Here are the options that should be available and their details.

1. `new contact`: This option creates a new contact info. When chosen, it asks the user to enter the following:
    * Name of contact.
    * Phone Number of Contact
    * Email of Contact.

    If the entered name of contact, already exists, then the program should ask the user if they want to overwrite the already existing information.

2. `delete contact`: This option asks the user for the name of the contact to be deleted. If the name exists, the information about the contact is deleted. If the name does exist in the phonebook, the program should tell the user that the desired number does not exist.

3. `modify phone number`: This option asks for the name of the contact which they want to modify their phone number, and asks the user to enter the new phone number to overwrite the old one. If given name does not exist, signal this to user and abort the operation.

4. `modify email`: This option asks for the name of the contact which they want to modify their email, and asks the user for the new email to overwrite the old one. If given name does not exist, signal this to the user and abort the operation

5. `show contacts`: This option prints all contacts, one contact per line in the following format:
    ```
    Erwin Smith, 09104200013, esmith@gmail.com
    Historia Reis, 05139343333, hreis@gmail.com
    ...
    ```
6. `quit`: Exits and closes the program, but before closing it saves the contacts in `.txt` file in the same format in the `show contacts` command.

You must use function in this project, such that each functionality is encapsulated in its own function. So you need to implement the following functions:
1. `run_program`: This is the main function that runs the program loop and it is called only once to start the program.
2. `show_options`: shows the user the options and reads the input which represents the users chosen option.
3. `delete_contact`: deletes an entry from the phone book
4. `modify_phone_number`: modifies a phone number of a particular name in the phonebook.
5. `modify_email`: modifies the email of a particular name in the phonebook
6. `save_phonebook`: saves the contents of the phonebook into a `.txt` file.


**Hints**:
* The phonebook needs to represented by some data structure, what do you think we can use. We might need to use more than one.
* The phonebook should be modified from different functions, what is the best way to make the phonebook accessible and modifiable from different function ? There are several ways.

## Bonus
* when using the `show contacts` option, can you make so that the contacts are sorted by alphabetical order
* When the program asks the user to enter a phone number and an email, the user might enter something that is not numerical for the phone number, like text or symbols, or something which is not a valid email. Can you handle this case by checking if the phone number is numerical and if the email is valid ? An email is valid if it has the following format:
    ```
    [lower_case_alphabets or number or symbols: .-]@gmail.com
    ```
