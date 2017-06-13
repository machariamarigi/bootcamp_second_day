""" Python OOP"""


class Employee(object):
    """Base Class for an Employee"""

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.name = "{0} {1}".format(firstname, lastname)
        self.pay = pay
