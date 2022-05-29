from unittest import TestCase
from Models.Classes import Classes
from Models.Changes import Changes
from Models.Users import Users
from Models.Courses import Courses

users = Users("1", "Testperson", "kode", "Fornavn", "Efternavn", "test@testen.dk", "6543214321", "minadresse", "1")
classes = Classes("10", "Universitetsparken 4", "2022-05-29" ,"08:00:00", "12:00:00", "1", "Softwareudvikling")
changes = Changes("11", "Universitetsparken 5", "2022-05-30", "09:00:00", "15:00:00", "1")
courses = Courses("1", "2022", "København Universitet", "1", "Sundhed og Informatik", "1", "Systemudvikling")


class TestClasses(TestCase):
    def test_get_classid(self):
        self.assertEqual(classes.get_classid(), 10)
        self.assertNotEqual(classes.get_classid(), "10")

    def test_set_classid(self):
        classes.set_classid("10")
        self.assertEqual(classes.get_classid(), 10)
        self.assertNotEqual(classes.get_classid(), "10")

    def test_get_location(self):
        self.assertEqual(classes.get_location(), "Universitetsparken 4")

    def test_set_location(self):
        classes.set_location("Universitetsparken 5")
        self.assertEqual(classes.get_location(), "Universitetsparken 5")

    def test_get_date(self):
        self.assertEqual(classes.get_date(), "2022-05-29")

    def test_set_date(self):
        classes.set_date("2022-05-30")
        self.assertEqual(classes.get_date(), "2022-05-30")

    def test_get_start(self):
        self.assertEqual(classes.get_start(), "08:00:00")

    def test_set_start(self):
        classes.set_start("09:00:00")
        self.assertEqual(classes.get_start(), "09:00:00")

    def test_get_end(self):
        self.assertEqual(classes.get_end(), "12:00:00")

    def test_set_end(self):
        classes.set_end("13:00:00")
        self.assertEqual(classes.get_end(), "13:00:00")

    def test_get_classcourseID(self):
        self.assertEqual(classes.get_classcourseID(), 1)

    def test_set_classcourseID(self):
        classes.set_classcourseID("2")
        self.assertEqual(classes.get_classcourseID(), 2)
        self.assertNotEqual(classes.get_classid(), "2")

    def test_get_coursename(self):
        self.assertEqual(classes.get_coursename(), "Softwareudvikling")

    def test_set_coursename(self):
        classes.set_coursename("Test")
        self.assertEqual(classes.get_coursename(), "Test")

    def test_changes_get_id(self):
        self.assertEqual(changes.get_id(), 11)

    def test_set_coursename(self):
        changes.set_id("10")
        self.assertEqual(changes.get_id(), 10)

    def test_changes_get_date(self):
        self.assertEqual(changes.get_date(), "2022-05-30")

    def test_changes_set_date(self):
        changes.set_date("2022-05-29")
        self.assertEqual(changes.get_date(), "2022-05-29")
        changes.set_date("29-05-2022")
        self.assertEqual(changes.get_date(), "29-05-2022")

    def test_changes_get_start(self):
        self.assertEqual(changes.get_start(), "09:00:00")

    def test_changes_set_start(self):
        changes.set_start("10:00:00")
        self.assertEqual(changes.get_start(), "10:00:00")

    def test_changes_get_end(self):
        self.assertEqual(changes.get_end(), "15:00:00")

    def test_changes_set_end(self):
        changes.set_end("16:00:00")
        self.assertEqual(changes.get_end(), "16:00:00")

    def test_changes_set_courseid(self):
        changes.set_courseid("2")
        self.assertEqual(changes.get_courseid(), 2)

    def test_changes_get_courseid(self):
        self.assertEqual(changes.get_courseid(), 1)
        self.assertNotEqual(changes.get_courseid(), "1")

    def test_users_get_id(self):
        self.assertEqual(users.get_id(), 1)

    def test_users_get_username(self):
        self.assertEqual(users.get_username(), "Testperson")
        self.assertNotEqual(users.get_username(), "testperson")

    def test_users_set_username(self):
        users.set_username("testperson")
        self.assertEqual(users.get_username(), "testperson")

    def test_users_get_password(self):
        self.assertEqual(users.get_password(), "kode")

    def test_users_set_password(self):
        users.set_password("testperson")
        self.assertEqual(users.get_password(), "testperson")

    def test_users_get_fname(self):
        self.assertEqual(users.get_fname(), "Fornavn")

    def test_users_set_fname(self):
        users.set_fname("Nytnavn")
        self.assertEqual(users.get_fname(), "Nytnavn")

    def test_users_get_lname(self):
        self.assertEqual(users.get_lname(), "Efternavn")

    def test_users_set_lname(self):
        users.set_lname("Nytnavn")
        self.assertEqual(users.get_lname(), "Nytnavn")

    def test_users_get_email(self):
        self.assertEqual(users.get_email(), "test@testen.dk")

    def test_users_set_email(self):
        users.set_email("test@testen.com")
        self.assertEqual(users.get_email(), "test@testen.com")

    def test_users_get_cpr(self):
        self.assertEqual(users.get_cpr(), 6543214321)

    def test_users_set_cpr(self):
        users.set_cpr("6543214321")
        self.assertEqual(users.get_cpr(), 6543214321)

    def test_users_get_address(self):
        self.assertEqual(users.get_address(), "minadresse")

    def test_users_set_address(self):
        users.set_address("nyadresse")
        self.assertEqual(users.get_address(), "nyadresse")

    def test_users_get_usertypeid(self):
        self.assertEqual(users.get_usertypeid(), 1)

    def test_users_set_usertypeid(self):
        users.set_usertypeid("2")
        self.assertEqual(users.get_usertypeid(), 2)

    def test_courses_get_courseID(self):
        self.assertEqual(courses.get_courseID(), 1)

    def test_courses_set_courseID(self):
        courses.set_courseID("2")
        self.assertEqual(courses.get_courseID(), 2)

    def test_courses_get_year(self):
        self.assertEqual(courses.get_year(), 2022)

    def test_courses_set_year(self):
        courses.set_year("3030")
        self.assertEqual(courses.get_year(), 3030)

    def test_courses_get_university(self):
        self.assertEqual(courses.get_university(), "København Universitet")

    def test_courses_set_university(self):
        courses.set_university("Odense Universitet")
        self.assertEqual(courses.get_university(), "Odense Universitet")

    def test_courses_get_uniID(self):
        self.assertEqual(courses.get_uniID(), 1)

    def test_courses_set_uniID(self):
        courses.set_uniID("2")
        self.assertEqual(courses.get_uniID(), 2)

    def test_courses_get_program(self):
        self.assertEqual(courses.get_program(), "Sundhed og Informatik")

    def test_courses_set_program(self):
        courses.set_program("Informatik og Sundhed")
        self.assertEqual(courses.get_program(), "Informatik og Sundhed")

    def test_courses_get_programID(self):
        self.assertEqual(courses.get_programID(), 1)

    def test_courses_set_programID(self):
        courses.set_programID("2")
        self.assertEqual(courses.get_programID(), 2)

    def test_courses_get_coursename(self):
        self.assertEqual(courses.get_coursename(), "Systemudvikling")

    def test_courses_set_coursename(self):
        courses.set_coursename("System")
        self.assertEqual(courses.get_coursename(), "System")



