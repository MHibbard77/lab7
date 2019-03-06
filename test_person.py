from unittest import TestCase
from Person import Person

class TestPerson(TestCase):
    def test_init_(self):
        self.person1 = Person("DEFAULT_EMAIL", "DEFAULT_USERNAME", "DEFAULT_PASSWORD")
        self.assertEquals(self.person1.email, "DEFAULT_EMAIL")
        self.assertEquals(self.person1.username, "DEFAULT_USERNAME")
        self.assertEquals(self.person1.password, "DEFAULT_PASSWORD")
        self.assertEquals(self.person1.name, "DEFAULT")
        self.assertEquals(self.person1.phone_number, "DEFAULT")

    def test_login(self):
        self.person1 = Person("DEFAULT", "DEFAULT", "DEFAULT")
        self.assertEquals(self.person1.login("DEFAULT",))



    def test_logout(self):
        self.fail()

    def test_update_info(self):
        self.fail()

    def test_access_contact_info(self):
        self.fail()
