class Player():
    def __init__(self, score, x):
        self.score = score
        self.x = x
    
    def draw(self):
        textSize(32)
        text(self.score,self.x,32)
    
    def increase_score(self):
        self.score += 1
    
class Paddle():
    def __init__(self, x, chosen_up_key, chosen_down_key):
        self.y = 300
        self.x = x
        self.dy = 2
        self.chosen_up_key = chosen_up_key
        self.chosen_down_key = chosen_down_key
        self.pressed_up = False
        self.pressed_down = False
    
    def draw(self):
        rect(self.x, self.y, 15, 80)
    
    def move(self):
        if paddle_1.pressed_up == True:
            paddle_1.y -= paddle_1.dy
        if paddle_2.pressed_up == True:
            paddle_2.y -= paddle_2.dy
        if paddle_1.pressed_down == True:
            paddle_1.y += paddle_1.dy
        if paddle_2.pressed_down == True:
            paddle_2.y += paddle_2.dy
        
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
    
    def bounce(self):
        if self.y > 589 or self.y < 11:
            self.dy *= -1
        # Check if touching right paddle and bounce off
        if self.x > 748:
            if self.y < paddle_2.y + 80 and self.y > paddle_2.y:
                self.dx *= -1 
                player_2.increase_score()
        if self.x < 67:
            if self.y < paddle_1.y + 80 and self.y > paddle_1.y:
                self.dx *= -1
                player_1.increase_score()

        
ball = Ball()
paddle_1 = Paddle(40, 'W', 'S')
paddle_2 = Paddle(760, 'I', 'K')
player_1 = Player(0,168)
player_2 = Player(0, 568)
def setup():
    size(800,600)

def draw():
    background(0)
    
    # Draw broken center line
    for r in range(10,800,100):
        rect(392,r,8,80)
    
    # Draw all ball and run related modules
    ball.draw()
    ball.move()
    ball.bounce()
    
    # Draw paddles and run related modules
    paddle_1.move()
    paddle_2.move()
    paddle_1.draw()
    paddle_2.draw()

    # draw scores
    player_1.draw()
    player_2.draw()

def keyPressed(self):
    if key == paddle_1.chosen_up_key or key == paddle_1.chosen_up_key.lower():        
        paddle_1.pressed_up = True
    if key == paddle_1.chosen_down_key or key == paddle_1.chosen_down_key.lower():
        paddle_1.pressed_down = True
    if key == paddle_2.chosen_up_key or key == paddle_2.chosen_up_key.lower():        
        paddle_2.pressed_up = True
    if key == paddle_2.chosen_down_key or key == paddle_2.chosen_down_key.lower():
        paddle_2.pressed_down = True
        
def keyReleased(self):
    if key == paddle_1.chosen_up_key or key == paddle_1.chosen_up_key.lower():        
        paddle_1.pressed_up = False
    if key == paddle_1.chosen_down_key or key == paddle_1.chosen_down_key.lower():
        paddle_1.pressed_down = False
    if key == paddle_2.chosen_up_key or key == paddle_2.chosen_up_key.lower():        
        paddle_2.pressed_up = False
    if key == paddle_2.chosen_down_key or key == paddle_2.chosen_down_key.lower():
        paddle_2.pressed_down = False
