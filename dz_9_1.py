
# My first class about cars

# Main class Moving Car
class MovingCar:
    # Define car brand, car color, car model, engine volume
    def __init__(self, car_brand: str, car_model: str,car_color: str, engine_volume: float):
        self.car_brand = car_brand
        self.car_model = car_model
        self.car_color = car_color
        self.engine_volume = engine_volume

    # Define how car can move
    def moving_forward(self):
        print(f"{self.car_color} {self.car_brand} {self.car_model} {self.engine_volume} is moving forward")

    def moving_back(self):
        print(f"{self.car_color} {self.car_brand} {self.car_model} {self.engine_volume} is moving back")

# Inherited class with new methods Turning_Car
class TurningCar(MovingCar):
    def __init__(self, car_brand: str, car_model: str,car_color: str, engine_volume: float):
        super().__init__(car_brand, car_model,car_color, engine_volume)

    # Define how car can turn
    def  turning_left(self):
        print(f"{self.car_color} {self.car_brand} {self.car_model} is turning left")

    def  turning_right(self):
        print(f"{self.car_color} {self.car_brand} {self.car_model} is turning right")

car1 = MovingCar("Toyota", "Auris", "Grey", 1.6)
car1.moving_forward()

car2 = MovingCar("Mitsubishi", "Pajero Sport", "Black", 2.4)
car2.moving_back()

car3 = TurningCar("Toyota", "Rav4", "White", 2.0 )
car3.turning_right()
car3.turning_left()