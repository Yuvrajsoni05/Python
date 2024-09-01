class Car:
    # model = None
    # brand = None
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


my_tesla = ElectricCar(brand='e', model='n',battery_size="R")
print(my_tesla.battery_size)








        # __init__ also Know Constrater


# my_car = Car("BMW","Corolla")
#
# print(my_car.brand)
# print(my_car.model)
#
# print(my_car.full_name())
#
# my_new_car = Car("TATA" , "Safari")
# print(my_new_car.model)
# print(my_new_car.brand)