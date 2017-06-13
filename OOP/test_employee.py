import unittest

from employee import Employee, Developer


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

    def test_employee_instance(self):
        self.assertEqual(
            self.developer.language,
            'Python',
            'Class not instantiating properly')


if __name__ == "__main__":
    unittest.main()
