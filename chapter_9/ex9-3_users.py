# EXERCISE 9-3: USERS

class Users:

    def __init__(self, first_name, last_name, last_login, age, sex):
        self.last_name = last_name
        self.first_name = first_name
        self.last_login = last_login
        self.age = age
        self.sex = sex

    def describe_user(self):
        print("User info:")
        print(f"\t First Name: {self.first_name}")
        print(f"\t Last Name: {self.last_name}")
        print(f"\t Last Login: {self.last_login}")
        print(f"\t Age: {self.age}")
        print(f"\t Sex: {self.sex}")

    def greet_user(self):
        print(
            f"Hello {self.first_name} {self.last_name}, thanks for logging in!"
            f" Last login was on {self.last_login}."
        )

josh = Users("Josh", "Myket", "7/14/2021", 35, "M")
celia = Users("Celia", "Myket", "7/9/2021", 5, "F")
carolyn = Users("Carolyn", "Myket", "5/22/2021", 35, "F")

josh.describe_user()
josh.greet_user()

celia.describe_user()
celia.greet_user()

carolyn.describe_user()
carolyn.greet_user()