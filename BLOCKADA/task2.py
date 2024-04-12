from pygame import *

W,H = 1280,720
win = display.set_mode((W,H))
display.set_caption("Blockada")
# game screen

bg = transform.scale(image.load("images/bgr.png"), (W, H))


class Settings(sprite.Sprite):
    def __init__(self, x,y,w,h,speed,img):
        super().__init__()
        self.w = w
        self.h = h
        self.speed = speed
        self.image = transform.scale(image.load(img), (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(Settings):
    def l_r(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -=self.speed
        if keys[K_d]:
            self.rect.x +=self.speed
            # shift alt down
    def u_d(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -=self.speed
        if keys[K_s]:
            self.rect.y +=self.speed
          
        
#TODO_IMAGES
background = 'images/bgr.png'
img_coin = 'images/coin.png'
img_door = 'images/door.png'
img_key = 'images/key.png'
img_chest_open = 'images/cst_open.png'
img_chest_close = 'images/cst_close.png'
img_cyborg = 'images/cyborg.png'
img_stair = 'images/stair.png'
img_port = 'images/portal.png'
img_platform = 'images/platform.png'
img_nothing = 'images/nothing.png'
img_power = 'images/mana.png'
img_hero = 'images/sprite1.png'

#TODO_FONT

#TODO_SOUNDS

#TODO_IMAGES

#TODO_SPRITES

player = Player(300,650,50,50,5, img_hero)
game = True
while game:
    win.blit(bg, (0,0)) 
    # from top left corner (in kivy bottom), to the bottom + by y-coordinate
    for e in event.get():
        if e.type == QUIT:
            game = False 
    player.u_d()        
    player.l_r() 
    player.reset()       
    display.update()