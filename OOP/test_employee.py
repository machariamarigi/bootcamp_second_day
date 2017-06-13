import unittest

from employee import Employee, Developer, Manager


class EmployeeTestCases(unittest.TestCase):
    """Class to test Employee class"""
    def setUp(self):
        self.employee = Employee('Test', 'Name', 100)

    def test_employee_instance(self):
        self.assertEqual(
            self.employee.name,
            'Test Name',
            'Class not instantiating properly')

    def test_employee_pay_rise(self):
        initial_pay = self.employee.pay
        self.employee.pay_rise()
        final_pay = self.employee.pay
        self.assertEqual(
            final_pay, 105, 'Something wrong with the pay_rise method')


class DeveloperTestCase(unittest.TestCase):
    """Class to Test Developer Class"""
    def setUp(self):
        self.developer = Developer('Test', 'Name', 100, 'Python')

    def test_developer_instance(self):
        self.assertEqual(
            self.developer.language,
            'Python',
            'Class not instantiating properly')

    def test_inheriance(self):
        initial_pay = self.developer.pay
        self.developer.pay_rise()
        final_pay = self.developer.pay
        self.assertEqual(
            final_pay, 105, 'Something wrong with the pay_rise method')


class ManagerTestCase(unittest.TestCase):
    """Class to Test Manager Class"""
    def setUp(self):
        self.manager = Manager('Test', 'Name', 100)
        self.employee = Employee('Test1', 'Name1', 100)

    def test_manager_instance(self):
        self.assertEqual(
            self.manager.employees,
            [],
            'Class not instantiating properly')

    def test_add_employee(self):
        initial_employees = self.manager.employees
        self.manager.add_employee(self.employee)
        final_employees = self.manager.employees
        difference = len(final_employees) - len(initial_employees)
        self.assertEqual(
            difference, 1, 'Something wrong with the add_employee method')


if __name__ == "__main__":
    unittest.main()
