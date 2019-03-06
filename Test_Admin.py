from Administrator import Administrator
from unittest import TestCase

class Test_Admin(TestCase):

    def test_createCourse(self):
        self.ad1 = Administrator("admin", "testpass", "blah@uwm.edu")
        self.ad2 = Administrator("admin2", "testpass2", "blah2@uwm.edu")

        self.assertTrue(self, self.ad1.createAccount("people","pass","thatguy@uwm.edu"))
        self.assertTrue(self, self.ad1.createAccount("people1", "pass2", "thatguy2@uwm.edu"))
        self.assertFalse(self, self.ad1.createAccount("people","pass","thatguy@uwm.edu"))

    def test_createAccount(self):
        self.ad1 = Administrator("admin", "testpass", "blah@uwm.edu")
        self.ad2 = Administrator("admin2", "testpass2", "blah2@uwm.edu")

        self.assertTrue(self, self.ad1.createCourse("CS337"))
        self.assertTrue(self, self.ad2.createCourse("CS315"))
        self.assertFalse(self, self.ad1.createCourse("CS337"))

    def test_editAccount(self):
        self.ad1 = Administrator("admin", "testpass", "blah@uwm.edu")
        self.ad2 = Administrator("admin2", "testpass2", "blah2@uwm.edu")

