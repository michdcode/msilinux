# Standard Library Imports 
import sys
import string_utils as su

# Local imports
from helper_functions import *

# variables and data structures

end_users = []
user_friends = []
friend_gifts = []

choice = 0

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
        name_validation(name)
        if not su.is_email(email):  # check that it is email
            raise ValueError("You did not enter an email address.")
    except ValueError as error:
        print(error)
    else:
        break


# clean data and create new user
if len(end_users) > 1: 
    for existing_users in end_users[0]:
        if existing_users == name:
            print("That user already exists.")
            break
NewUser = add_new_user(name, email)
user_key = NewUser.first_name + " " + NewUser.last_name
end_users.append({user_key: NewUser})
CurrentUser = NewUser

while choice is not 99:
    display_main_menu()
    option = get_user_option()

    # Add a new friend
    if option == 1:
        NewFriend = add_new_friend()
        friend_key = NewFriend.first_name + " " + NewFriend.last_name
        user_friends.append({friend_key: NewFriend})
        CurrentUser.set_new_friend(NewFriend)
    # Add a new gift idea
    elif option == 2:
        print("Enter the first and last name with a space in between."
              "of the friend that you have a gift idea for.")
        find_friend = input("Use exact name as originally entered: ")
        name_validation(find_friend)
        find_friend = find_friend.title()
        if len(user_friends) < 1:
            print("Enter a friend before adding a gift.")
            
        finder = False
        while finder is False:
            for friends in user_friends[0]:
                if friends == find_friend:
                    print("friend found")
                    finder = True
            break
        if not finder:
            print("friend not found.")
            break
        NewGift = add_new_gift()
        friend_gifts.append({NewGift.idea: NewGift})
        user_friends[0][find_friend].set_new_gift_on_giftlist(NewGift)
#>>> user_friends[0]['Ann Lum']._gift_lst
#['Idea: Pears, URL: https://www.harryanddavid.com/h/gift-baskets-tower-boxes/all-occasion-gift-boxes/13488, Notes: She loves these harry and david peaches']


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
    # elif option == 4:
        # if len(user_friends) < 1:
        #     print("You do not have any friends")
        #     break
        # print("Enter the first and last name with a space in between.")
        # find_friend = input("Use exact name as originally entered: ")
        # name_validation(find_friend)
        # find_friend = find_friend.title()
        # for friends in user_friends[0]
    #     find_friend_gifts = 
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
    elif option == 99:
        choice = 99

if choice == 99:
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
