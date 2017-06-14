import unittest

from employee import Employee, Developer, Manager


class DeveloperTestCase(unittest.TestCase):
    """Class to Test Developer Class"""
    def setUp(self):
        self.developer = Developer('Test', 'Name', 100, 'Python')

    def test_developer_instance(self):
        self.assertEqual(
            self.developer.language,
            'Python',
            'Class not instantiating properly')

    def test_company_email(self):
        self.assertEqual(
            self.developer.company_email(),
            'test.name-dev@company.com',
            'Something wrong with the company_email method'
        )

    def test_encapsulation(self):
        with self.assertRaises(AttributeError):
            self.developer.__change_language('C++')


class ManagerTestCase(unittest.TestCase):
    """Class to Test Manager Class"""
    def setUp(self):
        self.manager = Manager('Test', 'Name', 100)
        self.employee = Developer('Test1', 'Name1', 100, 'Java')

    def test_manager_instance(self):
        self.assertEqual(
            self.manager.employees,
            [],
            'Class not instantiating properly')

    def test_add_employee(self):
        initial_employees = self.manager.employees
        self.manager.add_employee(self.employee)
        employee_added = 2 - len(initial_employees)
        self.assertEqual(
            employee_added, 1, 'Something wrong with the add_employee method')

    def test_company_email(self):
        self.assertEqual(
            self.manager.company_email(),
            'test.name-manager@company.com',
            'Something wrong with the company_email method'
        )


if __name__ == "__main__":
    unittest.main()
