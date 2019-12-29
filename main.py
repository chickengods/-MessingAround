import pygame

#inialize the pygrame
pygame.init()

display_width = 1600
display_height = 1600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)


#create the screen
gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('a bit racey')



clock = pygame.time.Clock()
crashed = False

carImg = pygame.image.load('images/8_bit_racer.png')


def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x = 200
y = 200

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)


    car(x,y)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()