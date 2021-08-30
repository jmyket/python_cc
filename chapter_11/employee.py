class Employee:
    """Class representing an employee."""

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, pay_increase = 5000):
        """Annual salary increase."""
        self.salary += pay_increase