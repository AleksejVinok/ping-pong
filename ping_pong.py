from pygame import *
from random import randint
from time import time as timer
#ГЛАВНЫЙ КЛАСС
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y ,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#класс ракеты
class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_widht - 400:
            self.rect.y += self.speed
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_widht - 400:
            self.rect.y += self.speed
lost = 0
score = 0


#!ШРИФТ
font.init()
font1 = font.SysFont('Arial', 30)
font2 = font.SysFont('Arial', 80)

#TODO СОЗДАНИЕ ОКНА
win_widht = 1000 #размеры окна
win_height = 700
display.set_caption('Ping Pong 90-e')
window = display.set_mode((win_widht, win_height))
background = transform.scale(image.load('table.png'), (win_widht, win_height))
speed_x = 4
speed_y = 1
finish = False
run = True
#?Создание спрайтов
racket1 = Player("racket.jpg", 10, 200, 40, 100, 6)
racket2 = Player("racket.jpg", 940, 200, 40, 100, 6)
ball = GameSprite('ball.png', 450, 240, 50, 50, 4)
#Цикл игры
while run != False:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background,(0, 0)) #фон
        
        ball.rect.x += speed_x
        ball.rect.y -= speed_y
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_y *= -1


        racket1.update_right()
        racket2.update_left()
        racket1.reset()
        racket2.reset()
        ball.reset()
        display.update()
