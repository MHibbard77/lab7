from Person import Person


class TA(Person):

    def __init__(self, email, username, password):
        super().__init__(email, username, password)
        self.name = "DEFAULT"
        self.phone = "DEFAULT"
        self.courses = []

    def __view_TA_assignments__(self, assignments):
        return assignments

