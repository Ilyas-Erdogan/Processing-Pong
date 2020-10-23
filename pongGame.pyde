# classes
class Player():
    def __init__(self, score, x):
        # initialize variable
        self.score = score
        self.x = x
    
    def draw(self):
        # draw number of points according to given x value
        textSize(32)
        text(self.score,self.x,32)
    
    def increase_score(self):
        # increase score
        self.score += 1

        
class Paddle():
    def __init__(self, x, chosen_up_key, chosen_down_key):
        # initiazlie variables
        self.y = 300
        self.x = x
        self.dy = 2
        self.chosen_up_key = chosen_up_key
        self.chosen_down_key = chosen_down_key
        self.pressed_up = False
        self.pressed_down = False
    
    def draw(self):
        # draw paddle
        rect(self.x, self.y, 15, 80)
    
    def move(self):
        # move paddle accordingly to set values for keyPressed
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
        # initialize variables
        self.x = 400
        self.y = 300
        self.dx = 2
        self.dy = -2
    
    def draw(self):
        # draw circle
        circle(self.x,self.y,22)
        
    def move(self):
        # add to x and y values of ball to make it move
        self.x += self.dx
        self.y += self.dy
    
    def bounce(self):
        # checks if ball is hitting top and bottom boundaries
        if self.y > 589 or self.y < 11:
            self.dy *= -1
            
        # Check if touching right paddle and bounce off
        if self.x > paddle_2.x - 11:
            if self.y <= paddle_2.y + 80 and self.y >= paddle_2.y:
                self.dx *= -1 
                    
        # Check if touching left paddle and bounce off                
        if self.x < paddle_1.x + 26:
            if self.y <= paddle_1.y + 80 and self.y >= paddle_1.y:
                self.dx *= -1
                
        # check if past right paddle
        if self.x + 11 > paddle_2.x + 1:
            player_1.increase_score()
            self.reset()
        
        # check if past left paddle
        if self.x - 11 < paddle_1.x - 1:
            player_2.increase_score()
            self.reset()
            
    
    def reset(self):
        # resets the balls position
        self.x, self.y = 400, 300


# initialize all objects                
ball = Ball()
paddle_1 = Paddle(40, 'W', 'S')
paddle_2 = Paddle(760, 'I', 'K')
player_1 = Player(0,168)
player_2 = Player(0, 568)

# initialize global variables
game_mode = "play"

# functions
def setup():
    size(800,600)


def draw():
    if game_mode == "play":
        # draw playing screen
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
