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
        if player_1.pressed_up == True:
            player_1.y -= player_1.dy
        if player_2.pressed_up == True:
            player_2.y -= player_2.dy
        if player_1.pressed_down == True:
            player_1.y += player_1.dy
        if player_2.pressed_down == True:
            player_2.y += player_2.dy
        
class Ball():
    def __init__(self):
        self.x = 400
        self.y = 300
        self.dx = 2
        self.dy = -4
    
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
            if self.y < player_2.y + 80 and self.y > player_2.y:
                self.dx *= -1 
        if self.x < 67:
            if self.y < player_1.y + 80 and self.y > player_1.y:
                self.dx *= -1


        
ball = Ball()
player_1 = Paddle(40, 'W', 'S')
player_2 = Paddle(760, 'I', 'K')

def setup():
    size(800,600)

def draw():
    background(0)
    
    for r in range(10,800,100):
        rect(392,r,8,80)
    
    print(player_2.y, ball.y)
    # Draw all ball and run related modules
    ball.draw()
    ball.move()
    ball.bounce()
    
    # Draw paddles and run related modules
    player_1.move()
    player_2.move()
    player_1.draw()
    player_2.draw()


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
