""" Python OOP"""


class Employee(object):
    """Base Class for an Employee"""

    raise_amount = 1.05

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.name = "{0} {1}".format(firstname, lastname)
        self.pay = pay

    def pay_rise(self):
        self.pay = self.pay * self.raise_amount
