import pygame

pygame.init() # инициализации игры
screen = pygame.display.set_mode((600, 300)) # размеры экрана, flags=pygame.NOFRAME
pygame.display.set_caption("Pygame EMentuz.corp")

icon = pygame.image.load('images/icon.png') # иконка для окна
pygame.display.set_icon(icon)

square = pygame.Surface((50, 170)) # создание поверхности
square.fill('Red')

myfont = pygame.font.Font('fonts/CherryBombOne-Regular.ttf', 40) # создание шрифта
text_surface = myfont.render("Mentuz's game", False, "Green") # дополнительные
# характеристики к тестовой надписи: текстб цвеб задний фон сглаживание

player = pygame.image.load('images/car.png') # иконка

me = pygame.Surface((5,5))
me.fill('White')
coord_x = 0

running = True
while running:

    screen.blit(me, (coord_x, 50))
    coord_x += 5
    if coord_x > 600:
        coord_x = 0

    screen.blit(square, (20, 40)) # вывод square на экран

    # screen.fill((45, 84, 142))  # цвет экрана

    pygame.draw.circle(screen, "Blue", (600, 300), 30) # рисование на экране 2 способ
    pygame.draw.circle(square, "Blue", (0, 0), 30) # рисование на фигуре

    screen.blit(text_surface, (300, 100))# вывод текста на экран
    screen.blit(player, (10, 10))# вывод player на экран


    pygame.display.update() # обновление экрана

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # кнопка выхода
            pygame.quit()
            running = False
        elif event.type == pygame.KEYDOWN:# нажатие любой клавиши клавиатуры
            if event.key == pygame.K_a: # нажатие клавиши а
                screen.fill((10, 100, 150))  # цвет экрана


