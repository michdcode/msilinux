import finprep as fp
import string_utils as su

def add_new_friend():
    # get_current_user()
    while True:
        try:
            name = (str(input("Enter your friend's first and last name"
                              " seperated by a space, omit prefixes"
                              " and suffixes: ")))
            print("Enter birthday. Use a leading zero for months 1-9."
                  " You can use any of the past 100 years")
            birthday = input("Use this format MM/DD/YYYY: ")
            if not su.is_full_string(name):
                raise ValueError("Enter a name.")
            elif su.is_number(name):  # name is not just numbers
                raise ValueError("Enter a name, not a number.")
            elif not name.count(" ") == 1:  # name is not two words
                raise ValueError("Enter two names with a space in between")
            elif not validate_date(birthday):
                raise ValueError("You did not enter a valid birthday.")
        except ValueError as error:
            print(error)
        else:
            new_friend = add_friend_to_dict(name, birthday)
            return new_friend
            # next up is to add friend to user's friend list


def add_friend_to_dict(name, birthday):
    first, last = name.title().split(" ")
    month, day, year = birthday.split("/")
    CurrentFriend = fp.Friend(first, last, int(month), int(day), int(year))
    print("Your new friend has been added.")
    print(repr(CurrentFriend))
    return CurrentFriend



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

