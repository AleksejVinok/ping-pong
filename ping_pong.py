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
win_widht = 1000 #ширина
win_height = 700 #высота
display.set_caption('Ping Pong 90-e')
window = display.set_mode((win_widht, win_height))
background = transform.scale(image.load('table.png'), (win_widht, win_height))
speed_x = 4
speed_y = 1
finish = False
run = True
lose1 = 3
lose2 = 3
#?Создание спрайтов
racket1 = Player("racket.jpg", 10, 200, 40, 100, 6)
racket2 = Player("racket.jpg", 940, 200, 40, 100, 6)
ball = GameSprite('ball.png', 450, 240, 50, 50, 7)
#Цикл игры
while run != False:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background,(0, 0)) #фон
        #TODO Вывод текста
        text_life1 = font1.render('Осталось жизней:' + str(lose1), 1, (255, 255, 255))
        window.blit(text_life1, (10, 15))
        text_life2 = font1.render('Осталось жизней:' + str(lose2), 1, (0, 0, 0))
        window.blit(text_life2, (720, 15))
        text_lose1 = font2.render('ИГРОК 1 ПРОИГРАЛ', 1, (170, 0, 0))
        text_lose2 = font2.render('ИГРОК 2 ПРОИГРАЛ', 1, (170, 0, 0))
        #Отрисовка
        racket1.update_right()
        racket2.update_left()
        racket1.reset()
        racket2.reset()
        ball.reset()
        display.update()
        
        #Движение мяча
        ball.rect.x += speed_x
        ball.rect.y -= speed_y
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
        if ball.rect.y > win_height - 40:
            speed_y *= -1
        if ball.rect.y <= 5:
            speed_y *= -1
        #Счётчик пропуска
        if ball.rect.x < 0:
            speed_x *= -1
            lose1 -= 1
            if lose1 == 0:
                window.blit(text_lose1, (410, 340))
                time.delay(500)
                finish = True
        if ball.rect.x > win_widht:
            speed_x *= -1
            lose2 -= 1
            if lose2 == 0:
                window.blit(text_lose2, (410, 340))
                time.delay(500)
                finish = True
        if finish == True:
            del(ball)
            lose1 = 3
            lose2 = 3
            time.delay(2000)
            ball = GameSprite('ball.png', 450, 240, 50, 50, 7)
                
            



        