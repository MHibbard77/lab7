class Administrator(Person):
    """
    an instance represents an administrator within the schools
    system
    must have username
    must have password
    must be able to create courses
    must be able to create accounts
    must be able to edit accounts
    must be able to delete account
    must be able to send notification
    must be able to access information
    """
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def createCourse(self, courseName):
       return

    def createAccount(self, username, password, email):
        return

    def editAccount(self, editInfo):
        return

    def deleteAccount(self, username):
        return

    def sendNotification(self, notification):
        return

    def accessInfo(self):
        return

