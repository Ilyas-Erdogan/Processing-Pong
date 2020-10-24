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
        rectMode(CORNER)
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
        if self.x + 11 > paddle_2.x:
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
            
            

class Button():
    def __init__(self, x, y, type, txt):
        self.x = x
        self.y = y
        self.type = type
        self.txt = txt 
    
    def draw(self):
        rectMode(CENTER)
        textAlign(CENTER, CENTER)

        if self.type == "thick":
            # set fill color of rectangle according to theme
            if theme == "dark":
                fill(255)
            elif theme == "light":
                fill(0)
            elif theme == "tennis-court":
                fill(182, 123, 101)
            
            # draw rectangle                
            rect(self.x, self.y, 100, 50, 4)
            
            # set color of text according to theme
            if theme == "dark":
                fill(0)
            elif theme == "light":
                fill(255)
            elif theme == "tennis-court":
                fill(255)
                
            # draw text
            text(self.txt, self.x, self.y)
            
        elif self.type == "thin":
            # set fill color of rectangle according to theme
            if theme == "dark":
                fill(255)
            elif theme == "light":
                fill(0)
            elif theme == "tennis-court":
                fill(182, 123, 101)
            
            # draw thin rectangle
            rect(self.x, self.y, 220, 25, 4)
            
            # set color of text according to theme
            if theme == "dark":
                fill(0)
            elif theme == "light":
                fill(255)
            elif theme == "tennis-court":
                fill(255)
                
            # draw text
            text(self.txt, self.x, self.y)
            
    
        

# initialize all objects                
ball = Ball()
paddle_1 = Paddle(40, 'W', 'S',)
paddle_2 = Paddle(760, 'I', 'K')
player_1 = Player(0,168)
player_2 = Player(0, 568)
play_button = Button(330, 300, "thick", "Play")
game_mode_button = Button(450, 300, "thick", "Single Player")
theme_button = Button(390, 350, "thin", "Theme")
instructions_button = Button(390, 380, "thin", "Instructions")

# initialize global variables
mode = "single-player"
theme = "dark"
screen = "home-screen"

# functions
def setup():
    size(800,600)


def draw():
    if theme == "dark":
        # sets theme to dark
        background(0)
        fill(255)
        stroke(255)
    elif theme == "light":
        # set theme to light
        background(255)
        fill(0)
        stroke(0)
    elif theme == "tennis-court":
        # set theme to tennis-court
        background(19, 94, 70)
        fill(182, 123, 101)
        stroke(0,255,255)

        
    if screen == "home-screen":
        # displays home screen
        
        # play button
        play_button.draw()
        
        # game mode button
        game_mode_button.draw()
        
        # theme button
        theme_button.draw()
        
        # instructions button
        instructions_button.draw()
        
    if screen == "play":
        # start single player game
        if mode == "single-player":
            # draw playing screen
            
            if theme == "tennis-court":
            # Draw broken center line
                for r in range(10,800,100):
                    fill(255)
                    rect(392,r,8,80)
            else:
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
    
        
def keyPressed():
    if screen == "play":     
        if key == paddle_1.chosen_up_key or key == paddle_1.chosen_up_key.lower():        
            paddle_1.pressed_up = True
        if key == paddle_1.chosen_down_key or key == paddle_1.chosen_down_key.lower():
            paddle_1.pressed_down = True
        if key == paddle_2.chosen_up_key or key == paddle_2.chosen_up_key.lower():        
            paddle_2.pressed_up = True
        if key == paddle_2.chosen_down_key or key == paddle_2.chosen_down_key.lower():
            paddle_2.pressed_down = True

                
def keyReleased():
    if screen == "play":
        if key == paddle_1.chosen_up_key or key == paddle_1.chosen_up_key.lower():        
            paddle_1.pressed_up = False
        if key == paddle_1.chosen_down_key or key == paddle_1.chosen_down_key.lower():
            paddle_1.pressed_down = False
        if key == paddle_2.chosen_up_key or key == paddle_2.chosen_up_key.lower():        
            paddle_2.pressed_up = False
        if key == paddle_2.chosen_down_key or key == paddle_2.chosen_down_key.lower():
            paddle_2.pressed_down = False

def mousePressed():
    global screen, mode, theme
    if screen == "home-screen":
        if (mouseX < play_button.x + 50 and mouseX > play_button.x - 50) and (mouseY < play_button.y + 25 and mouseY > play_button.y - 25):
            screen = "play"
        elif (mouseX < game_mode_button.x + 50 and mouseX > game_mode_button.x - 50) and (mouseY < game_mode_button.y + 25 and mouseY > game_mode_button.y - 25):
            if mode == "single-player":
                mode = "multiplayer"
            elif mode == "multiplayer":
                mode = "single-player"
        elif (mouseX < instructions_button.x + 110 and mouseX > instructions_button.x - 100) and (mouseY < instructions_button.y + 12.5 and mouseY > instructions_button.y - 12.5):
            screen = "instructions"
        elif (mouseX < theme_button.x + 110 and mouseX > theme_button.x - 100) and (mouseY < theme_button.y + 12.5 and mouseY > theme_button.y - 12.5):
            if theme == "dark":
                theme = "light"
            elif theme == "light":
                theme = "tennis-court"
            elif theme == "tennis-court":
                theme = "dark"
