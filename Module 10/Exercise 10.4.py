
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

class Race:
    def __init__(self, name, km_distance, participants):
        self.name = name
        self.km_distance = km_distance
        self.participants = participants
    def hours_passes(self, hours):
        for i in cars:
            i.accelerate(random.randint(-10,15))
            i.drive(hours)
    def print_status(self):
        print(f'{self.name} status:')
        print('Car  |  Max Speed  | Speed | Travel Distance')
        for i in cars:
            print(f"{i.registration_number}   {i.max_speed}km/h {i.current_speed}km/h   {i.travel_distance}")
    def race_finished(self):
        for i in cars:
            if i.travel_distance >= 10000:
                winner = i
                print(f'Winner is: {winner.registration_number}')
                return True

        

cars = []

for i in range(1,11):
    car = Car(f"ABC-{i}", random.randint(100, 200))
    cars.append(car) 

race = Race('Grand Demolition Derby', 8000, cars)

while not race.race_finished():
    for i in range(1,11):
        race.hours_passes(1)
    race.print_status()





