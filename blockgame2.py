#blockgame2.py

#pip install pygame

import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 설정
width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("블록 게임")

# 색깔 정의
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# 블록 설정
block_size = 50
block_x = width // 2 - block_size // 2
block_y = height - block_size * 2
block_speed = 5

# 장애물 설정
obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5

obstacles = []

# 시계 설정
clock = pygame.time.Clock()

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and block_x - block_speed > 0:
        block_x -= block_speed
    if keys[pygame.K_RIGHT] and block_x + block_size + block_speed < width:
        block_x += block_speed

    # 장애물 생성
    if random.randint(0, 100) < 5:
        obstacle_x = random.randint(0, width - obstacle_width)
        obstacle_y = 0
        obstacles.append([obstacle_x, obstacle_y])

    # 장애물 이동
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed

    # 충돌 체크
    for obstacle in obstacles:
        if (
            block_x < obstacle[0] < block_x + block_size or
            block_x < obstacle[0] + obstacle_width < block_x + block_size
        ) and (
            block_y < obstacle[1] < block_y + block_size or
            block_y < obstacle[1] + obstacle_height < block_y + block_size
        ):
            pygame.quit()
            sys.exit()

    # 화면 업데이트
    screen.fill(black)

    pygame.draw.rect(screen, white, [block_x, block_y, block_size, block_size])

    for obstacle in obstacles:
        pygame.draw.rect(screen, red, [obstacle[0], obstacle[1], obstacle_width, obstacle_height])

    pygame.display.flip()

    # FPS 설정
    clock.tick(30)


