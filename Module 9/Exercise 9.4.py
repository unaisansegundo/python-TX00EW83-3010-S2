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

cars = []

for i in range(1,11):
    car = Car(f"ABC-{i}", random.randint(100, 200))
    cars.append(car)

print(cars)
loop = True
while loop:
    for i in cars:
        i.accelerate(random.randint(-10,15))
        i.drive(1)
        if i.travel_distance >= 10000:
            winner = i
            loop = False
print('Race results:')
print(f'Winner is: {winner.registration_number}')
print('Car  |  Max Speed  | Speed | Travel Distance')
for i in cars:
    print(
        f"{i.registration_number}   {i.max_speed}km/h {i.current_speed}km/h   {i.travel_distance}")