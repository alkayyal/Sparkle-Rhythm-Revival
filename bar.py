import ball

class Bar:

    def __init__(self, length):
        self.tube_length = length
        self.ball = Ball()
        self.goal_1 = 0
        self.goal_2 = self.tube_length