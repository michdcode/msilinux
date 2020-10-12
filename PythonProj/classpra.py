# Random Note: CTRL + SHIFT + L to make change to all occurences of selection

class Duck():
    # functions are overloaded but have diff num of args
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name

"""
>>> fowl = Duck("Howard")
>>> fowl.name
inside the getter
'Howard'
>>> fowl.name = "Donald"
inside the setter
>>> fowl.name
inside the getter
'Donald'
"""


class A():
    # classmethods act on entire class, not just an instance
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")
"""
>>> myGr = A()
>>> easy_A = A()
>>> breezy_A = A()
>>> A.kids()
A has 3 little objects.
>>> myGr.exclaim()
I'm an A!
>>> easy_A.exclaim()
I'm an A!
"""

class Word():
    # this is a magic method
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
"""
>> first = Word("ha")
>>> second = Word("HA")
>>> third = Word('eh')
>>> first == second
True
>>> first == third
False
>>> second == third
False
"""



class distance:
    def __init__(self, x=None,y=None):
        self.ft=x
        self.inch=y
    def __add__(self, x):
        # this new temp object is what is acted upon to create answer
        temp=distance() # it's an empty object
        # in example below, self is d1 & x is d2
        temp.ft=self.ft+x.ft
        temp.inch=self.inch+x.inch
        # this just does a conversion to a foot if > 12 inches
        if temp.inch>=12:
            temp.ft+=1
            temp.inch-=12
            return temp
    def __str__(self):
        return 'ft:'+str(self.ft)+' in: '+str(self.inch)
"""
>>> d1 = distance(3,10)
>>> d2 = distance(4,4)
>>> print("d1= {} d2={}".format(d1, d2))
d1= ft:3 in: 10 d2=ft:4 in: 4
>>> d3 = d1 + d2
>>> print(d3)
ft:8 in: 2
"""




