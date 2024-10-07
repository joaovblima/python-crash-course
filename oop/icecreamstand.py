class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"O restaurante {self.restaurant_name}, tem uma cozinha {self.cuisine_type}")
    

    def open_restaurant(self):
        print(f"O restaurant esta aberto.")
    
    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, more_served):
        self.number_served += more_served
  

class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["napolitano", "pistache", "nutella"]

    def get_ice_cream_flavors(self):
        for flavors in self.flavors:
            print(f"Sabores: -> {flavors}")

frutilla = IceCreamStand("frutilla", "sorveteria")
frutilla.get_ice_cream_flavors()

