# imports
import time
# classes
class Instructions():
    def __init__(self):
        self.x, self.y = 400, 300
        self.dx, self.dy = 2, -2
        
    def draw(self):
        textAlign(CENTER)
        textSize(32)
        text("Instructions", 390, 33)
        textAlign(CENTER, CENTER)
        textSize(20)
        text("""Welcome to Pong! 

Player 1 (left), use the W key to go up and the S key to go down. 
Player 2 (right), use the I key to go up and the K key to go down.
If your opponent misses the ball then you get a point. 
The goal is to get the most points.

Have Fun!
(Press B to go back to title screen)
""", 400, 300)
        if theme == "light":
            fill(0)
        else:
            fill(255)
        circle(self.x, self.y, 22)
    def move(self):
        self.x += self.dx
        self.y += self.dy
        
    def bounce(self):
        if self.y > 589 or self.y < 11:
            self.dy *= -1
        if self.x + 11 > 800 or  self.x - 11 < 0:
            self.dx *= -1        
        
        
        
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
        
        if theme == "tennis-court":
            fill(224, 229, 255)
        elif theme == "dark":
            fill(255)
        elif theme == "light":
            fill(0)
        rectMode(CORNER)
        rect(self.x, self.y, 15, 80)
    
    def move(self):
        # move paddle accordingly to set values for keyPressed
        if paddle_1.pressed_up == True:
            if paddle_1.y != 0:
                paddle_1.y -= paddle_1.dy
        if paddle_2.pressed_up == True:
            if paddle_2.y != 0:
                paddle_2.y -= paddle_2.dy
        if paddle_1.pressed_down == True:
            if paddle_1.y + 80 != 600:
                paddle_1.y += paddle_1.dy
        if paddle_2.pressed_down == True:
            if paddle_2.y + 80 != 600:
                paddle_2.y += paddle_2.dy


class COM_Paddle():
    def __init__(self, x):
        # initiazlie variables
        self.y = 300
        self.x = x
        self.dy = 2 
        self.rand = random(0,80) 
        
    def draw(self):
        if theme == "tennis-court":
            fill(224, 229, 255)
        elif theme == "dark":
            fill(255)
        elif theme == "light":
            fill(0)
        rectMode(CORNER)
        rect(self.x, self.y, 15, 80)
    
    def move(self):
        self.y = ball.y - int(self.rand)
        
    def bounce(self):
        # check if ball hits paddle
        if ball.x + 11 > self.x:
            if ball.y < self.y + 80 and ball.y > self.y:
                ball.dx *= -1
        
        # check if ball goes past paddle
        if ball.x + 11 > self.x + 1:
            player_1.increase_score()
            ball.reset()
            self.rand = int(random(-160, 160))
            ball.random_dir()     
        
class Ball():
    def __init__(self):
        # initialize variables
        self.x = 400
        self.y = 300
        self.dx = 2
        self.dy = -2
    
    def draw(self):
        # draw circle
        if theme == "tennis-court":
            fill(220, 253, 80)
        elif theme == "light":
            fill(0)
        elif theme == "dark":
            fill(255)
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
            self.random_dir()
        
        # check if past left paddle
        if self.x - 11 < paddle_1.x - 1:
            player_2.increase_score()
            self.reset()
            self.random_dir()
        
    def reset(self):
        # resets the balls position
        self.x, self.y = 400, 300
        time.sleep(2)
    
    def random_dir(self):
        # set a random direction for ball to go in
        self.dy = int(random(1,3)) * random(random(-1,-1), random(1,1))
        self.dx *= -1
            
            

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
            
    
        
# initialize global variables
mode = "single-player"
theme = "dark"
screen = "home-screen"

# initialize all objects   
instructions = Instructions()             
ball = Ball()
paddle_1 = Paddle(40, 'W', 'S',)
paddle_2 = Paddle(760, 'I', 'K')
com_paddle = COM_Paddle(760)
player_1 = Player(0,168)
player_2 = Player(0, 568)
play_button = Button(330, 300, "thick", "Play")
game_mode_button = Button(450, 300, "thick", "Game Mode")
theme_button = Button(390, 350, "thin", "Theme")
instructions_button = Button(390, 380, "thin", "Instructions")

#images
title = loadImage("title-black.png")

# functions
def setup():
    size(800,600)


