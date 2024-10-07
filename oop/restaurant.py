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
     


restaurant = Restaurant("Don Martin", "Italiana")
restaurant.number_served = 10
restaurant.describe_restaurant()
print(f"o restaurante serviu {restaurant.number_served} pessoas")
restaurant.set_number_served(25)
print(f"o restaurante serviu {restaurant.number_served} pessoas")
restaurant.increment_number_served(20)
print(f"o restaurante serviu {restaurant.number_served} pessoas")
