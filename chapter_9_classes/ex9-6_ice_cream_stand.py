# EXERCISE 9-6: ICE CREAM STAND

class Restaurant: # FROM EX 9-4
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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type = "Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Vanilla", "Chocolate", "Strawberry", "Coffee"]

    def show_flavors(self):
        print("We offer the following flavors of ice cream:")
        for flav in self.flavors:
            print(f"\t- {flav}")

ice_cream_shop = IceCreamStand("Sun's Ice Cream")

ice_cream_shop.show_flavors()