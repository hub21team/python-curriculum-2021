"""
Problem 1
"""
import random
court_size = int(input("Enter size of court"))

while court_size < 3:
    court_size = int(input("Court size should not be less than 3. Please Enter a valid value."))

player_position = 1
computer_position = 1
player_win = None

while True:

    throw_command = input("Play your turn by entering throw")
    while throw_command != 'throw':
        throw_command = input("Play your turn by entering throw")
    print("")

    player_move = random.randint(1, 6)
    player_position += player_move

    print("You moved " + str(player_move) + " steps.")
    print("Your current position is", player_position)
    print("")

    if player_position >= court_size:
        player_win = True
        break

    computer_move = random.randint(1, 6)
    computer_position += computer_move

    print("Computer moved " + str(computer_move) + " steps.")
    print("Computer's current position is", computer_position)
    print("")
    if computer_position >= court_size:
        player_win = False
        break

if player_win:
    print("You won the race!")
else:
    print("Computer won the race!")

#------------------------------------------------------------------
"""
Project 2
"""

def show_options():
    print("Choose one of the following options by inputing its number: ")
    print("1) New Contact")
    print("2) Delete Contact")
    print("3) Modify Phone Number")
    print("4) Modify Email")
    print("5) Show Contacts")
    print("6) Quit")
    option = input()
    return int(option)

def create_new_contact(phonebook):
    name = input("Enter the name of the contact. ")
    phone_number = input("Enter the phone number of the contact. ")
    email = input("Enter the email of the contact. ")

    if name in phonebook:
        response = input("Contact already exists. Do you wish to overwrite it ? (Enter [Y or y or yes or Yes] for positive, or anything else for negative").

        if response not in ['y', 'Y', 'yes', 'Yes']:
             print("Adding new contact aborted.")
             return

    phonebook[name] = (phone_number, email)
    print("Contact Successfully Created !")

def delete_contact(phonebook):

    name = input("Enter name of contact to delete")
    if name not in phonebook:
        print("contact name does not exist in phonebook")
        return
    del phonebook[name]

def modify_phone_number(phonebook):

    name = input("Enter name of contact whose phone number will be modified")
    if name not in phonebook:
        print("contact name does not exist in phonebook")
        return
    new_phone_number = input("Enter new phone number")
    old_phone_number, old_email = phonebook[name]
    phonebook[name] = (new_phone_number, old_email)

def modify_email(phonebook):

    name = input("Enter name of contact whose email will be modified")
    if name not in phonebook:
        print("contact name does not exist in phonebook")
        return
    new_email = input("Enter new email")
    old_phone_number, old_email = phonebook[name]
    phonebook[name] = (old_phone_number, new_email)

def show_contacts(phonebook):
    for name in phonebook.keys():
        print(name + ", " + phonebook[name][0] + ", " + phonebook[name][1])

def save_phonebook(phonebook):

    phonebook_str = ""
    for name in phonebook.keys():
        line = name + ", " + phonebook[name][0] + ", " + phonebook[name][1] + "\n"
        phonebook_str += line
    with open("phonebook.txt", "w") as f:
        f.write(phonebook_str)

def run_program():

    phonebook = {}
    while(True):
        option = show_options()

        if option == 1:
            create_new_contact(phonebook)
        elif option == 2:
            delete_contact(phonebook)
        elif option == 3:
            modify_phone_number(phonebook)
        elif option == 4:
            modify_email(phonebook)
        elif option == 5:
            show_contacts(phonebook)
        elif option == 6:
            save_phonebook(phonebook)
            break
