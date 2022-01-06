import pygame
pygame.init()

wid = 1000
height=int(wid*0.8)
screen = pygame.display.set_mode((wid,height))
pygame.display.set_caption('SURMONK')
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    pygame.display.update()
pygame.quit()