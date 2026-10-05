import pygame
import random

clock = pygame.time.Clock()

pygame.init() # инициализации игры
screen = pygame.display.set_mode((618, 359)) # размеры экрана, flags=pygame.NOFRAME
pygame.display.set_caption("Pygame EMentuz.corp")

icon = pygame.image.load('images/icon.png').convert_alpha() # иконка для окна
pygame.display.set_icon(icon)

# square = pygame.Surface((50, 170)) # создание поверхности
# square.fill('Red')

myfont = pygame.font.Font('fonts/CherryBombOne-Regular.ttf', 40) # создание шрифта
# text_surface = myfont.render("Mentuz's game", False, "Green") # дополнительные
# характеристики к тестовой надписи: текстб цвеб задний фон сглаживание

bg = pygame.image.load('images/background.jpg').convert_alpha() # картинка

# TODO: поиграться с фонами чтобы луна проходила один раз
# bg2 = pygame.image.load('images/background2.jpg') # картинка
# bg3 = pygame.image.load('images/background3.jpg') # картинка

ghost = pygame.image.load('images/ghost.png').convert_alpha()
ghost_list_in_game = []

# создание иконки
walk_right = [
    pygame.image.load('images/player_right/1.png').convert_alpha(),
    pygame.image.load('images/player_right/2.png').convert_alpha(),
    pygame.image.load('images/player_right/3.png').convert_alpha(),
    pygame.image.load('images/player_right/4.png').convert_alpha(),
    ]
walk_left = [
    pygame.image.load('images/player_left/1.png').convert_alpha(),
    pygame.image.load('images/player_left/2.png').convert_alpha(),
    pygame.image.load('images/player_left/3.png').convert_alpha(),
    pygame.image.load('images/player_left/4.png').convert_alpha(),
    ]

player_anim_count = 0

bg_x = 0

bg_sound = pygame.mixer.Sound("sounds/muz.mp3")
bg_sound.play()

player_speed = 5
player_x = 0
player_y = 250

is_jump = False
jump_count = 8

# a = int(random.uniform(2.5, 8) * 1000)
# ghost_timer = pygame.USEREVENT + 1
# pygame.time.set_timer(ghost_timer, a) # таймер для врагов

next_ghost_spawn_time = pygame.time.get_ticks() + 1500


running = True
while running:
    current_time = pygame.time.get_ticks()


    # screen.blit(square, (20, 40)) # вывод square на экран

    # screen.fill((45, 84, 142))  # цвет экрана

    # pygame.draw.circle(screen, "Blue", (600, 300), 30) # рисование на экране 2 способ
    # pygame.draw.circle(square, "Blue", (0, 0), 30) # рисование на фигуре

    # screen.blit(text_surface, (300, 100))# вывод текста на экран

    screen.blit(bg, (bg_x, 0)) # вывод фона на экран
    screen.blit(bg, (bg_x + 626, 0)) # вывод фона на экран

    player_rect = walk_left[0].get_rect(topleft=(player_x, player_y)) # квадрат вокруг игрока

    if ghost_list_in_game:
        for el in ghost_list_in_game:
            screen.blit(ghost, el)
            el.x -= 5

            if player_rect.colliderect(el): # отслеживание соприкосновений
                print('you lose')


    bg_x -= 1
    if bg_x == -626:
        bg_x = 0

    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT] and player_x > 0:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))# вывод игрока на экран
    else:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))# вывод игрока на экран

    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 575:
        player_x += player_speed


    #     прыжок
    if not is_jump:
        if keys[pygame.K_UP]:
            is_jump = True
    else:
        if jump_count >= -8:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 8




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

    # Планируем следующее появление: случайный интервал от 1.5 до 6 секунд
    if current_time >= next_ghost_spawn_time:
        ghost_list_in_game.append(ghost.get_rect(topleft=(620, 250)))
        next_ghost_spawn_time = current_time + random.randint(500, 6000)


