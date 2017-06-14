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

    def company_email(self):
        return "{0}.{1}@company.com".format(
            self.firstname, self.lastname).lower()

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.firstname,
                                                 self.lastname,
                                                 self.pay)


class Developer(Employee):
    """A class for developer employees"""

    def __init__(self, firstname, lastname, pay, language):
        super().__init__(firstname, lastname, pay)
        self.language = language


class Manager(Employee):
    """A class for manager employees"""

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)