# EXERCISE 9-2: 3 RESTAURANTS

class Restaurant:
    """Class to represent a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant attibutes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Restaurant description."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Restaurant status."""
        print(f"{self.restaurant_name} is open.")

restaurant_1 = Restaurant("Lombardo's", "italian")
restaurant_2 = Restaurant("Shot and Bottle", "contemporary")
restaurant_3 = Restaurant("Lucky Dog", "bar")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()