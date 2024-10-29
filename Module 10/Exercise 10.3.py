class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.floor = bottom_floor
    def floor_up(self):
        self.floor +=1
        print(f'Moving up to floor {self.floor}')
    def floor_down(self):
        self.floor -= 1
        print(f'Moving down to floor {self.floor}')
    def go_to_floor(self, target_floor):
        if target_floor == self.floor:
            print('We are already on that floor')
        elif target_floor < self.floor:
            for i in range(target_floor, self.floor):
                i+=1
                self.floor_down()
            print(f'We arrived at the {target_floor} floor')
        elif target_floor > self.floor:
            for i in range(self.floor, target_floor):
                i += 1
                self.floor_up()
            print(f'We arrived at the {target_floor} floor')

class Building:
    def __init__(self, bottom_floor, top_floor, n_elevators):
        self.elevator = None
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.n_elevators = n_elevators
        self.elevators = []

        for i in range(n_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator, target_floor):
        self.elevators[elevator].go_to_floor(target_floor)

    def fire_alarm(self):
        for i in range(self.n_elevators):
            self.elevators[i].go_to_floor(self.bottom_floor)
        print(f'All elevators arrived at floor {self.bottom_floor}')



one = Building(0,20,3)
one.run_elevator(2, 7)
one.run_elevator(1, 5)
one.run_elevator(0, 3)
one.run_elevator(2, 9)
one.run_elevator(1, 2)
one.run_elevator(0, 3)
one.fire_alarm()