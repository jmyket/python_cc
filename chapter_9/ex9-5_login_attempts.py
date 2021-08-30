# EXERCISE 9-5: LOGIN ATTEMPTS

class Users:

    def __init__(self, first_name, last_name, last_login, age, sex):
        self.last_name = last_name
        self.first_name = first_name
        self.last_login = last_login
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        print("User info:")
        print(f"\t First Name: {self.first_name}")
        print(f"\t Last Name: {self.last_name}")
        print(f"\t Last Login: {self.last_login}")
        print(f"\t Age: {self.age}")
        print(f"\t Sex: {self.sex}")
        print(f"\t Logins: {self.login_attempts}")

    def greet_user(self):
        print(
            f"Hello {self.first_name} {self.last_name}, thanks for logging in!"
            f" Last login was on {self.last_login}."
        )

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

josh = Users("Josh", "Myket", "7/14/2021", 35, "M")

josh.describe_user()
josh.increment_login_attempts()
josh.increment_login_attempts()
josh.increment_login_attempts()
josh.describe_user()

josh.reset_login_attempts()
josh.describe_user()