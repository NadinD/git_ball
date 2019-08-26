import pygame
import random

size = width, height = 400, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True

# Параметры круга
ball_radius = 10
#  скорость
v = 100

# Пустые списки для координат и цветов наших кругов
ball = []
ball_color = []
ind = []

# Создадим второй холст
screen2 = pygame.Surface(screen.get_size())

# Запускаем окно
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # определяем цвет для  нового шарика
            col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            ball.append(event.pos)
            ball_color.append(col)
            pygame.draw.circle(screen, ball_color[-1], ball[-1], ball_radius)

    screen.fill((0, 0, 0))
    # рисуем на экране сохраненное на втором холсте
    screen.blit(screen2, (0, 0))
    t = v * clock.tick() / 1000

    if ball:
        for i in range(len(ball)):
            x_pos, y_pos = ball[i]

            if y_pos <= height - t - 10:
                y_pos += t
                ball[i] = x_pos, y_pos
                pygame.draw.circle(screen, ball_color[i], (x_pos, int(y_pos)), ball_radius)
            else:
                pygame.draw.circle(screen2, ball_color[i], (x_pos, int(y_pos)), ball_radius)
                pygame.draw.circle(screen, ball_color[i], (x_pos, int(y_pos)), ball_radius)
                ind.append(i)

        for i in range(len(ind)):
            ball.pop(i)
            ball_color.pop(i)
        ind.clear()

    pygame.display.flip()

pygame.quit()
