# imports
import time

# classes
class Instructions():
    '''
    This class is used to for creating the content of the instructions screen.
    It holds 3 method (apart from the constructor):
        draw() -> draws the content 
        move() -> allows the ball to move
        bounce() -> allows the ball in the background to bounce
    '''
    def __init__(self):
        self.x, self.y = 400, 300
        self.dx, self.dy = 2, -2
        
    def draw(self):
        # Draws instructions screen texts and centers it accordingly
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
        
        # set color according to theme
        if theme == "light":
            fill(0)
        else:
            fill(255)
        circle(self.x, self.y, 22)
        
    def move(self):
        # move ball according to directional x and y position
        self.x += self.dx
        self.y += self.dy
        
    def bounce(self):
        # bounce off top and bottom
        if self.y > 589 or self.y < 11:
            self.dy *= -1
        # bounce off left and right
        if self.x + 11 > 800 or  self.x - 11 < 0:
            self.dx *= -1        
        
        
        
class Player():
    '''
    This class is used to for to create a player for the game.
    It holds 2 methods (apart from the constructor):
        draw() -> draws the content 
        increase_score() -> increases the score of the player
    '''
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
    '''
    This class is used to for creating a paddle (one per player).
    It holds 2 methods (apart from the constructor):
        draw() -> draws the content 
        move() -> allows the paddle to move according to the pressed keys
    '''
    def __init__(self, x, chosen_up_key, chosen_down_key):
        self.y = 300
        self.x = x
        self.dy = 2
        self.chosen_up_key = chosen_up_key
        self.chosen_down_key = chosen_down_key
        self.pressed_up = False
        self.pressed_down = False
    
    def draw(self):
        # change colour of paddle accoding to theme
        if theme == "tennis-court":
            fill(224, 229, 255)
        elif theme == "dark":
            fill(255)
        elif theme == "light":
            fill(0)
        
        # draw rectangle from top-left corner
        rectMode(CORNER)
        rect(self.x, self.y, 15, 80)
    
    def move(self):
        # move paddle accordingly to set values for keyPressed (allows for simultaenous key presses)
        # left paddle
        if paddle_1.pressed_up == True:
            if paddle_1.y != 0:
                paddle_1.y -= paddle_1.dy
        if paddle_2.pressed_up == True:
            if paddle_2.y != 0:
                paddle_2.y -= paddle_2.dy
        # right paddle
        if paddle_1.pressed_down == True:
            if paddle_1.y + 80 != 600:
                paddle_1.y += paddle_1.dy
        if paddle_2.pressed_down == True:
            if paddle_2.y + 80 != 600:
                paddle_2.y += paddle_2.dy


class COM_Paddle():
    '''
    This class is used to for creating a computer player (for single player mode).
    It holds 3 methods (apart from the constructor):
        draw() -> draws the content 
        move() -> allows the paddle to move (on its own)
        bounce() -> allows the ball to bounce of the computer player paddle
    '''    
    def __init__(self, x):
        self.y = 300
        self.x = x
        self.dy = 2 
        self.rand = random(0,80) 
        
    def draw(self):
        # updates colours according to theme
        if theme == "tennis-court":
            fill(224, 229, 255)
        elif theme == "dark":
            fill(255)
        elif theme == "light":
            fill(0)
        
        # draw rectangle from the top-left corner
        rectMode(CORNER)
        rect(self.x, self.y, 15, 80)
    
    def move(self):
        # move paddle according to randomized position
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
            # randomize position of paddle 
            self.rand = int(random(-160, 160))
            ball.random_dir()     
        
