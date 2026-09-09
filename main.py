import pygame

pygame.init() # инициализации игры
screen = pygame.display.set_mode((600, 300)) # размеры экрана, flags=pygame.NOFRAME
pygame.display.set_caption("Pygame EMentuz.corp")

icon = pygame.image.load('images/icon.png') # иконка для окна
pygame.display.set_icon(icon)

running = True
while running:


    # screen.fill((45, 84, 142))  # цвет экрана

    pygame.display.update() # обновление экрана

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # кнопка выхода
            pygame.quit()
            running = False
        elif event.type == pygame.KEYDOWN:# нажатие любой клавиши клавиатуры
            if event.key == pygame.K_a: # нажатие клавиши а
                screen.fill((10, 100, 150))  # цвет экрана


