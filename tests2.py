import unittest
from datetime import datetime
from pythonobecnosc import mark_attendance, display_students, update_attendance

class TestAttendanceOperations(unittest.TestCase):
    def setUp(self):
        # example list of students
        self.students = [
            [1, 'Jan', 'Kowalski', []],
            [2, 'Anna', 'Nowak', []],
            [3, 'Piotr', 'Zieliński', []],
            [4, 'Maria', 'Wójcik', []],
        ]

    def test_mark_attendance(self):
        # test marking attendance
        mark_attendance(self.students, 1, 'Obecny', '2024-11-19')
        expected = {'data': '2024-11-19', 'status': 'Obecny'}
        self.assertIn(expected, self.students[0][3])
        print("Test for marking attendance passed.")

    def test_update_attendance_existing_date(self):
        # test updating attendance for an existing date
        mark_attendance(self.students, 1, 'Obecny', '2024-11-19')
        update_attendance(self.students, 1, 'Nieobecny', '2024-11-19') 
        expected = {'data': '2024-11-19', 'status': 'Nieobecny'}
        self.assertIn(expected, self.students[0][3])
        print("Test for updating existing attendance passed.")

    def test_update_attendance_missing_student(self):
        # test updating attendance for a non-existing student
        with self.assertRaises(Exception) as context:
            update_attendance(self.students, 99, 'Obecny', '2024-11-19')
        self.assertEqual(str(context.exception), "Student not found with ID: 99")

    def test_display_students(self):
        # test displaying the student list
        mark_attendance(self.students, 1, 'Obecny', '2024-11-19')
        with self.assertLogs() as captured:
            display_students(self.students)
        self.assertTrue(any("Jan Kowalski" in message for message in captured.output))
        self.assertTrue(any("Data: 2024-11-19 - Status: Obecny" in message for message in captured.output))
        print("Test for displaying students passed.")

    def tearDown(self):
        self.students = []

# run the tests
if __name__ == "__main__":
    unittest.main(exit=False)


