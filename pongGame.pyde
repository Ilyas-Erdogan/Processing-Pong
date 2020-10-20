
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
    
    def keyPressed(self):
        if key == self.chosen_up_key or key == self.chosen_up_key.lower():        
            self.pressed_up = True
        elif key == self.chosen_down_key or key == self.chosen_down_key.lower():
            self.pressed_down = True
    def keyReleased(self):
        if key == self.chosen_up_key or key == self.chosen_up_key.lower():        
            self.pressed_up = False
        elif key == self.chosen_down_key or key == self.chosen_down_key.lower():
            self.pressed_down = False    
    
    def move_up():
        self.y -= self.dy
    def move_down():
        self.y += self.dy
        
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
keyboard = [player_1, player_2]

def setup():
    size(800,600)

def draw():
    background(0)
    ball.draw()
    ball.move()
    ball.check_bounce()
    
    player_1.draw()
    player_2.draw()
    
def keyPressed():
    if player_1.pressed_up == True:
        player_1.move_up()
    if player_2.pressed_up == True:
        player_2.move_up()
    if player_2.pressed_down == True:
        player_2.move_down()
    if player_2.pressed_down == True:
        player_2.move_down()
