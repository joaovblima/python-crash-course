from car import Car

class Battery:
    def __init__(self, battery_size = 40):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f"o carro esta com a bateria de {self.battery_size}Kwh")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"Esse carro pode percorrer cerca de {range} milhas com a carga")
    
    def upgrade_battery(self):
        print("Fazendo um upgrade na bateria...")
        size = self.battery_size
        if size == 40:
            self.battery_size = 65

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()