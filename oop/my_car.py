from car import Car
my_new_car = Car("volks", "gol", 2018)
print(my_new_car.get_descriptive_name())
my_new_car.odemeter_reading = 23
my_new_car.read_odemeter()