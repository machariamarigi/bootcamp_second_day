""" Python OOP"""


class Employee(object):
    """Base Class for an Employee"""

    def pay_rise(self):
        pass

    def company_email(self):
        pass


class Developer(Employee):
    """A class for developer employees"""

    raise_amount = 1.05

    def __init__(self, firstname, lastname, pay, language):
        self.firstname = firstname
        self.lastname = lastname
        self.name = "{0} {1}".format(firstname, lastname)
        self.pay = pay
        self.language = language

    def company_email(self):
        return "{0}.{1}-dev@company.com".format(
            self.firstname, self.lastname).lower()

    # Encapsulated method
    def __change_language(self, language):
        self.language = language
        return self.language


class Manager(Employee):
    """A class for manager employees"""

    raise_amount = 1.10

    def __init__(self, firstname, lastname, pay, employees=None):
        self.firstname = firstname
        self.lastname = lastname
        self.name = "{0} {1}".format(firstname, lastname)
        self.pay = pay
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def company_email(self):
        return "{0}.{1}-manager@company.com".format(
            self.firstname, self.lastname).lower()


# a fun way to see polymorphism in action
def polymorphism():
    employees = [
        Manager('Poly', 'Manger', 100),
        Developer('Poly', 'Dev', 100, 'Javascript')]

    for employee in employees:
        print('{0} : {1}'.format(employee.name, employee.company_email()))

