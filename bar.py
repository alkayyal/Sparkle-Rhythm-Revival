import ball

class Bar:

    def __init__(self, length, ball_position, ball_velocity):
        self.tube_length = length
        self.ball = ball.Ball(ball_position,ball_velocity)
        self.goal_1 = 0
        self.goal_2 = self.tube_length