import pygame
import time
import random

WIDTH, HEIGHT = 1500, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alex dodge")
background = pygame.image.load("burgerBg.jpg")
road = pygame.image.load("road.png")

PLAYER_WIDTH = 190
PLAYER_HEIGHT = 200

PLAYER_VEL = 15



def draw(player_image, player_x, player_y):
    WINDOW.blit(background, (-200, -210))
    WINDOW.blit(road, (0, 450))
    WINDOW.blit(road, (600, 450))
    WINDOW.blit(road, (900, 450))

    scaled_image = pygame.transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))
    WINDOW.blit(scaled_image, (player_x, player_y))
    pygame.display.update()

def main():
    pygame.init()

    run = True
    player_image = pygame.image.load("player_image.png")

    player_image = pygame.transform.scale(player_image, (100, 100))  # Scale the player image
    player_x = 50
    player_y = HEIGHT - PLAYER_HEIGHT - player_image.get_height()
    player = player_image.get_rect(topleft=(player_x, player_y))

    clock = pygame.time.Clock()
    stamina = 100

    while run:
        clock.tick(60)

        player_image = pygame.image.load("player_image2.png")
        player_image = pygame.image.load("player_image.png")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        
        if player_x + PLAYER_WIDTH + PLAYER_VEL <= WIDTH:
            player_x += PLAYER_VEL
        
        if stamina >= 15:
            if keys [pygame.K_LEFT] and player_x - PLAYER_VEL >= 0:
                stamina -= 4
                player_x -= PLAYER_VEL + 15
            if keys [pygame.K_RIGHT] and player_x + PLAYER_WIDTH + PLAYER_VEL <= WIDTH:
                stamina -= 4
                player_x += PLAYER_VEL + 5

        if stamina <= 98:
            stamina += 3
            print(stamina)        
                


        draw(player_image, player_x, player_y)


    pygame.quit()

if __name__ == "__main__":
    main()