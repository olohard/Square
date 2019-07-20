import pygame,sys

pygame.init()
pygame.display.set_caption("First game")
screen = pygame.display.set_mode((1280,720))

x = 50
y = 50
width = 50
height = 50
vel = 5

clock = pygame.time.Clock()
delta = 0.0



while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)

    delta += clock.tick()
    while delta > 4.0:
        delta -= 4.0


        key = pygame.key.get_pressed()


        if key[pygame.K_a] and x > vel:                         # Square moves left
            x -= vel

        if key[pygame.K_d] and x < 1280 - width - vel:          # Square moves right
            x += vel

        if key[pygame.K_w] and y > vel:                         # Square moves up
                y -= vel

        if key[pygame.K_s] and y < 720 - height - vel:          # Square moves down
                y += vel



    screen.fill((0,0,0))
    pygame.draw.rect(screen, (0, 255, 255), (x, y, width, height))
    pygame.display.flip()
