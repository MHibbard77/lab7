class Supervisor(person):
    def __init__(self,name, email, username, password, phone):
        super().__init__(name, email, username, password, phone)

    def assign_instructor_course(self, instructor, course):
        """
        assigns the given instructor's course to the course parameter
        """
        return

    def assign_ta_course(self, ta, course):
        """
        assigns the given TA's course to the course parameter
        """
        return

    def assign_ta_lab(self, ta, lab):
        """
        assigns the given TA's lab
        """
        return
