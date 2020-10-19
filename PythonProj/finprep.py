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

    def __get_UUID_lst(self):
        """ This will return a list of all UUIDS"""
        return self._UUID_lst


class User(Person):
    """User is subclass of Person, who is tracking gift ideas."""

    def __init__(self, first, last, email):
        """Creates a User object, which is a subclass of Person."""

        Person.__init__(self, first, last)
        self.email = email
        # # in real life would not store password as plain text
        # self.__password = pwd
        # self.hint = hint
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
        # self.email = email
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
                    + ', Days to Birthday: ' + self.days_to_birthdaystr)


class Gift():
    """Generic class to store gift information."""

    def __init__(self, name, URL, notes):
        """Creates a gift object."""

        self.idea = name
        self.URL = URL
        self.notes = notes
        self.gift = {'Idea': self.idea, 'URL': self.URL, 'Notes': self.notes}

    def set_updated_gift_info(self, **kwargs):
        """Allows update to Gift object."""

        for k, v in kwargs.items():
            setattr(self, k, v)
        return 'updated friend info.'

    def __repr__(self):
        return repr('Idea: ' + self.idea + ', URL: ' + self.URL +
                    ', Notes: ' + self.notes)

    """
    michelle = User("michelle", "dicks", "michd@gmail.com", "passme", {'great_song': 'doves_cry'})
    michelle.set_updated_user(**{'first_name':'Michie', 'email':'michelle@gmail.com'})
    >>> michelle.set_updated_user(**{'password': 'frenchie'})
    'updated user info.'
    >>> michelle.password
    'frenchie'
    Bubba = User("Bubba", "Wallace", "bubs@gmail.com", "drive it fast", {'favorite number': 43})
    >>> Bubba.hint
    {'favorite number': 43}
    >>> Annette = Friend("Annette", "Lum", "annli@gmail.com", 4, 18, 1970)
    >>> repr(Annette)
    "'Name: Annette Lum, birthday: April 18, 1970, days to birthday: 182'"
    >>> shoes = Gift('Cole Haan', 'https://www.colehaan.com', 'She likes ballet, these slippers are perfect')
    >>> hat = Gift('Dodgers', 'https://www.dodgers.com', 'She and her husband like the Dodgers')
    >>> Annette.set_new_gift_on_giftlist(shoes)
    'added new gift to giftlist'
    >>> Annette.set_new_gift_on_giftlist(hat)
    'added new gift to giftlist'
    >>> Peter = Friend("Peter", "Express", "peter@gmail.com", 6, 26, 1985)
    >>> shoes = Gift('Nike', 'https://www.nike.com', 'He likes to workout')
    >>> Peter.set_new_gift_on_giftlist(shoes)
    'added new gift to giftlist'
    >>> hat = Gift('Patroits', 'https://www.patriots.com', 'He loves new England')
    >>> Peter.set_new_gift_on_giftlist(hat)
    'added new gift to giftlist'
    >>> Annette.print_gift_lst()
    1 'Idea: Cole Haan, URL: https://www.colehaan.com, Notes: She likes ballet, these slippers are perfect'
    2 'Idea: Dodgers, URL: https://www.dodgers.com, Notes: She and her husband like the Dodgers'
    >>> Peter.print_gift_lst()
    1 'Idea: Nike, URL: https://www.nike.com, Notes: He likes to workout'
    2 'Idea: Patroits, URL: https://www.patriots.com, Notes: He loves new England'
    >>> michelle.set_new_friend(Annette)
    'Added new friend to list'
    >>> michelle.set_new_friend(Alice)
    'Added new friend to list'
    >>> Bubba.set_new_friend(Peter)
    'Added new friend to list'
    >>> michelle.prnt_friend_lst()
    You have 2 friend(s). Here is a list:
    1 'Name: Annette Lum, birthday: April 18, 1970, days to birthday: 182'
    2 'Name: Alice Meng, birthday: March 31, 1968, days to birthday: 200'
    >>> Bubba.prnt_friend_lst()
    You have 1 friend(s). Here is a list:
    # CAREFUL - when spelling keys it will create a new k:v pair if you misspell the key
    # need to make sure to use upper/lower, etc when setting and retrieving name
    """
