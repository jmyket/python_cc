from chapter_9_classes import user

class Privileges:

    def __init__(self, privileges = []):
        self.privileges = privileges

    def show_privileges(self):
        print(
            f"admin privileges: {self.privileges}"
        )

class Admin(user.Users):
    def __init__(
        self, first_name = None, last_name = None, last_login = None
        , age = None, sex = None
    ):
        super().__init__(
            first_name, last_name, last_login, age, sex
        )
        self.first_name = "admin"
        self.privileges = Privileges()