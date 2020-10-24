import unittest
from my_classes import *
import sys


class test_Person_class(unittest.TestCase):
    """Tests for Person class attributes and methods."""
    def test_person_class(self):
        James = Person("James", "Bond")
        self.assertIsInstance(James, Person)
        self.assertEqual(James.last_name, "Bond")
        self.assertEqual(James.first_name, "James")
        self.assertIsNotNone(James._UUID, "problem")
        self.assertIsNotNone(James._get_UUID_lst)


class test_User_class(unittest.TestCase):
    """Tests for User class attributes and methods."""
    def test_user_class(self):
        Jane = User("Jane", "Moneypenny", "jane.moneypenny@misix.org")
        Andrew = Friend("Andrew", "Bond", 2, 3, 1940)
        Monique = Friend("Monique", "Delacroix", 3, 4, 1950)
        self.assertIsInstance(Jane, User)
        self.assertEqual(Jane.first_name, "Jane")
        self.assertEqual(Jane.last_name, "Moneypenny")
        self.assertEqual(Jane.email, "jane.moneypenny@misix.org")
        Jane.set_updated_user(**{"first_name": "Janey"})
        self.assertEqual(Jane.first_name, "Janey")
        Jane.set_new_friend(Andrew)
        Jane.set_new_friend(Monique)
        self.assertIn(Andrew, Jane._friend_lst, "Problem")
        self.assertIn(Monique, Jane._friend_lst, "Problem")
        self.assertIsNotNone(Jane.get_friend_lst, "Problem")
        self.assertIsNotNone(Jane.prnt_friend_lst, "Problem")
        self.assertEqual(Jane.get_friend("Andrew", "Bond"), Andrew, "Problem")
        self.assertEqual(Jane.get_friend("Andy", "Bon"), "Friend not found.",
                         "Problem")
        self.assertIsNotNone(Jane.__repr__, "Problem")


class test_Friend_class(unittest.TestCase):
    """Tests for Friend class attributes and methods."""
    def test_friend_class(self):
        Andrew = Friend("Andrew", "Bond", 2, 3, 1940)
        self.assertIsInstance(Andrew, Friend)
        self.assertEqual(Andrew.first_name, "Andrew")
        self.assertEqual(Andrew.last_name, "Bond")
        self.assertEqual(Andrew.birthdate, date(1940, 2, 3))
        self.assertEqual(Andrew.birthdatestr, 'February 03, 1940')
        # New few functions only correct on 10/24/2020
        self.assertEqual(Andrew.days_to_birthday, 264)
        self.assertEqual(Andrew.days_to_birthdaystr, '264')
        self.assertEqual(len(Andrew._gift_lst), 0)
        Andrew.set_updated_friend(**{"first_name": "Andy"})
        self.assertEqual(Andrew.first_name, "Andy")
        shoes = Gift('Nike', 'https://www.nike.com', 'He likes to workout')
        hat = Gift('Patroits', 'https://www.patriots.com',
                   'He loves new England')
        self.assertEqual(Andrew.set_new_gift_on_giftlist(shoes),
                         'added new gift to giftlist')
        self.assertEqual(Andrew.set_new_gift_on_giftlist(hat),
                         'added new gift to giftlist')
        self.assertEqual(len(Andrew._gift_lst), 2)
        self.assertIsNotNone(Andrew.get_gift_lst, "Problem")
        self.assertIsNotNone(Andrew.print_gift_lst, "Problem")
        self.assertIsNotNone(Andrew.__repr__, "Problem")


class test_Gift_class(unittest.TestCase):
    """Tests for Gift class attributes and methods."""
    def test_gift_class(self):
        Shoes = Gift('Nike', 'https://www.nike.com', 'He likes to workout')
        self.assertIsInstance(Shoes, Gift)
        self.assertEqual(Shoes.idea, "Nike")
        self.assertEqual(Shoes.URL, 'https://www.nike.com')
        self.assertEqual(Shoes.notes, 'He likes to workout')
        Shoes.set_updated_gift_info(**{"notes": "Running is his fun."})
        self.assertEqual(Shoes.notes, "Running is his fun.")


if __name__ == "__main__":
    unittest.main()

"""
Results:
(env) michd@DESKTOP-GNV4GB8:~/Code/PythonProj/Final_Pro$ coverage run --source=. --omit=env/* testing.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK

(env) michd@DESKTOP-GNV4GB8:~/Code/PythonProj/Final_Pro$ coverage report -m
Name            Stmts   Miss  Cover   Missing
---------------------------------------------
my_classes.py      76     11    86%   26, 56, 61-64, 78, 113, 118-119, 124, 149
testing.py         64      1    98%   81
---------------------------------------------
TOTAL             140     12    91%

NOTE: There are tests for each of the functions and attributes in my_classes.py, so
I am unsure why it lists certain lines as missing testing coverage. Thank you.
"""
