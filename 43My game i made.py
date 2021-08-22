import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battle Craft")

WHITE = (98, 84, 234)
BLACK = (28, 78, 236)

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

FPS = 60
VEL = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACE_IMAGE = pygame.image.load('./python02/spaceship_yellow.png')
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACE_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)


RED_SPACE_IMAGE = pygame.image.load('./python02/spaceship_red.png')
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACE_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


def draw_window(red, yellow):
    WIN.fill((WHITE))
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, yellow.y))
    pygame.display.update()


def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #Yellow control
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: #Left
            yellow.x -= VEL
        if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: #Right
            yellow.x += VEL
        if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: #up
            yellow.y -= VEL
        if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT: #down
            yellow.y += VEL
            

        #Red control
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]: #Left
            red.x -= VEL
        if keys_pressed[pygame.K_RIGHT]: #Right
            red.x += VEL
        if keys_pressed[pygame.K_UP]: #up
            red.y -= VEL
        if keys_pressed[pygame.K_DOWN]: #down
            red.y += VEL

        draw_window(red, yellow)

    pygame.quit()

if __name__ == "__main__":
    main()
