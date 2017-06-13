import unittest

from employee import Employee


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
        self.assertEqual(final_pay, 105)


if __name__ == "__main__":
    unittest.main()
