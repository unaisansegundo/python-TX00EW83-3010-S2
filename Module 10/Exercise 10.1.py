class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.floor = bottom_floor
    def floor_up(self):
        self.floor +=1
        print(f'Moving to floor {self.floor}')
    def floor_down(self):
        self.floor -= 1
        print(f'Moving to floor {self.floor}')
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


h=Elevator(0,10)
h.go_to_floor(5)
h.go_to_floor(0)