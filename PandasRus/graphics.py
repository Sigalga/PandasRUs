import pygame

from params import *


def render_image(file, size):
    image = pygame.image.load(file)
    image = pygame.transform.scale(image, size)
    return image


item_list = ({'img': 'graphics/toy_teddy.png', 'size': (169, 140), 'type': 'teddy'},
             {'img': 'graphics/toy_ball.png', 'size': (118, 118), 'type': 'ball'},
             {'img': 'graphics/toy_hat.png', 'size': (171, 112), 'type': 'hat'},
             {'img': 'graphics/toy_barbie.png', 'size': (73, 135), 'type': 'barbie'},
             {'img': 'graphics/toy_gipoe.png', 'size': (95, 137), 'type': 'action_figure'},
             {'img': 'graphics/toy_puzzle.png', 'size': (150, 111), 'type': 'puzzle'},
             {'img': 'graphics/toy_lego.png', 'size': (158, 100), 'type': 'lego'})

item_list_small = ({'img': 'graphics/toy_slime_blue.png', 'size': (40, 50), 'type': 'slime'},
                   {'img': 'graphics/toy_slime_red.png', 'size': (40, 50), 'type': 'slime'},
                   {'img': 'graphics/toy_slime_green.png', 'size': (40, 50), 'type': 'slime'},
                   {'img': 'graphics/toy_slime_orange.png', 'size': (40, 50), 'type': 'slime'},
                   {'img': 'graphics/toy_slime_pink.png', 'size': (40, 50), 'type': 'slime'},
                   {'img': 'graphics/toy_slime_yellow.png', 'size': (40, 50), 'type': 'slime'})

jerry_away = pygame.Surface((0, 0))
jerry_list = []
for i in range(0, len(jerry_sizes), 1):
    jerry_list.append((render_image('graphics/jerry.png', jerry_sizes[i]), jerry_poses[i]))
# jerry1 = render_image('graphics/jerry.png', JERRY_SIZE_1)
# jerry2 = render_image('graphics/jerry.png', JERRY_SIZE_2)
# jerry3 = render_image('graphics/jerry.png', JERRY_SIZE_6)
jerry_angry = render_image('graphics/jerry_angry.png', JERRY_ANGRY_SIZE)
jerry_happy = render_image('graphics/jerry_happy.png', JERRY_HAPPY_SIZE)
# jerry_list = ((jerry1, (JERRY_X1, JERRY_Y1)),
#               (jerry2, (JERRY_X2, JERRY_Y2)),
#               (jerry3, (JERRY_X6, JERRY_Y6)))

bg_img = render_image('graphics/panda-store-background.png', WINDOW_DIMENSIONS)
frame_img = render_image('graphics/panda-store-frame.png', WINDOW_DIMENSIONS)
open_screen_img = render_image('graphics/open-screen.png', WINDOW_DIMENSIONS)
game_over_img = render_image('graphics/game_over.png', WINDOW_DIMENSIONS)
win_img = render_image('graphics/win.png', WINDOW_DIMENSIONS)
credits_img = render_image('graphics/credits.png', WINDOW_DIMENSIONS)
