from unittest import TestCase
from Models.Classes import Classes
from Models.Changes import Changes

classes = Classes("10", "Københavns Universitet", "08:00:00", "12:00:00", "Programmering")
changes = Changes("11", "Københavns Universitet", "2022-05-23", "08:00:00", "12:00:00", "10")
class TestClasses(TestCase):
    def test_get_id(self):
        self.assertEqual(classes.get_id(), 10)
        self.assertNotEqual(classes.get_id(), "10")

    def test_set_id(self):
        classes.set_id(int("10"))
        self.assertEqual(classes.get_id(), 10)
        self.assertNotEqual(classes.get_id(), "10")

    def test_get_location(self):
        self.assertEqual(classes.get_location(), "Københavns Universitet")

    def test_set_location(self):
        classes.set_location("Odense Universitet")
        self.assertEqual(classes.get_location(), "Odense Universitet")

    def test_changes_get_id(self):
        self.assertEqual(changes.get_id(), 11)

    def test_changes_get_date(self):
        self.assertEqual(changes.get_date(), "2022-05-23")

    def test_changes_get_courseid(self):
        self.assertEqual(changes.get_courseid(), 10)