def draw():
    global screen
    if theme == "dark":
        # sets theme to dark
        title = loadImage("title-black.png")
        background(0)
    elif theme == "light":
        # set theme to light
        background(255)
        title = loadImage("title-white.png")
    elif theme == "tennis-court":
        # set theme to tennis-court
        title = loadImage("title-green.png")
        background(19, 94, 70)
        noStroke()

        
    if screen == "home-screen":
        # displays home screen
        
        # displays title
        imageMode(CENTER)
        image(title, 400, 200)
        
        # play button
        play_button.draw()
        
        # game mode button
        game_mode_button.draw()
        
        # theme button
        theme_button.draw()
        
        # instructions button
        instructions_button.draw()
        
        if mode == "single-player":
            if theme == "light":
                fill(0)
            else:
                fill(255)
            text("Current Mode: Singleplayer", 390,400)
        elif mode == "multiplayer":
            if theme == "light":
                fill(0)
            else:
                fill(255)
            text("Current Mode: Multiplayer", 390,400)
        
        if theme == "dark":
            text("Current Theme: Dark (classic)", 390, 420)
        elif theme == "light":
            text("Current Theme: Light", 390, 420)
        elif theme == "tennis-court":
            text("Current Theme: Tennis Court", 390, 420)
            
            
        
    if screen == "play":
        # draw playing screen
        
        if theme == "tennis-court" or theme == "dark":
        # Draw broken center line
            for r in range(10,800,100):
                fill(255)
                rect(392,r,8,80)
        else:
            for r in range(10,800,100):
                fill(0)
                rect(392,r,8,80)
        # Draw all ball and run related modules
        ball.draw()
        ball.move()
        ball.bounce()
    
        # draw scores
        player_1.draw()
        player_2.draw()
    
    # Draw paddles and run related modules
        paddle_1.move()
        paddle_1.draw()
            
        # start single player game
        if mode == "single-player":
            paddle_2.move()
            paddle_2.draw()            
            
        elif mode == "multiplayer":
            com_paddle.draw()
            com_paddle.bounce()
            com_paddle.move()
        
        if player_1.score == 2:
                screen = "winner-player-1"
        if player_2.score == 2:
                screen  = "winner-player-2"
        
    
    if screen == "instructions":
        instructions.draw()
        instructions.move()
        instructions.bounce()
        
    if screen == "winner-player-1":
        textMode(CENTER)
        textSize(32)
        textAlign(CENTER,CENTER)
        text("Player 1 won!", 400, 300)
    elif screen == "winner-player-2":
        textMode(CENTER)
        textSize(32)
        textAlign(CENTER,CENTER)
        text("Player 2 won!", 400, 300) 
        
def keyPressed():
    global screen
    if screen == "play":     
        if key == paddle_1.chosen_up_key or key == paddle_1.chosen_up_key.lower():        
            paddle_1.pressed_up = True
        if key == paddle_1.chosen_down_key or key == paddle_1.chosen_down_key.lower():
            paddle_1.pressed_down = True
        if key == paddle_2.chosen_up_key or key == paddle_2.chosen_up_key.lower():        
            paddle_2.pressed_up = True
        if key == paddle_2.chosen_down_key or key == paddle_2.chosen_down_key.lower():
            paddle_2.pressed_down = True
    
    if screen == "instructions":
        if key == "b" or key == "B":
            screen = "home-screen"
            textSize(11)

                
def keyReleased():
    if screen == "play":
        # checks if the players have 
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
        # checks if play button was pressed
        if (mouseX < play_button.x + 50 and mouseX > play_button.x - 50) and (mouseY < play_button.y + 25 and mouseY > play_button.y - 25):
            screen = "play"
        # switches multiplayer to singleplayer ans singleplayer to multiplayer
        elif (mouseX < game_mode_button.x + 50 and mouseX > game_mode_button.x - 50) and (mouseY < game_mode_button.y + 25 and mouseY > game_mode_button.y - 25):
            if mode == "single-player":
                mode = "multiplayer"
            elif mode == "multiplayer":
                mode = "single-player"
        # switches to instructions screen
        elif (mouseX < instructions_button.x + 110 and mouseX > instructions_button.x - 100) and (mouseY < instructions_button.y + 12.5 and mouseY > instructions_button.y - 12.5):
            screen = "instructions"
        # switches theme of game
        elif (mouseX < theme_button.x + 110 and mouseX > theme_button.x - 100) and (mouseY < theme_button.y + 12.5 and mouseY > theme_button.y - 12.5):
            if theme == "dark":
                theme = "light"
            elif theme == "light":
                theme = "tennis-court"
            elif theme == "tennis-court":
                theme = "dark"
