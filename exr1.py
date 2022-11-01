class car:
    def __init__(self, register_num, max_speed, current_speed=0, travel_distance=0):
        self.register_num = register_num
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travel_distance = travel_distance



BMW = car('ABC-123',142)
print(f'The propertis of BMW is :{BMW.register_num},{BMW.max_speed},{BMW.current_speed},{BMW.travel_distance}')
