
import ball
import bar

class Game:

    time_granularity = 60
    max_time = 120 * time_granularity

    def __init__(self):

        self.current_time = 0
        self.num_of_bars = 5
        self.bar_size = 20
        self.grid = []
        for i in range(self.num_of_bars):
            self.grid.append(bar.Bar(self.bar_size,0,0))
        self.score_1 = 0
        self.score_2 = 0
    
    def game_start(self, difficulty):
        self.current_time = 0
        
        if(difficulty == 'easy'):
            self.num_of_bars = 1
        elif(difficulty == 'medium'):
            self.num_of_bars = 3
        else:
            self.num_of_bars = 5
        
        self.grid = []
        current_direction = 1
        for i in range(self.num_of_bars):
            current_direction *= -1
            self.grid.append(bar.Bar())
        self.score_1 = 0
        self.score_2 = 0

        return

    def game_state():

        return
    
    def update_state(state):

        return
    
