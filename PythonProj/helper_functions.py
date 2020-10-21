import finprep as fp
import string_utils as su


"""
************************************************
 instantion related functions
************************************************
"""


def add_new_user(name, email):
    """Clean data and create User instance."""
    first, last = name.title().split(" ")
    NewUser = fp.User(first, last, email)
    print("Welcome, here is the information on file: ")
    print(repr(NewUser))
    return NewUser


def add_new_friend():
    """Get information and create Friend instance."""
    while True:
        try:
            friend = (str(input("Enter your friend's first and last name"
                                " seperated by a space, omit prefixes"
                                " and suffixes: ")))
            birthday = input("Enter birthday in this format "
                                 "with no leading zeros MM/DD/YYYY: ")
            new_friend = add_friend(friend, birthday)
            return new_friend
        except ValueError as error:
            print(error)
                  


def add_friend(friend, birthday):
    """Clean data and create Friend instance."""
    first, last = friend.title().split(" ")
    month, day, year = birthday.split("/")
    CurrentFriend = fp.Friend(first, last, int(month), int(day), int(year))
    print("Your new friend has been added.")
    print(repr(CurrentFriend))
    return CurrentFriend


def add_new_gift():
    """Get information and create new Gift instance."""

    while True:
        try:
            gift_name = str(input("Enter the name of the gift idea: "))
            gift_URL = str(input("Please paste the URL of the gift: "))
            gift_note = str(input("Enter an optional note: "))
            if not su.is_full_string(gift_name):
                raise ValueError("Enter a name for the gift idea.")
            if not su.is_url(gift_URL):
                raise ValueError("Enter a valid URL.")
        except ValueError as error:
            print(error)
        else:
            NewGift = fp.Gift(gift_name, gift_URL, gift_note)
            return NewGift



"""
************************************************
validation functions
************************************************
"""


def name_validation(name_to_check):
    """Make sure name is not empty, two words, not numbers."""
    if not su.is_full_string(name_to_check): # at least 1 non-space
        raise ValueError("Enter a name.")
    elif su.is_number(name_to_check):  # not just numbers
        raise ValueError("Enter a name, not a number.")
    elif not name_to_check.count(" ") == 1:  # not two words
        raise ValueError("Enter two names with a space in between")


"""
************************************************
menu functions
************************************************
"""


def display_main_menu():
    """Shows main options for program."""
    options = ["Add a new friend", "Add a new gift idea",
               "See list of friends", "Get list of gifts for a friend",
               "Update name or email", "Update friend information",
               "Update gift information", "Exit"]
    print("Please choose one of these options: ")
    for count, option in enumerate(options, 1):
        print(count, option)


def get_user_option():
    """Allows user to choose next action to take."""
    while True:
        try:
            pick = int(input("Enter number corresponding to your"
                             " choice: "))
            if (pick > 8) or (pick < 1):
                raise ValueError("Choices are between 1 and 8, or 99.")
        except ValueError as error:
            print(error)
        else:
            return pick
