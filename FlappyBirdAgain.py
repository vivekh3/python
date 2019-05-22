import pygame
import time

pygame.init()
display_width=800
display_height=600
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Flappy Bird Again")
clock=pygame.time.Clock()
birdimg=pygame.image.load('Bird.png')
crashed=False
x=display_width*0.3
y=display_height*0.4
white=(255,255,255)
black=(0,0,0)


def bird(x,y):
    gameDisplay.blit(birdimg,(x,y))

while not crashed:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            crashed=True

        
        gameDisplay.fill(white)
        bird(x,y)
        pygame.display.update()
        clock.tick(60)


pygame.quit()



        
