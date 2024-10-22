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


car = Car("ABC-123", 142)
print(
    f" Registration Number: {car.registration_number}, max speed: {car.max_speed}km/h"
)
print(f" Current speed: {car.current_speed}, travel distance: {car.travel_distance}")
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f" Current speed:{car.current_speed}")
car.accelerate(-200)
print(f" Final speed after brake:{car.current_speed}")
