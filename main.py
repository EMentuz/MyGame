import pygame

pygame.init() # инициализации игры
screen = pygame.display.set_mode((600, 300)) # размеры экрана, flags=pygame.NOFRAME
pygame.display.set_caption("Pygame EMentuz.corp")


running = True
while running:



    pygame.display.update() # обновление экрана

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # кнопка выхода
            pygame.quit()
            running = False
