import unittest

from employee import Employee


class EmployeeTestCases(unittest.TestCase):
    """Class to test Employee class"""
    def setUp(self):
        self.employee = Employee('Test', 'Name', 0)

    def test_employee_instance(self):
        self.assertEqual(
            self.employee.name,
            'Test Name',
            'Class not instantiating properly')


if __name__ == "__main__":
    unittest.main()
