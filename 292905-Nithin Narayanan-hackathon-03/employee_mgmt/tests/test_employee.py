import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    # Test for if employye get created

    def test_employee_creation(self):
        emp = Employee("Alice", "HR", "Manager", 5000, 500, 300)
        self.assertEqual(emp.name, "Alice")
        self.assertEqual(emp.department, "HR")
        self.assertEqual(emp.designation, "Manager")
        self.assertEqual(emp.gross_salary, 5000)
        self.assertEqual(emp.tax, 500)
        self.assertEqual(emp.bonus, 300)

        # Id generation
    def test_id_is_generated(self):
        emp = Employee("Bob", "IT", "Engineer", 4000, 400, 200)
        self.assertTrue(emp.id)  

    # Net salary calc
    def test_net_salary_calculation(self):
        emp = Employee("Charlie", "Sales", "Rep", 6000, 600, 100)
        expected_net = 6000 - 600 + 100
        self.assertEqual(emp.net_salary, expected_net)


if __name__ == "__main__":
    unittest.main()
