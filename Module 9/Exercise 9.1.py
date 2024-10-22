class Car:
    def __init__(
        self, registration_number, max_speed, current_speed=0, travel_distance=0
    ):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travel_distance = travel_distance


car = Car("ABC-123", 142)
print(
    f" Registration Number: {car.registration_number}, max speed: {car.max_speed}km/h"
)
print(f" Current speed: {car.current_speed}, travel distance: {car.travel_distance}")
