import unittest
from employee import Employee
from employee_manager import EmployeeManager

class TestEmployeeManager(unittest.TestCase):

    def setUp(self):
        self.manager = EmployeeManager()

    def test_add_employee(self):
        emp = self.manager.add_employee("Alice", "HR", "Manager", 50000, 5000, 2000)
        self.assertEqual(len(self.manager.get_all_employees()), 1)
        self.assertEqual(emp.name, "Alice")
        self.assertEqual(emp.net_salary, 50000 - 5000 + 2000)

    def test_get_all_employees(self):
        self.manager.add_employee("Bob", "Finance", "Analyst", 40000, 3000, 1500)
        self.manager.add_employee("Carol", "IT", "Engineer", 60000, 6000, 2500)
        employees = self.manager.get_all_employees()
        self.assertEqual(len(employees), 2)

    def test_find_by_id(self):
        emp = self.manager.add_employee("Dan", "Marketing", "Executive", 45000, 4000, 1000)
        found = self.manager.find_by_id(emp.id)
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "Dan")

    def test_delete_employee(self):
        emp = self.manager.add_employee("Eve", "Sales", "Lead", 47000, 3500, 1200)
        deleted = self.manager.delete_employee(emp.id)
        self.assertTrue(deleted)
        self.assertEqual(len(self.manager.get_all_employees()), 0)

    def test_delete_invalid_id(self):
        result = self.manager.delete_employee("nonexistent-id")
        self.assertFalse(result)

    def test_load_employees_from_dict(self):
        data = [
            {
                "id": "test-id",
                "name": "Frank",
                "department": "Support",
                "designation": "Rep",
                "gross_salary": 30000,
                "tax": 2000,
                "bonus": 1000,
                "net_salary": 29000
            }
        ]
        self.manager.load_employees(data)
        self.assertEqual(len(self.manager.get_all_employees()), 1)
        self.assertEqual(self.manager.get_all_employees()[0].name, "Frank")

    def test_to_dict_list(self):
        self.manager.add_employee("Grace", "Admin", "Clerk", 28000, 1500, 800)
        data = self.manager.to_dict_list()
        self.assertEqual(type(data), list)
        self.assertEqual(data[0]["name"], "Grace")

if __name__ == '__main__':
    unittest.main()
