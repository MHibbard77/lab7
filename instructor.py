from Person import Person


class Instructor(Person):

    def __init__(self, email, username, password):
        super().__init__(email, username, password)
        self.name = "DEFAULT"
        self.phone = "DEFAULT"
        self.courses = []

