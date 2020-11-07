import pygame
import sys
import random
pygame.init()
# pygame.mixer.pre_init(buffer=512)      # Sound setting if delayed


def ball_animation():
    global ball_x_speed, ball_y_speed, score_time
    ball.x += ball_x_speed
    ball.y += ball_y_speed

    if ball.left <= 0:
        global player2_score
        pygame.mixer.Sound.play(score_sound)
        score_time = pygame.time.get_ticks()
        player2_score += 1

    if ball.right >= screen_width:
        pygame.mixer.Sound.play(score_sound)
        global player1_score
        score_time = pygame.time.get_ticks()
        player1_score += 1

    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(pong_sound)
        ball_y_speed *= -1

    if ball.colliderect(player1) or ball.colliderect(player2):
        pygame.mixer.Sound.play(pong_sound)
        ball_x_speed *= -1
        if random.choice((1, 0)):
            ball_y_speed *= -1


def players_check():

    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= screen_height:
        player1.bottom = screen_height

    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screen_height:
        player2.bottom = screen_height


def restart():
    global ball_x_speed, ball_y_speed, score_time

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width / 2, screen_height / 2)

    if current_time - score_time < 700:
        num3 = font_score.render("3", True, obj_colour)
        screen.blit(num3, (screen_width / 2 - 10, screen_height / 2 + 35))

    if 700 < current_time - score_time < 1400:
        num2 = font_score.render("2", True, obj_colour)
        screen.blit(
            num2,
            (screen_width / 2 - 10, screen_height / + 35)
        )

    if 1400 < current_time - score_time < 2100:
        num1 = font_score.render("1", True, obj_colour)
        screen.blit(num1, (screen_width / 2 - 10, screen_height / 2 + 35))

    if current_time - score_time < 2100:
        ball_x_speed, ball_y_speed = 0, 0
    else:
        ball_x_speed = 4 * random.choice((1, -1))
        ball_y_speed = 4 * random.choice((1, -1))
        score_time = None


screen_width = 1368
screen_height = 710
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PONG")

# Game Variables
bg_colour = (42, 45, 51)
obj_colour = (200, 200, 200)

ball_x_speed = 4 * random.choice((1, -1))
ball_y_speed = 4 * random.choice((1, -1))

player1_speed = 0
player1_score = 0

player2_speed = 0
player2_score = 0

font_score = pygame.font.Font(None, 50)
# Rectangles
ball = pygame.Rect(screen_width / 2 - 13, screen_height / 2 - 13, 24, 24)
player1 = pygame.Rect(screen_width - 20, screen_height / 2, 10, 140)
player2 = pygame.Rect(10, screen_height / 2, 10, 140)

# Time variables
clock = pygame.time.Clock()
score_time = True

# Sound
pong_sound = pygame.mixer.Sound("sounds/pong.ogg")
score_sound = pygame.mixer.Sound("sounds/score.ogg")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1_speed -= 5
            if event.key == pygame.K_DOWN:
                player1_speed += 5
            if event.key == pygame.K_w:
                player2_speed -= 5
            if event.key == pygame.K_s:
                player2_speed += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player1_speed += 5
            if event.key == pygame.K_DOWN:
                player1_speed -= 5
            if event.key == pygame.K_w:
                player2_speed += 5
            if event.key == pygame.K_s:
                player2_speed -= 5

    ball_animation()

    player2.y += player2_speed
    player1.y += player1_speed

    players_check()

    screen.fill(bg_colour)

    pygame.draw.rect(screen, obj_colour, player1)
    pygame.draw.rect(screen, obj_colour, player2)
    pygame.draw.ellipse(screen, obj_colour, ball)
    pygame.draw.aaline(
        screen,
        obj_colour,
        (screen_width / 2, 0), (screen_width / 2, screen_height)
    )

    if score_time:
        restart()

    player1_text = font_score.render(f'{player1_score}', True, obj_colour)
    screen.blit(
        player1_text, (screen_width / 2 - 30, screen_height / 2)
    )

    player2_text = font_score.render(f'{player2_score}', True, obj_colour)
    screen.blit(
        player2_text, (screen_width / 2 + 13, screen_height / 2)
    )

    pygame.display.update()
    clock.tick(120)
