import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 설정
screen_width, screen_height = 600, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("블록깨기 게임")

# 색깔 정의
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# 패들 설정
paddle_width, paddle_height = 100, 10
paddle_x = screen_width // 2 - paddle_width // 2
paddle_y = screen_height - 20

# 공 설정
ball_radius = 10
ball_x = screen_width // 2
ball_y = paddle_y - ball_radius - 5
ball_speed_x = 5
ball_speed_y = -5

# 블록 설정
block_width, block_height = 50, 20
blocks = []
for row in range(5):
    for col in range(10):
        block = pygame.Rect(col * block_width, row * block_height, block_width, block_height)
        blocks.append(block)

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 5
    if keys[pygame.K_RIGHT] and paddle_x < screen_width - paddle_width:
        paddle_x += 5

    # 공 이동
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 벽과의 충돌 처리
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen_width:
        ball_speed_x = -ball_speed_x
    if ball_y - ball_radius <= 0:
        ball_speed_y = -ball_speed_y

    # 패들과의 충돌 처리
    if paddle_x < ball_x < paddle_x + paddle_width and paddle_y < ball_y < paddle_y + 10:
        ball_speed_y = -ball_speed_y

    # 블록과의 충돌 처리
    for block in blocks:
        if block.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)):
            blocks.remove(block)
            ball_speed_y = -ball_speed_y

    # 화면 그리기
    screen.fill(black)
    pygame.draw.rect(screen, white, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)

    for block in blocks:
        pygame.draw.rect(screen, blue, block)

    pygame.display.flip()

    # 초당 프레임 설정
    pygame.time.Clock().tick(60)
