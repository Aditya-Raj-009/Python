import pygame

# initialising pygame:
pygame.init()

# creating window:
win = pygame.display.set_mode((500,500))

# adding caption:
pygame.display.set_caption("Learning Pygame.")

# set axis.:
x = 40
y = 40
width = 40
height = 60
velocity = 5

run = True
while run:
    pygame.time.delay(100)
    # event:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # condition for if we click on red cross on window of pygame it will close.
            run = False
    keys = pygame.key.get_pressed()

    #     creating character:
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))  # rect: rectangle(window,(color),(parameter for height,width,and position(x,y))
    pygame.display.update() # so that our rectangle is visible on screen.

    #     move rectangle:
    if keys[pygame.K_LEFT]:
        x-=velocity
    if keys[pygame.K_RIGHT]:
        x+=velocity
    if keys[pygame.K_UP]:
        y-=velocity
    if keys[pygame.K_DOWN]:
        y+=velocity
#     to fix bug: bug was rectangle not moving over previouse rectangle..ie..aage-pichhe karne par new rectangle aa jaa raha tha
#     to fix this we use fill((color) function:
    win.fill((0,0,0))

pygame.quit()