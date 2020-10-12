class StudentInfo(object):
    """Simple Student class"""
    def __init__(self, first='', last='', id=0):
        """NOTE: an __init__ method can NOT have a return statement."""
        self.first_name_str = first
        self.last_name_str = last
        self.id_int = id
    
    def __str__(self):
        return"{} {}, ID:{}".format\
               (self.first_name_str, self.last_name_str, self.id_int)


    def update(self, first='', last='', id =0):
        if first:
            self.first_name_str = first
        if last:
            self.last_name_str = last
        if id:
            self.id_int = id



            """
>>> michelle = StudentInfo("Michelle", "Blackman", 100220)
>>> print(michelle)
Michelle Blackman, ID:100220
>>> print(michelle.__class__)
<class '__main__.StudentInfo'>
# the .__class__ will show the template it was created from
"""

class MyClass(object):
    def __init__(self, param1=0):
        print("in constructor")
        self.value = param1
    def __str__(self):
        print('in str')
        return "value is: {}".format(str(self.value))
    def __add__(self, param2):
        """remember that param 2 needs to be a MyClass object"""
        print("in add")
        result = self.value + param2.value
        return MyClass(result)

"""
>>> inst1 = MyClass(27)
in constructor
>>> print(inst1)
in str
value is: 27
>>> a_sum = inst1 + inst1
in add
in constructor
>>> print(a_sum)
in str
value is: 54
"""


https://stackoverflow.com/questions/1045344/how-do-you-create-an-incremental-id-in-a-python-class/54318273#54318273


https://www.vitoshacademy.com/hashing-passwords-in-python/
