from unittest import TestCase
from TA import TA


class TestTA(TestCase):
    def test__init__(self):
        self.ta1 = TA("DEFAULT_EMAIL", "DEFAULT_USERNAME", "DEFAULT_PASSWORD")
        self.assertEquals(self.ta1.email, "DEFAULT_EMAIL")
        self.assertEquals(self.ta1.username, "DEFAULT_USERNAME")
        self.assertEquals(self.ta1.password, "DEFAULT_PASSWORD")
        self.assertEquals(self.ta1.name, "DEFAULT")
        self.assertEquals(self.ta1.phone_number, "DEFAULT")

    def test___view_TA_assignments__(self):
        self.fail()
