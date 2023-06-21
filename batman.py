import pygame
import sys
from pygame.locals import *
pygame.init()
bg_img = pygame.image.load("C:\\Users\\Student\\Downloads\\wall1.png")#jpg
screen = pygame.display.set_mode([1920,1080])
input_rect = pygame.Rect(200, 200, 140, 38)
color_active = (50,50,50)
color_passive = (13,137,189)
color = color_passive
color1=color_passive
active = False
active1 = False
while True:
    #pygame.display.flip()
    #screen.blit(bg_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
                user_text = ""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE :
                pygame.quit()
                sys.exit()
        if active:
            color = color_active
        else:
            color = color_passive
        if active1:
            color1 = color_active
        else:
            color1 = color_passive
        #pygame.draw.rect(screen, color_passive, submit_rect)
    pygame.draw.rect(screen, color, input_rect)
    pygame.display.flip()
        #clock.tick(60)
    screen.blit(bg_img, (0, 0))