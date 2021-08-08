# EXERCISE 9-1: RESTAURANT 

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

restaurant = Restaurant("Gibraltar", "mediterranean")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()