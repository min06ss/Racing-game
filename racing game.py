import pygame
import sys
import random
from pygame import draw
from pygame.locals import *
from pygame.constants import KEYDOWN, KEYUP, K_DOWN, K_LEFT, K_RIGHT, K_UP

while True:
    screen_width = 900
    screen_heigth = 450
    mycar = pygame.image.load("Racing_car.jpg")
    mycar = pygame.transform.scale(mycar, (140, 100))
    mycar_x = (80)
    mycar_y = (220)
    score = 0
    bestscore = 0
        

    car_1 = pygame.image.load("car1.jpg")
    car_1 = pygame.transform.scale(car_1, (150, 75))
    car_2 = pygame.image.load("car2.png")
    car_2 = pygame.transform.scale(car_2, (150, 100))
    car_3 = pygame.image.load("car3.png")
    car_3 = pygame.transform.scale(car_3, (150, 75))

    random1_y1 = random.randint(0, 350)
    random1_y2 = random.randint(0, 350)
    random1_y3 = random.randint(0, 350)
    car_x_1 = 750
    car_x_2 = 500
    car_x_3 = 800
    car_1_y = random1_y1
    car_2_y = random1_y2
    car_3_y = random1_y3

    if __name__ == "__main__":
        move_up = 0
        move_down = 0
        move_right = 0
        move_left = 0
        pygame.init()
        screen = pygame.display.set_mode((screen_width, screen_heigth), 0, 32)
        pygame.display.set_caption("자동차레이싱")

        #실행
    T = True
    while T:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                T = False
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    move_up = True 
                elif event.key == K_DOWN:
                    move_down = True
                elif event.key == K_LEFT:
                    move_left = True 
                elif event.key == K_RIGHT:
                    move_right = True
    
            elif event.type == KEYUP:
                if event.key == K_UP:
                    move_up = False 
                elif event.key == K_DOWN:
                    move_down = False
                elif event.key == K_LEFT:
                    move_left = False 
                elif event.key == K_RIGHT:
                    move_right = False
        # 방향키
        if move_up == True:
            mycar_y -= 0.5
        if move_down == True:
             mycar_y += 0.5
        if move_left == True:
            mycar_x -= 0.5
        if move_right == True:
            mycar_x += 0.5

            # 자동차 속도
        car_x_1, car_x_2, car_x_3 = car_x_1 - 0.3, car_x_2 - 0.4, car_x_3 - 0.5

        if mycar_x <= 0:
            mycar_x = 0
        if mycar_x >= 750:
            mycar_x = 750
        if mycar_y <= 0:
            mycar_y = 0
        if mycar_y >= 375:
            mycar_y = 375

        if car_x_1 <= -200:
            car_x_1 = 1100
            score = score + 100
            car_1_y = random.randint(0,350)    
        check_y1 = car_1_y - mycar_y
        if check_y1 <= -30:
            check_y1 = 100
            
        if car_x_1 <= mycar_x - 130:
            check_y1 = 100
            
        if car_x_1 <= mycar_x + 120 and check_y1 <= 90:
            score = 0
            car_x_1 = 1300
            car_x_2 = 1300
            car_x_3 = 1300

        if car_x_2 <= -200:
            car_x_2 = 1100
            score = score + 100
            car_2_y = random.randint(0,350)    
        check_y2 = car_2_y - mycar_y
            
        if check_y2 <= -30:
            check_y2 = 100
            
        if car_x_2 <= mycar_x - 130:
            check_y2 = 100
            
        if car_x_2 <= mycar_x + 120 and check_y2 <= 90:
            score = 0
            car_x_1 = 1300
            car_x_2 = 1300
            car_x_3 = 1300

        if car_x_3 <= -200:
            car_x_3 = 1100
            score = score + 100
            car_3_y = random.randint(0,350)    
        check_y3 = car_3_y - mycar_y
            
        if check_y3 <= -30:
            check_y3 = 100
            
        if car_x_3 <= mycar_x - 130:
            check_y3 = 100
            
        if car_x_3 <= mycar_x + 120 and check_y3 <= 90:
            score = 0
            car_x_1 = 1300
            car_x_2 = 1300
            car_x_3 = 1300
    
        if score >= bestscore and score >= 0:
            bestscore = score
    
        font_30 = pygame.font.SysFont('FixedSys', 40, True, False)
        text_score = font_30.render('SCORE: {}'.format(score), True, (0, 0, 0))
        text_bestscore = font_30.render('BESTSCORE: {}'.format(bestscore), True, (0, 0, 0))
        screen.fill((255, 255, 255))
        screen.blit(mycar, (mycar_x, mycar_y))
        screen.blit(car_1, (car_x_1, car_1_y))
        screen.blit(car_2, (car_x_2, car_2_y))
        screen.blit(car_3, (car_x_3, car_3_y))
        screen.blit(text_score, (500, 0))
        screen.blit(text_bestscore, (0, 0))
        pygame.display.flip()