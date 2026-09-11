import pygame

clock = pygame.time.Clock()

pygame.init() # инициализации игры
screen = pygame.display.set_mode((618, 359)) # размеры экрана, flags=pygame.NOFRAME
pygame.display.set_caption("Pygame EMentuz.corp")

icon = pygame.image.load('images/icon.png') # иконка для окна
pygame.display.set_icon(icon)

# square = pygame.Surface((50, 170)) # создание поверхности
# square.fill('Red')

myfont = pygame.font.Font('fonts/CherryBombOne-Regular.ttf', 40) # создание шрифта
# text_surface = myfont.render("Mentuz's game", False, "Green") # дополнительные
# характеристики к тестовой надписи: текстб цвеб задний фон сглаживание

bg = pygame.image.load('images/background.jpg') # картинка

# TODO: поиграться с фонами чтобы луна проходила один раз
# bg2 = pygame.image.load('images/background2.jpg') # картинка
# bg3 = pygame.image.load('images/background3.jpg') # картинка


# создание иконки
walk_right = [
    pygame.image.load('images/player_right/1.png'),
    pygame.image.load('images/player_right/2.png'),
    pygame.image.load('images/player_right/3.png'),
    pygame.image.load('images/player_right/4.png'),
    ]
walk_left = [
    pygame.image.load('images/player_left/1.png'),
    pygame.image.load('images/player_left/2.png'),
    pygame.image.load('images/player_left/3.png'),
    pygame.image.load('images/player_left/4.png'),
    ]

player_anim_count = 0

bg_x = 0

bg_sound = pygame.mixer.Sound("sounds/muz.mp3")
bg_sound.play()

running = True
while running:


    # screen.blit(square, (20, 40)) # вывод square на экран

    # screen.fill((45, 84, 142))  # цвет экрана

    # pygame.draw.circle(screen, "Blue", (600, 300), 30) # рисование на экране 2 способ
    # pygame.draw.circle(square, "Blue", (0, 0), 30) # рисование на фигуре

    # screen.blit(text_surface, (300, 100))# вывод текста на экран

    screen.blit(bg, (bg_x, 0)) # вывод фона на экран
    screen.blit(bg, (bg_x + 626, 0)) # вывод фона на экран
    bg_x -= 1
    if bg_x == -626:
        bg_x = 0
    screen.blit(walk_right[player_anim_count], (0, 250))# вывод фона на экран

    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1

    pygame.display.update() # обновление экрана

    clock.tick(30) # кол-во фреймов в с (частота)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # кнопка выхода
            pygame.quit()
            running = False
        elif event.type == pygame.KEYDOWN:# нажатие любой клавиши клавиатуры
            if event.key == pygame.K_a: # нажатие клавиши а
                screen.fill((10, 100, 150))  # цвет экрана

