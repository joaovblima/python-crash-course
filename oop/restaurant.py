class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"O restaurante {self.restaurant_name}, tem uma cozinha {self.cuisine_type}, serviu {self.number_served}")
    

    def open_restaurant(self):
        print(f"O restaurant esta aberto.")
    
    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, more_served):
        self.number_served += more_served
     


