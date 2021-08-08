# EXERCISE 9-4: NUMBER SERVED

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

restaurant = Restaurant("Filmore Slim's", "BBQ")

restaurant.number_served
restaurant.number_served = 5
restaurant.number_served

restaurant.number_served
restaurant.set_number_served(15)
restaurant.number_served

restaurant.number_served
restaurant.increment_number_served(15)
restaurant.number_served
restaurant.increment_number_served(25)
restaurant.number_served # SHOULD EQUAL 40