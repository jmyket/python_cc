"""Class to model a restaurant."""

class Restaurant:
    """Class to represent a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant attibutes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Restaurant description."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Restaurant status."""
        print(f"{self.restaurant_name} is open.")

    def set_number_served(self, num_served):
        self.number_served = num_served

    def increment_number_served(self, new_customers):
        self.number_served += new_customers