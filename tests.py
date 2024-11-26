import unittest
import os
import csv
from textfileoperator import import_students, export_attendance

class TestTextFileOperator(unittest.TestCase):
    def setUp(self):
        # createating mock 
        self.test_import_file = "test_students_import.csv"
        self.test_export_file = "test_students_export.csv"
        self.mock_students = [
            ["1", "Andrzej", "Nowak", "Nieobecny"],
            ["2", "Anna", "Kowalska", "Obecny"],
        ]

        # writing mock data
        with open(self.test_import_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(self.mock_students)

    def test_valid_file_import(self):
        # testing import
        result = import_students(self.test_import_file)
        self.assertEqual(result, self.mock_students)
        print("Importing test is valid")

    def test_export_attendance(self):
        # testing export
        export_attendance(self.mock_students, self.test_export_file)
        with open(self.test_export_file, mode="r") as file:
            reader = csv.reader(file)
            rows = list(reader)
        # checking matching data
        expected = [["id", "name", "surname", "status"]] + self.mock_students
        self.assertEqual(rows, expected)
        print("Test for export attendance passed.")

    def tearDown(self):
        # removing test files
        if os.path.exists(self.test_import_file):
            os.remove(self.test_import_file)
        if os.path.exists(self.test_export_file):
            os.remove(self.test_export_file)

# running test
if __name__ == "__main__":
    unittest.main()
