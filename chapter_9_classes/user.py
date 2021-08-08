class Users: # FROM EX 9-5 (ALTERED SINCE MOST OF THESE WOULDN'T APPLY TO
# AN ADMIN)
    def __init__(
        self, first_name = None, last_name = None, last_login = None
        , age = None, sex = None
    ):
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