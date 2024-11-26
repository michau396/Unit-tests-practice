import unittest
import os
from importer import studentAdd, studentBaseExport, studentBaseImport


class TestStudentOperations(unittest.TestCase):
    def setUp(self):
        # example list of students
        self.students = [
            [1, "Maria", "Krawczyk"],
            [2, "Krzysztof", "Krawczyk"],
            [3, "Jan", "Krawczyk"],
            [4, "Alojzy", "Kołodziejski"],
        ]
        self.test_file = "test_students_list.csv"

    def test_student_add(self):
        # adding new student 
        studentAdd("Anna", "Nowak", self.students)
        self.assertEqual(len(self.students), 5)
        self.assertEqual(self.students[-1], [5, "Anna", "Nowak"])

    def test_student_base_export(self):
        # export student base 
        studentBaseExport(self.students, self.test_file)
        self.assertTrue(os.path.exists(self.test_file)) 
        with open(self.test_file) as f:
            lines = f.readlines()
        self.assertEqual(len(lines), len(self.students) + 1) 
        self.assertEqual(lines[1].strip(), "1,Maria,Krawczyk")

    def test_student_base_import(self):
        # export then import of students base
        studentBaseExport(self.students, self.test_file)
        imported_students = studentBaseImport(self.test_file)
        self.assertEqual(imported_students, self.students)

    def tearDown(self):
        # removing test files
        if os.path.exists(self.test_file):
            os.remove(self.test_file)


if __name__ == "__main__":
    unittest.main(exit=False)
