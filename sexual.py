import pygame
import random
import sys
import time
from button import Button

pygame.init()
pygame.font.init()

run = True

font = pygame.font.Font(None, 36)

BG = pygame.image.load("background.png")

character = pygame.image.load("aizen6.png")
character_rect = character.get_rect()

character_rect.topleft = (600, 300)

score = 0
score_increment = 1

player = pygame.Rect((300, 300, 50, 50))  
ground = pygame.Rect((0, 600, 1280, 1000))

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

player_speed = 4
star_speed = 2
character_speed = 3

WHITE = (255, 255, 255)

stars = []
star_spawn_timer = 0

clock = pygame.time.Clock()

def loop():
    pygame.init()
    pygame.font.init()

    run = True

    font = pygame.font.Font(None, 36)

    BG = pygame.image.load("background.png")

    character = pygame.image.load("aizen6.png")
    character_rect = character.get_rect()


    character_rect.topleft = (600, 300)

    score = 0
    score_increment = 1

    player = pygame.Rect((300, 300, 50, 50))
    ground = pygame.Rect((0, 600, 1280, 1000))

    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))

    player_speed = 4
    star_speed = 2
    character_speed = 3

    WHITE = (255, 255, 255)

    stars = []
    star_spawn_timer = 0

    clock = pygame.time.Clock()

    while run:
        screen.fill("black")

        pygame.draw.rect(screen, (255, 0, 0), player)
        pygame.draw.rect(screen, (0, 255, 0), ground)
        screen.blit(character, character_rect)

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if keys[pygame.K_w]:
            player.y -= player_speed
        elif keys[pygame.K_s]:
            player.y += player_speed
        elif keys[pygame.K_a]:
            player.x -= player_speed
        elif keys[pygame.K_d]:
            player.x += player_speed

        if keys[pygame.K_UP]:
            character_rect.y -= player_speed
        if keys[pygame.K_DOWN]:
            character_rect.y += player_speed
        if keys[pygame.K_LEFT]:
            character_rect.x -= player_speed
        if keys[pygame.K_RIGHT]:
            character_rect.x += player_speed

        score += score_increment

        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        star_spawn_timer += 1
        difficulty_factor = 1.05

        if star_spawn_timer >= max(10, int(30 / difficulty_factor)):
            star_spawn_timer = 0
            num_new_stars = int(difficulty_factor)
            for _ in range(num_new_stars):
                new_star = pygame.Rect(random.randint(0, screen_width - 50), 0, 100, 100)
                stars.append(new_star)
            difficulty_factor *= 1.05

        for star in stars[:]:
            star.y += star_speed
            pygame.draw.rect(screen, (255, 255, 0), star)

            if player.colliderect(star):
                game_over()

            if star.y > screen_height:
                stars.remove(star)

        def game_over():
            game_over_text = font.render(f'GAME OVER', True, (255, 255, 255))
            screen.fill("black")
            screen.blit(game_over_text, (
                screen_width / 2 - game_over_text.get_width() / 2,
                screen_height / 2 - game_over_text.get_height() / 2
            ))

            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            sys.exit()

        if player.colliderect(ground) or player.y >= screen_height or player.y <= 0 or player.x >= screen_width or player.x <= 0:
            game_over()

        pygame.display.update()
        clock.tick(55)

    pygame.quit()


def main_menu():
    pygame.display.set_caption("Main Menu")

    while True:

        play_button_text = font.render("PLAY GAME", True, WHITE)
        play_button_rect = play_button_text.get_rect(center=(screen_width / 2, screen_height / 2))
        screen.blit(play_button_text, play_button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    loop()

        pygame.display.update()


main_menu()

play_button = Button(image=None, pos=(screen_width // 2, screen_height // 2), 
                     text_input="PLAY GAME", font=font, 
                     base_color=WHITE, hovering_color=(0, 255, 0))

play_button.changeColor(pygame.mouse.get_pos())