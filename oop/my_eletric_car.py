from car import EletricCar

my_byd = EletricCar("byd", "byd shark", 2022)
print(my_byd.get_descriptive_name())
my_byd.battery.describe_battery()
my_byd.battery.get_range()