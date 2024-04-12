# minimal program that runs the screen
from pygame import *

W,H = 800,500
win = display.set_mode((W,H))
display.set_caption("Blockada")

game = True
while game:
    for e in event.get():
        if e.type == QUIT: #cross to end the game, the game cycle is stopped
            game = False #we can stop the game, but run the menu
            #here we have a separate cycle for each screen
    display.update()