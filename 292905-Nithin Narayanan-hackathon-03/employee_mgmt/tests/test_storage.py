import unittest
import os
import pickle
from storage import Storage
from employee import Employee

class TestStorage(unittest.TestCase):

    def setUp(self):
        self.test_filename = "test_employees.pkl"
        self.storage = Storage(self.test_filename)
        self.test_data = [
            Employee("Alice", "HR", "Manager", 50000, 5000, 2000).to_dict(),
            Employee("Bob", "IT", "Engineer", 60000, 6000, 2500).to_dict()
        ]

    def tearDown(self):
        # Clean up test file if it exists
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_save_creates_file(self):
        self.storage.save(self.test_data)
        self.assertTrue(os.path.exists(self.test_filename))


    def test_load_from_missing_file_returns_empty_list(self):
        # Remove file if it exists
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
        loaded = self.storage.load()
        self.assertEqual(loaded, [])

    def test_load_from_invalid_pickle_returns_empty_list(self):
        # Create an invalid file
        with open(self.test_filename, 'w') as f:
            f.write("not a pickle file")
        loaded = self.storage.load()
        self.assertEqual(loaded, [])

if __name__ == '__main__':
    unittest.main()
