import string_utils as su
import finprep as fp
import helper_functions as hf
import sys


# Welcome
print("Welcome to Birthday Budddy!")
print("Birthday Buddy helps track friends birthdays and gift ideas.")
print("Let's get started!")

# Sign Up User and validate data
while True:
    try:
        name = (str(input("Enter your first and last name seperated "
                          "by a space, omit prefixes and suffixes: ")))
        email = (str(input("Enter your email address: ")))
        if not su.is_full_string(name):
            raise ValueError("Enter a name.")
        elif su.is_number(name):  # name is not just numbers
            raise ValueError("Enter a name, not a number.")
        elif not name.count(" ") == 1:  # name is not two words
            raise ValueError("Enter two names with a space in between")
        elif not su.is_email(email):  # check that it is email
            raise ValueError("You did not enter an email address.")
    except ValueError as error:
        print(error)
    else:
        break


# clean data and create new user 

name_snake = name.replace(" ", "_")
CurrentUser = su.snake_case_to_camel(name_snake)
first, last = name.title().split(" ")
CurrentUser = fp.User(first, last, email)
print("Welcome, here is the information on file: ")
repr(CurrentUser)

# main menu


def display_main_menu():

    options = ["Add a new friend", "Add a new gift idea",
               "List of friends", "Get list of gifts for a friend",
               "Update name or email", "Update friend information",
               "Update gift information", "Exit"]
    print("Please choose one of these options: ")
    for count, option in enumerate(options, 1):
        print(count, option)


def get_user_option():
    while True:
        try:
            pick = int(input("Enter number corresponding to your"
                               "choice: "))
            if (pick > 8) or (pick < 1):
                raise ValueError("Choices are between 1 and 8 only.")
        except ValueError as error:
            print(error)
        else:
            return pick


while choice != 8
    display_main_menu()
    option = get_user_option()
    
    if option == 1:
        hf.add_new_friend()
    elif option == 2:
        add_new_gift()
    elif option == 3:
        get_friend_list()
    elif option == 4:
        get_friend_gift_list()
    elif option == 5:
        update_user_info()
    elif option == 6:
        update_friend_info()
    elif option == 7:
        update_gift_info()
    elif option == 8:
        choice = 8

print("Thank you for using Birthday Buddy.")
print("Exiting.")
sys.exit()






"""
# password = (str(input("Enter a password with 8 or more "
        #             "characters: ")))
        # hint = (str(input("Enter a hint to remember your password: ")))

if (not su.is_full_string(name)) or (not
            su.is_full_string(password)) or (not
            su.is_full_string(hint)):
elif len(password) < 8:
            raise ValueError("Password must be at least 8 characters")
"""
