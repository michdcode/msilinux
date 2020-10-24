import itertools
from datetime import date, datetime


class Person(object):
    """Person class is a base class for users and friends."""

    # counter for assignment of UUID's, list of UUID's
    _UUID_counter = itertools.count()
    _UUID_lst = []

    def __init__(self, first, last):
        """This constructor creates a person object."""
        self.first_name = first
        self.last_name = last
        self._UUID = self.__set_UUID()
        self._UUID_lst.append(self._UUID)

    def __set_UUID(self):
        """This private method assigns a UUID to each Person object."""
        self.new_UUID = next(self._UUID_counter)
        return self.new_UUID

    def _get_UUID_lst(self):
        """ This will return a list of all UUIDS"""
        return self._UUID_lst


class User(Person):
    """User is subclass of Person, who is tracking gift ideas."""

    def __init__(self, first, last, email):
        """Creates a User object, which is a subclass of Person."""

        Person.__init__(self, first, last)
        self.email = email
        self._friend_lst = []

    def set_updated_user(self, **kwargs):
        """Allows updates to User attributes."""

        # in real life would not update password this way
        for k, v in kwargs.items():
            setattr(self, k, v)
        return 'updated user info.'

    def set_new_friend(self, friend):
        """Allows user to add Friend object to friend list. """

        self._friend_lst.append(friend)
        return "Added new friend to list"

    def get_friend_lst(self):
        """Returns the entire list of friends for a user."""

        return self._friend_lst

    def prnt_friend_lst(self):
        """Prints friend list in readable format."""

        print("You have {} friend(s). Here is a list:"
              .format(len(self._friend_lst)))
        for count, friend in enumerate(self._friend_lst, 1):
            print(count, friend)

    def get_friend(self, first, last):
        """Finds friend on friend list by first and last name."""

        for friend in self._friend_lst:
            if (first == friend.first_name) and\
               (last == friend.last_name):
                return friend
        else:
            return "Friend not found."

    def __repr__(self):
        """Returns offical representation of User object."""
        return repr('Name: ' + self.first_name + ' ' + self.last_name
                    + ', email: ' + self.email)


class Friend(Person):
    """Friend is subclass of Person,potential gift recipient."""

    def __init__(self, first, last, month, day, year):
        """Creates a Friend object, which is subclass of Person."""

        Person.__init__(self, first, last)
        self.birthdate = date(year=year, month=month, day=day)
        self.birthdatestr = self.birthdate.strftime("%B %d, %Y")
        today = date.today()
        this_year_birthday = date(today.year, month, day)
        self.days_to_birthday = (abs(this_year_birthday - today)).days
        self.days_to_birthdaystr = str(self.days_to_birthday)
        self._gift_lst = []

    def set_updated_friend(self, **kwargs):
        """Allows updates to Friend attributes."""

        for k, v in kwargs.items():
            setattr(self, k, v)
        return 'updated friend info.'

    def set_new_gift_on_giftlist(self, gift):
        """Allows user to add a Gift object to gift list for friend."""

        self._gift_lst.append(gift)
        return "added new gift to giftlist"

    def get_gift_lst(self):
        """Returns the entire gift list of friend."""

        return self._gift_lst

    def print_gift_lst(self):
        """Prints gift list in readable format."""

        for count, gift in enumerate(self._gift_lst, 1):
            print(count, gift)

    def __repr__(self):
        """Returns offical representation of Friend object."""

        return repr('Name: ' + self.first_name + ' ' + self.last_name
                    + ', Birthday: ' + self.birthdatestr
                    + ', Days to Birthday: '
                    + self.days_to_birthdaystr)


class Gift():
    """Generic class to store gift information."""

    def __init__(self, name, URL, notes=""):
        """Creates a gift object."""

        self.idea = name
        self.URL = URL
        self.notes = notes  # notes are optional so added a default
        self.gift = {'Idea': self.idea, 'URL': self.URL, 'Notes': self.notes}

    def set_updated_gift_info(self, **kwargs):
        """Allows update to Gift object."""

        for k, v in kwargs.items():
            setattr(self, k, v)
        return 'updated friend info.'

    def __repr__(self):
        return repr('Idea: ' + self.idea + ', URL: ' + self.URL +
                    ', Notes: ' + self.notes)

