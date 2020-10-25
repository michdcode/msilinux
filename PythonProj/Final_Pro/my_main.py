# Standard Library Imports
import sys
import string_utils as su
from datetime import date

# Local imports
from my_functions import *

# initialize data structures
end_users = []
user_friends = []
friend_gifts = []


def welcome():
    """Print initial greeting to new user."""
    print("Welcome to Birthday Buddy!")
    print("Birthday Buddy helps track friends birthdays and gift ideas.")
    print("Let's get started!")


def sign_up_new_user():
    while True:
        try:
            name = (str(input("Enter your first and last name separated "
                            "by a space, omit prefixes and suffixes: ")))
            email = (str(input("Enter your email address: ")))
            name_validation(name)
            if not su.is_email(email):  # check that it is email
                raise ValueError("You did not enter an email address.")
        except ValueError as error:
            print(error)
        else:
            break
    NewUser = add_new_user(name, email)
    end_users.append(NewUser)
    CurrentUser = NewUser
    return CurrentUser


def main(CurrentUser_instance):
    choice = 0
    CurrentUser = CurrentUser_instance
    while choice is not 6:
        display_main_menu()
        option = get_user_option()

        # Add a new friend
        if option == 1:
            NewFriend = add_new_friend()
            user_friends.append(NewFriend)
            CurrentUser.set_new_friend(NewFriend)

        # Add a new gift idea
        elif option == 2:
            # create new gift instance
            NewGift = add_new_gift()
            # get name of friend
            print("Enter friend's first and last name with a space in between.")
            find_friend = input("Use exact name as originally entered: ")
            name_validation(find_friend)
            find_friend = find_friend.title()
            friend_first, friend_last = find_friend.split()
            # add NewGift to Friend
            try:
                for friend in user_friends:
                    if (friend_first == friend.first_name) and\
                       (friend_last == friend.last_name):
                        friend.set_new_gift_on_giftlist(NewGift)
                        friend_gifts.append(NewGift)
                        print("Added the gift to your friends gift list!")
                        found = True
                if not found:
                    raise ValueError("Could not find friend, gift not added.")
            except KeyError as error:
                print(error)
            else:
                print("Back to the main menu.")

        # List of friends
        elif option == 3:
            try:
                lst_of_friends = CurrentUser.prnt_friend_lst()
                print(lst_of_friends)
                filename = open("friends.txt", "w")
                for item in CurrentUser.get_friend_lst():
                    s = (str(item)) + "\n"
                    filename.write(s)
                filename.close()
                "Printing list of friends to file named friends.txt"
            except IOError as error:
                print(error)
            else:
                print("Back to the main menu.")

        # Get list of gifts for a friend
        elif option == 4:
            print("Enter friend's first and last name with a space in between.")
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
                        found = True
                if not found:
                    raise ValueError("Could not find friend.")
            except KeyError as error:
                print(error)
            else:
                print("Back to the main menu.")
        # Update user name or email
        elif option == 5:
            print("If you don't need to update a field, just press enter.")
            try:  
                name = (str(input("Otherwise, enter your first and last name "
                                "separated by a space, omit prefixes and "
                                "suffixes: ")))
                email = (str(input("Enter your email address: ")))
                if name:
                    name_validation(name)
                if (email) and (not su.is_email(email)):  # check that it is email
                    raise ValueError("You did not enter an email address.")
                OldUser = CurrentUser
            except ValueError as error:
                print(error)
            else:
                if (name) and (email):
                    first, last = name.title().split()
                    CurrentUser.set_updated_user(**{'first_name': first,
                                                    'last_name': last,
                                                    'email': email})
                elif name:
                    first, last = name.title().split()
                    CurrentUser.set_updated_user(**{'first_name': first,
                                                    'last_name': last})
                elif email:
                    CurrentUser.set_updated_user(**{'email': email})
                for user in end_users:
                    if user == OldUser:
                        end_users.remove(OldUser)
                        end_users.append(CurrentUser)
                print("Information updated!")
                print(repr(CurrentUser))

        # Exit
        elif option == 6:
            choice = 6

    print("Thank you for using Birthday Buddy.")
    print("Exiting.")


if __name__ == '__main__':
    welcome()
    current_user = sign_up_new_user()
    main(current_user)
