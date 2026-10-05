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

next_ghost_spawn_time = pygame.time.get_ticks() + 1500

label = pygame.font.Font('fonts/CherryBombOne-Regular.ttf', 40) # создание шрифта
lose_label = label.render("You lose!", False, "Green") # дополнительные
# характеристики к тестовой надписи: текстб цвеб задний фон сглаживание

restart_label = label.render("Restart", False, "Green")
restart_label_rect = restart_label.get_rect(topleft=(180, 200))

gameplay = True

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

    if gameplay:

        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y)) # квадрат вокруг игрока

        if ghost_list_in_game:
            for (i, el) in enumerate(ghost_list_in_game):
                screen.blit(ghost, el)
                el.x -= 5

                # удаление ghost которые за экраном
                if el.x < -40:
                    ghost_list_in_game.pop(i)

                if player_rect.colliderect(el): # отслеживание соприкосновений
                    gameplay = False


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

        # Планируем следующее появление: случайный интервал от 1.5 до 6 секунд
        if current_time >= next_ghost_spawn_time:
            ghost_list_in_game.append(ghost.get_rect(topleft=(620, 250)))
            next_ghost_spawn_time = current_time + random.randint(500, 6000)
    else:
        # screen.fill((87, 88, 89))
        screen.blit(lose_label, (180, 100))
        screen.blit(restart_label, restart_label_rect)


        if restart_label_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 0
            ghost_list_in_game.clear()

    pygame.display.update() # обновление экрана

    clock.tick(30) # кол-во фреймов в с (частота)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # кнопка выхода
            pygame.quit()
            running = False