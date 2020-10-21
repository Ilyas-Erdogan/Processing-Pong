class Paddle():
    def __init__(self, x, chosen_up_key, chosen_down_key):
        self.y = 300
        self.x = x
        self.dy = 5
        self.chosen_up_key = chosen_up_key
        self.chosen_down_key = chosen_down_key
        self.pressed_up = False
        self.pressed_down = False
    
    def draw(self):
        rect(self.x, self.y, 15, 80)
    
        
class Ball():
    def __init__(self):
        self.x = 400
        self.y = 300
        self.dx = 2
        self.dy = -2
    
    def draw(self):
        circle(self.x,self.y,22)
        
    def move(self):
        self.x += self.dx
        self.y += self.dy
    
    def check_bounce(self):
        if self.y > 589 or self.y < 11:
            self.dy *= -1
        if self.x < 11 or self.x > 789:
            self.dx *= -1


        
ball = Ball()
player_1 = Paddle(40, 'W', 'S')
player_2 = Paddle(760, 'I', 'K')
keyboard = [False, False]

def setup():
    size(800,600)

def draw():
    background(0)
    ball.draw()
    ball.move()
    ball.check_bounce()
    
    player_1.draw()
    player_2.draw()

    if player_1.pressed_up == True:
        player_1.y -= player_1.dy
    if player_2.pressed_up == True:
        player_2.y -= player_2.dy
    if player_1.pressed_down == True:
        player_1.y += player_1.dy
    if player_2.pressed_down == True:
        player_2.y += player_2.dy

def keyPressed(self):
    if key == player_1.chosen_up_key or key == player_1.chosen_up_key.lower():        
        player_1.pressed_up = True
    if key == player_1.chosen_down_key or key == player_1.chosen_down_key.lower():
        player_1.pressed_down = True
    if key == player_2.chosen_up_key or key == player_2.chosen_up_key.lower():        
        player_2.pressed_up = True
    if key == player_2.chosen_down_key or key == player_2.chosen_down_key.lower():
        player_2.pressed_down = True
        
def keyReleased(self):
    if key == player_1.chosen_up_key or key == player_1.chosen_up_key.lower():        
        player_1.pressed_up = False
    if key == player_1.chosen_down_key or key == player_1.chosen_down_key.lower():
        player_1.pressed_down = False
    if key == player_2.chosen_up_key or key == player_2.chosen_up_key.lower():        
        player_2.pressed_up = False
    if key == player_2.chosen_down_key or key == player_2.chosen_down_key.lower():
        player_2.pressed_down = False