class Ball():
    '''
    This class is used to for creating the content of the instructions screen.
    It holds 5 methods (apart from the constructor):
        draw() -> draws the content 
        move() -> allows the ball to move
        bounce() -> allows the ball in the background to bounce
        reset() -> resets the position of the ball after each point
        random_dir() -> sets a random direction after each point
    '''
    def __init__(self):
        self.x = 400
        self.y = 300
        self.dx = 2
        self.dy = -2
    
    def draw(self):
        # updates colours according to theme
        if theme == "tennis-court":
            fill(220, 253, 80)
        elif theme == "light":
            fill(0)
        elif theme == "dark":
            fill(255)
            
        circle(self.x,self.y,22)
        
    def move(self):
        # move the ball according to the directional x and y values
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
    '''
    This class is used to for creating the button on the title screen and content.
    It holds 1 method (apart from the constructor):
        draw() -> draws the button and its content
    '''
    def __init__(self, x, y, type, txt):
        self.x = x
        self.y = y
        self.type = type
        self.txt = txt 
    
    def draw(self):
        # draws rectangle from the center
        rectMode(CENTER)
        textAlign(CENTER, CENTER)
        
        # draw a thick button and set according sizes 
        if self.type == "thick":
            # set fill color of rectangle according to theme
            if theme == "dark":
                fill(255)
            elif theme == "light":
                fill(0)
            elif theme == "tennis-court":
                fill(182, 123, 101)
            
            # draw thick rectangle                
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
        
        # draw a thin button and set according sizes 
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
mode = "single-player" # options are multiplayer and single-player
theme = "dark" # options are dark, light and tennis-court
screen = "home-screen" # options are home-screen, instructions-screen and game-screen
title = loadImage("title-black.png") # options are title-black, title-white and title-green

# initialize all objects   
# screen objects
instructions = Instructions()

# game objects              
ball = Ball()
paddle_1 = Paddle(40, 'W', 'S',)
paddle_2 = Paddle(760, 'I', 'K')
com_paddle = COM_Paddle(760)
player_1 = Player(0,168)
player_2 = Player(0, 568)

# home-screen buttons
play_button = Button(330, 300, "thick", "Play")
game_mode_button = Button(450, 300, "thick", "Game Mode")
theme_button = Button(390, 350, "thin", "Theme")
instructions_button = Button(390, 380, "thin", "Instructions")

# functions
def setup():
    size(800,600)


def draw():
    global screen
    
    # update title photo according to theme and set themes
    
    if theme == "dark":
        title = loadImage("title-black.png")
        background(0)
    elif theme == "light":
        background(255)
        title = loadImage("title-white.png")
    elif theme == "tennis-court":
        title = loadImage("title-green.png")
        background(19, 94, 70)
        noStroke()

    # displays home screen
    if screen == "home-screen":
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
        
        # Displays current theme 
        if theme == "dark":
            text("Current Theme: Dark (classic)", 390, 420)
        elif theme == "light":
            text("Current Theme: Light", 390, 420)
        elif theme == "tennis-court":
            text("Current Theme: Tennis Court", 390, 420)
            
    # draw playing screen
    if screen == "play":
        # Draw broken center line and color according to set theme
        if theme == "tennis-court" or theme == "dark":
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
            
        # draws a computer powered paddle instead of a second player
        elif mode == "multiplayer":
            com_paddle.draw()
            com_paddle.bounce()
            com_paddle.move()
        
        # Changes winning screen according to who reaches 20 points first
        if player_1.score == 20:
                screen = "winner-player-1"
        if player_2.score == 20:
                screen  = "winner-player-2"
        
    
    # displays instruction screen and its contents
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
    
    # checks if the key relevant to a paddle is pressed and updates boolean value accordingly
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
        # check if b key was pressed and returns usere to the home screen
        if key == "b" or key == "B":
            screen = "home-screen"
            textSize(11)

                
def keyReleased():
    if screen == "play":
        # checks if the key relevant to a paddle is released and updates boolean value accordingly
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
            # Rotates themes
            if theme == "dark":
                theme = "light"
            elif theme == "light":
                theme = "tennis-court"
            elif theme == "tennis-court":
                theme = "dark"
