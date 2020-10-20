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
            print("Enter birthday. Use a leading zero for months 1-9."
                  " You can use any of the past 100 years")
            birthday = input("Use this format MM/DD/YYYY: ")
            name_validation(friend)
            if not validate_date(birthday):
                raise ValueError("You did not enter a valid birthday.")
        except ValueError as error:
            print(error)
        else:
            new_friend = add_friend(friend, birthday)
            return new_friend


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


def validate_date(date):
    "Makes sure that date entered is valid and in last 100 years."
    NUMB_IDX = (0, 1, 3, 4, 6, 7, 8, 9)
    PUNC_IDX = (2, 5)

    # quickly check presence of punctuation and length
    if (date.count("/") == 2) and (len(date) == 10):
        return True
    else:
        return False

    # check type and position
    for char in range(0, len(date)):
        if (date[char].isdigit()) and (char in NUMB_IDX) and\
           (date[char] == "/") and (char in PUNC_IDX):
            return True
        else:
            return False

    # validate date
    month, day, year = date.split("/")
    thirties = [4, 6, 9, 11]
    thirty_ones = [1, 3, 5, 7, 8, 10, 12]

    if (int(month) in range(1, 13)) and (int(day) in range(1, 32)) and\
       (int(year) in range(1920, 2021)):
        pass
    elif (int(month) == 2) and (int(day) < 30):
        return True
    elif (int(month) in thirties) and (int(day) < 31):
        return True
    elif (int(month) in thirty_ones) and (int(day) < 32):
        return True
    else:
        return False


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
                raise ValueError("Choices are between 1 and 8 only.")
        except ValueError as error:
            print(error)
        else:
            return pick
