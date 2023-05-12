import pygame
import sys
import time
import random

WIDTH, HEIGHT = 1500, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alex dodge")
background = pygame.image.load("burgerBg.jpg")
road = pygame.image.load("road.png")

PLAYER_WIDTH = 640
PLAYER_HEIGHT = 360
PLAYER_VEL = 5


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = [
            pygame.image.load('runFrame1.png'),
            pygame.image.load('runFrame2.png'),
            pygame.image.load('runFrame3.png'),
            pygame.image.load('runFrame4.png'),
            pygame.image.load('runFrame5.png')
        ]
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def update(self):
        self.current_sprite += 0.4

        

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: 
            self.current_sprite += 0.6   

        if keys[pygame.K_LEFT]: 
            self.current_sprite -= 0.2   

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0       

        self.image = self.sprites[int(self.current_sprite)]


def draw(player_image, player_x, player_y):
    WINDOW.blit(background, (-200, -210))
    WINDOW.blit(road, (0, 450))
    WINDOW.blit(road, (0, 375))
    WINDOW.blit(road, (600, 375))
    WINDOW.blit(road, (900, 375))
    WINDOW.blit(road, (600, 450))
    WINDOW.blit(road, (900, 450))

    scaled_image = pygame.transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))
    WINDOW.blit(scaled_image, (player_x, player_y))
    pygame.display.update()


def main():
    pygame.init()
    run = True
    player_image = pygame.image.load("player_image.png")
    player_image = pygame.transform.scale(player_image, (100, 100))
    player_x = 50
    player_y = HEIGHT - PLAYER_HEIGHT - player_image.get_height()
    player = Player(player_x, player_y)
    clock = pygame.time.Clock()
    stamina = 100

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()

        if player_x > 0:
            player_x -= PLAYER_VEL

        if stamina >= 15:
            if keys[pygame.K_LEFT] and player_x - PLAYER_VEL >= 0:
                stamina += 2
                player_x -= PLAYER_VEL
            if keys[pygame.K_RIGHT] and player_x + PLAYER_WIDTH + PLAYER_VEL <= WIDTH:
                stamina -= 10
                if stamina>= 10:
                    player_x += PLAYER_VEL + 22
                if stamina < 10 and player_x - PLAYER_VEL >= 0:
                    player_x -= PLAYER_VEL

          

                

        if stamina <= 30:
            stamina += 8

        player.update()
        draw(player.image, player_x, player_y)

    pygame.quit()


if __name__ == "__main__":
    main()