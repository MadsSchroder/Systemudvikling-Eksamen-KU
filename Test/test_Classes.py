from unittest import TestCase
from Models.Classes import Classes

classes = Classes(10, "Københavns Universitet", "08:00:00", "12:00:00", "Programmering")

class TestClasses(TestCase):
    def test_get_id(self):
        self.assertEqual(classes.get_id(), 10)
        self.assertNotEqual(classes.get_id(), "10")

    def test_set_id(self):
        classes.set_id("10")
        self.assertEqual(classes.get_id(), 10)
        self.assertNotEqual(classes.get_id(), "10")

    def test_get_location(self):
        self.assertEqual(classes.get_location(), "Københavns Universitet")

    def test_set_location(self):
        classes.set_location("Odense Universitet")
        self.assertEqual(classes.get_location(), "Odense Universitet")


