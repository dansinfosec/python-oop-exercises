# Imagine an address book. We could create a Person class with instance
# variables for name , address , phoneNumber , and birthday . We could create
# as many objects from the Person class as we want, one for each person
# we know. The instance variables in each Person object would contain
# different values. We could then write code to search through all the
# Person objects and retrieve information about the one or ones we are
# looking for.


class Person(object):
    """docstring for Person"""

    def __init__(self, arg):
        super(Person, self).__init__()
        self.arg = arg
