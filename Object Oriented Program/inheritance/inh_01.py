class Car:
    @staticmethod
    def start():
        print("Car.start")

    @staticmethod
    def stop():
        print("Car.stop")

class ToyotoCar(Car):
    def __init__(self,name):
        self.name = name


car1 = ToyotoCar("Toyoto")
car2 = ToyotoCar("Toyoto_2")

print(car1.start())
print(car2.name)