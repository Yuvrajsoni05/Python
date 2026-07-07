class Car:
    @staticmethod
    def start():
        return "Car.start"

    @staticmethod
    def stop():
        print("Car.stop")

class ToyotoCar(Car):
    def __init__(self,name):
        self.name = name
        super().start()
        
class FortunerCar(ToyotoCar):
    def __init__(self,type):
        self.type = type


car1 = FortunerCar("Toyoto")
car2 = ToyotoCar("Toyoto_2")

print(car1.start())
# print(car2.name)