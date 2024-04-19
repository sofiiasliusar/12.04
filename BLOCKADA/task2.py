from pygame import *
from level import level

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
          

class Camera(): #the field of vision
    def __init__(self,camera_func, w, h):
        self.camera_func = camera_func
        self.state = Rect(0,0,w,h)
        
    def apply(self, target):
        return target.rect.move(self.state.topleft)
    
    def update(self,target):
        self.state = self.camera_func(self.state, target.rect)
    #function will move everything
    # can write for_ in range, _can be a variable "empty variable"
    def camera_config(camera, target_rect): 
        l,t,_,_ = target_rect
        _,_,w,h = camera # we need empty variables because camera returns 4 arguments, so that the program doesn't argue with us
        l, t= -1 + W/2, -t + H/2
        l = min (0, l)
        t = min(0, t)
        l = max(-(camera.width - W), 1)
        t = max(-(camera.height - H), t)
        t = min(0, t)
        
        return Rect(l,t,w,h) #t-top
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

#TO_DO_OBJECTS
player = Player(300, 650, 50, 50, 5, img_hero)
#TODO_GROUPS
blocks_r = []
blocks_l = []
coins = []
stairs = []
platforms = []

items = sprite.Group()

#TODO_IMAGES

#TODO_SPRITES

player = Player(300,650,50,50,5, img_hero)

#TODO_GAME
win.blit(bg, (0,0))
x = y = 0
for r in level:
    for c in r:
        if c == "r":
            r1 = Settings(x,y,40,40,0, img_nothing) #air block, as in minecraft. Each block has a coordinate
            r1.reset()
        if c == "l":
            r2 = Settings(x,y,40,40,0, img_nothing)
            r2.reset()
        if c == '/':
            r3 = Settings(x,y-40,40,180,0, img_stair)
            r3.reset()
        if c == '°':
            r4 = Settings(x,y,40,40,0,img_coin)
            r4.reset()
        if c == "-":
            r5 = Settings(x,y,40,40,0,img_platform)
            r5.reset()
        x+=40 # start with top pixes and paint each block 1 by 1
    y+=40  # go back and do y, while x =   
    x = 0
            

game = True
while game: 
    # from top left corner (in kivy bottom), to the bottom + by y-coordinate
    for e in event.get():
        if e.type == QUIT:
            game = False 
    player.u_d()        
    player.l_r() 
    player.reset()
    # time.delay(15)
    # after adding TO_DO_GAME block of code, uncomented player leaves a trace, because the level is not being repainted
    display.update()