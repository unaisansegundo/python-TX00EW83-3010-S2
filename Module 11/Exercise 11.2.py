import random

class Car:
    def __init__(
        self, registration_number, max_speed, current_speed=0, travel_distance=0
    ):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travel_distance = travel_distance

    def accelerate(self, speed_change):
        if (self.current_speed + speed_change) > self.max_speed:
            self.current_speed = self.max_speed
        elif (self.current_speed + speed_change) < 0:
            self.current_speed = 0
        else:
            self.current_speed += speed_change

    def drive(self, hours):
        self.travel_distance += hours * self.current_speed



class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_capacity):
        super().__init__(registration_number, max_speed)
        self.tank_capacity = tank_capacity

electric = ElectricCar("ABC-15", 180, 52.5)
gasoline = GasolineCar("ACD-123", 165, 32.3)

electric.current_speed = random.randint(0,100)
gasoline.current_speed = random.randint(0,100)

electric.drive(5)
gasoline.drive(5)

print(f"The electric car has travelled for {electric.travel_distance}")
print(f"The gasoline car has travelled for {gasoline.travel_distance}")