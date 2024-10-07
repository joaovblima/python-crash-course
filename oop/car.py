class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odemeter_reading = 0


    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"

        return long_name.title()
    
    def read_odemeter(self):
        print(f"esse carro etm {self.odemeter_reading} km rodados")

    def update_odometer(self, new_odometer):
        if new_odometer >= self.odemeter_reading:
            self.odemeter_reading = new_odometer
        else:
            print("voce nao pode reduzir o odometro")
    def increment_odometer(self, miles):
        self.odemeter_reading += miles


new_car = Car("gol", "volkswagen", 2008)
print(new_car.get_descriptive_name())
new_car.update_odometer(27_200)
new_car.read_odemeter()
new_car.increment_odometer(200)
new_car.read_odemeter()