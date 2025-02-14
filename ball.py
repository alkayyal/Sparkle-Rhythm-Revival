
class Ball:

    def __init__(self, pos, vel):
        self.velocity = vel
        self.position = pos

    def change_velocity(self,new_velocity):
        self.velocity = new_velocity

    def change_position(self,new_position):
        self.position = new_position

    