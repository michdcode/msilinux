import itertools
from datetime import date, datetime


class Person():
    """This is a generic class for any user or gift recipient."""

    # counter for assignment of UUID's, list of UUID's
    _UUID_counter = itertools.count()
    _UUID_lst = []

    
    def __init__(self, first="", middle="", last=""):
        """This is the recipe for all Person objects"""
        self.first_name = first
        self.middle_name = middle
        self.last_name = last
        self.UUID = self.__set_UUID()
        self._UUID_lst.append(self.UUID)
        
    
    def __set_UUID(self):
        """This private method assigns a UUID to each Person object."""
        self.new_UUID = next(self._UUID_counter)
        return self.new_UUID


    def __get_UUID_lst(self):
        """ This will return a list of all UUIDS"""
        return self._UUID_lst
    
    
    def set_name_change(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        return 'updated name.'

        # to use: >>> michd.set_name_change(**{'first_name':'Michelle', 'last_name':'Dicks'})
        # CAREFUL - when spelling keys 
        """
        >>> michd.set_name_change(**{'first_Name': 'Michelle'})
        updated name.
        >>> michd.first_name
        'Michaelle'
        >>> michd.set_name_change(**{'first_name': 'Michelle'})
        updated name.
        >>> michd.first_name
        'Michelle'
        """
        # need to make sure to use upper/lower, etc when setting and retrieving name


    
class User(Person):
    _friend_lst = []
    
    
    def __init__(self, first="", middle="", last=""):
        Person.__init__(self, first, middle, last)


    def user_info(self, email='', pwd='', hint={}):
        self.email = email
        self.__password = pwd
        self.hint = hint


    def __set_new_pwd(self, new_pwd):
        self.__password = new_pwd
    

    def set_new_friend(self, friend):
        self._friend_lst.append(friend)
        return "added new friend to list"


    def get_friend_lst(self):
        return self._friend_lst


    def prnt_friend_lst(self):
        print("You have {} friend(s). Here is a list:"\
            .format(len(self._friend_lst)))
        for friend in self._friend_lst:
            print("Name: {} {} {}, Birthday: {}, Days to birthday: {}"\
                .format(friend.first_name, friend.middle_name,\
                        friend.last_name, friend.birthdatestr, 
                        friend.days_to_birthdaystr))


    def get_friend(self, first, middle, last):
        for friend in self._friend_lst:
            if (first == friend.first_name) and\
               (middle == friend.middle_name) and\
               (last == friend.last_name):
               return friend
        else:
            return "Friend not found."

    

    """
    >>> bubba.set_new_pwd("puppies")
    >>> bubba.password
    #'puppies'
    https://www.pythonanywhere.com 
    >>> bubba = User("Bubba", "Jerome", "Wallace")
    >>> bubba.UUID
    2
    >>> bubba.user_info("bubba@mail.com", "idjsos", {"What is your favorite number": 43})
    >>> bubba.password
    'idjsos'
    >>> bubba.hint.values()
    dict_values([43])
    >>> bubba.hint['What is your favorite number']
    43
    >>> michelle = User("michelle", "therese", "dicks")
    >>> annette = Friend("Annette", "Heller", "Lum")
    >>> annette.friend_info('annlum@email.com', 4, 18, 1970)
    >>> michelle.set_new_friend(annette)
    added new friend to list
    >>> michelle.get_friend_lst()
    [<__main__.Friend object at 0x7fffbcdf4c18>]
    >>> michelle.prnt_friend_lst()
    Annette 1970-04-18
    """

class Friend(Person):
    def __init__(self, first="", middle="", last=""):
        Person.__init__(self, first, middle, last)


    def friend_info(self, email='', month=1, day = 1, year=1):
        # if a year is not available use this year's date
        self.email = email
        self.birthdate = date(year=year, month=month, day=day)
        self.birthdatestr = self.birthdate.strftime("%B %d, %Y")
        today = date.today()
        this_year_birthday = date(today.year, month, day)
        self.days_to_birthday = (abs(this_year_birthday - today)).days
        self.days_to_birthdaystr = str(self.days_to_birthday)
             

    def set_updated_friend_info(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        return 'updated friend info.'


    def __repr__(self):
        return repr('Name: ' + self.first_name + ' ' + self.last_name \
                    + ', birthday: ' + self.birthdatestr \
                    + ', days to birthday: ' + self.days_to_birthdaystr)
    """
        >>> alice = Friend("Alice", "In", "Wonderland")
        >>> alice.friend_info('alice@email.com', 7, 12, 1982)
        >>> alice.birthdate
        datetime.date(1982, 7, 12)
        >>> alice.days_to_birthday
        90
        
        >>> annette = Friend("Annette", "Heller", "Lum")
        >>> annette.friend_info('annlum@email.com', 4, 18, 1970)
        >>> repr(annette)
        "'Name:Annette Lum, birthday: April/18/1970, days to birthday: 176'"
    """

    
