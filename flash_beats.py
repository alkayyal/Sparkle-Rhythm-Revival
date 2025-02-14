
class ball:

    def __init__(self):
        self.speed = 2
        self.position = 10
        self.direction = 1

class bar:
    
    def __init__(self):
        self.tube_length = 20
        self.ball = ball()
        self.goal_1 = 0
        self.goal_2 = self.tube_length

class game:

    numOfBars = 5
    def __init__(self):
        self.grid = []
        for i in range(numOfBars):
            self.grid.append(bar())
        
        self.score_1 = 0
        self.score_2 = 0
    
    def game_state():
        return
    
    def update_state(state):
        return
    
    


