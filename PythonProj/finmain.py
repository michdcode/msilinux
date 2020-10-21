# Standard Library Imports 
import sys
import string_utils as su

# Local imports
from helper_functions import *

# initialize variables and data structures

end_users = []
user_friends = []
friend_gifts = []

choice = 0

# Welcome
print("Welcome to Birthday Buddy!")
print("Birthday Buddy helps track friends birthdays and gift ideas.")
print("Let's get started!")

# Sign up user and validate data
while True:
    try:
        name = (str(input("Enter your first and last name seperated "
                          "by a space, omit prefixes and suffixes: ")))
        email = (str(input("Enter your email address: ")))
        name_validation(name)
        if not su.is_email(email):  # check that it is email
            raise ValueError("You did not enter an email address.")
    except ValueError as error:
        print(error)
    else:
        break

# clean data and create new user
NewUser = add_new_user(name, email)
end_users.append(NewUser)
CurrentUser = NewUser


# main control of program
while choice is not 8:
    display_main_menu()
    option = get_user_option()

    # Add a new friend
    if option == 1:
        NewFriend = add_new_friend()
        user_friends.append(NewFriend)
        CurrentUser.set_new_friend(NewFriend)
    # Add a new gift idea
    elif option == 2:
        if len(user_friends) < 1:
            print("Enter a friend before adding a gift.")
        NewGift = add_new_gift()
        find_friend = input("Enter the first and last name with a space in "
                            "between of friend you have a gift idea for: ")
        name_validation(find_friend)
        find_friend = find_friend.title()
        friend_first, friend_last = find_friend.split()
        try:
            for friend in user_friends:
                if (friend_first == friend.first_name) and\
                   (friend_last == friend.last_name):
                    friend.set_new_gift_on_giftlist(NewGift)
                    friend_gifts.append(NewGift)
                    print("Added the gift to your friends gift list!")
        except KeyError as error:
            print(error)
        else:
            "Could not find friend on your list, gift not added."

    # List of friends
    elif option == 3:
        lst_of_friends = CurrentUser.prnt_friend_lst()
        print(lst_of_friends)
        print("Outputting list of friends to file named friends.txt")
        filename = open("friends.txt", "w")
        for item in CurrentUser.get_friend_lst():
            s = (str(item)) + "\n"
            filename.write(s)
        filename.close()
    # Get list of gifts for a friend
    elif option == 4:
        if len(user_friends) < 1:
            print("You do not have any friends")
            break
        print("Enter the first and last name with a space in between.")
        find_friend = input("Use exact name as originally entered: ")
        name_validation(find_friend)
        find_friend = find_friend.title()
        friend_first, friend_last = find_friend.split()
        try:
            for friend in user_friends:
                if (friend_first == friend.first_name) and\
                   (friend_last == friend.last_name):
                    print("The gift list for {} {} is:".format
                          (friend.first_name, friend.last_name))
                    for gift in friend._gift_lst:
                        print(gift)
        except KeyError as error:
            print(error)
        else:
            "Could not find friend on your list, please try again."
    # Update name or email
    elif option == 5:
        update_user_info()
    # Update friend information
    elif option == 6:
        update_friend_info()
    # Update gift information"
    elif option == 7:
        update_gift_info()
    # Exit
    elif option == 8:
        choice = 8

if choice == 9:
    print("Thank you for using Birthday Buddy.")
    print("Exiting.")
    sys.exit()





