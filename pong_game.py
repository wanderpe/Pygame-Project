import sys

import pygame, random

# Pygame Initialize
pygame.init()
clock = pygame.time.Clock()

# setting main window
pygame.display.set_caption("Pong Game")
screen = pygame.display.set_mode((800, 500))
screen_rect = screen.get_rect()

# Left paddle Surface and Rect
left_paddle = pygame.Surface((10, 90))
left_paddle.fill("white")
left_paddle_rect = left_paddle.get_rect()
left_paddle_rect.midleft = screen.get_rect().midleft

# Right paddle Surface and Rect
right_paddle = pygame.Surface((10, 90))
right_paddle.fill("white")
right_paddle_rect = right_paddle.get_rect()
right_paddle_rect.midright = screen.get_rect().midright

# Text variables
left_paddle_score = 0
right_paddle_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

# Ball Rect
ball_rect = pygame.Rect(0, 0, 20, 20)
ball_rect.center = screen_rect.center
player_speed = 7
opponent_speed = 7
ball_speed_x = 7
ball_speed_y = 7




def ball_animation():
    global ball_speed_x, ball_speed_y, right_paddle_score, left_paddle_score, score_time
    ball_rect.x += ball_speed_x  # Direction x-coordinate of the ball
    ball_rect.y += ball_speed_y  # Direction y-coordinate of the ball

    if ball_rect.bottom >= screen_rect.bottom or ball_rect.top <= 0:  # collision of y coordinate
        ball_speed_y *= -1

    if ball_rect.left < 0:
        left_paddle_score += 1
        score_time = pygame.time.get_ticks()

    if ball_rect.right >= screen_rect.right:  # collision of x coordinate
        right_paddle_score += 1
        score_time = pygame.time.get_ticks()

    if ball_rect.colliderect(left_paddle_rect) or ball_rect.colliderect(
            right_paddle_rect):  # ball collision to the paddle
        ball_speed_x *= -1


def ball_start():
    global ball_speed_x, ball_speed_y, score_time

    current_time = pygame.time.get_ticks()
    ball_rect.center = screen_rect.center

    if current_time - score_time < 700:
        number_three = game_font.render("3", False, "white")
        screen.blit(number_three, (800/2 - 10, 500/2 + 20))
    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2", False, "white")
        screen.blit(number_two, (800/2 - 10, 500/2 + 20))
    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1", False, "white")
        screen.blit(number_one, (800/2 - 10, 500/2 + 20))

    if current_time - score_time < 2100:
        ball_speed_x , ball_speed_y = 0,0
    else:
        ball_speed_x = 7 * random.choice((1, -1))
        ball_speed_y = 7 * random.choice((1, -1))
        score_time = 0







def player_animation():
    left_paddle_rect.y += player_speed
    if left_paddle_rect.top <= 0:
        left_paddle_rect.top = 0
    if left_paddle_rect.bottom >= 500:
        left_paddle_rect.bottom = 500


def opponent_Ai():
    if right_paddle_rect.y < ball_rect.y:
        right_paddle_rect.top += opponent_speed
    if right_paddle_rect.y > ball_rect.y:
        right_paddle_rect.bottom -= opponent_speed
    if right_paddle_rect.top <= 0:
        right_paddle_rect.top = 0
    if right_paddle_rect.bottom >= 500:
        right_paddle_rect.bottom = 500


def get_input():
    global player_speed
    player_speed = 0
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        player_speed += -7
    if key[pygame.K_DOWN]:
        player_speed += 7



# score timer
score_time = 1



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()



    ball_animation()
    player_animation()
    opponent_Ai()
    get_input()


    # visuals
    screen.fill("black")  # Filling up a color in screen
    screen.blit(left_paddle, left_paddle_rect)  # Left paddle draws
    screen.blit(right_paddle, right_paddle_rect)  # Right paddle draws
    pygame.draw.ellipse(screen, "white", ball_rect)  # Ball draws
    pygame.draw.aaline(screen, "white", (800 / 2, 0), (800 / 2, 500))


    if score_time:
        ball_start()


    left_paddle_text = game_font.render(f"{left_paddle_score}", False, "white")
    screen.blit(left_paddle_text, (480, 200))
    right_paddle_text = game_font.render(f"{right_paddle_score}", False, "white")
    screen.blit(right_paddle_text, (300, 200)),

    # updating the window
    pygame.display.flip()
    clock.tick(60)  # for framerate
