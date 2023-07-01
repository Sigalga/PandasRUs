FPS = 30
USEREVENT = 32850
SECOND = 1000
WIN_SCORE = 85

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
WINDOW_DIMENSIONS = (SCREEN_WIDTH, SCREEN_HEIGHT)
DISPLAY_X = 42
DISPLAY_Y = 74
DISPLAY_WIDTH = 256
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_WIDTH)
BG_COLOR = (255, 255, 255)  # white
PLAYER_COLOR = (10, 12, 6)  # black
FONT_COLOR = (57, 50, 50)

BLOCK_WIDTH = 64
BLOCK_HEIGHT = 64
BLOCK_SIZE = [BLOCK_WIDTH, BLOCK_HEIGHT]

SHELF_AREA_WIDTH = 1317
SHELF_AREA_HEIGHT = 151
SHELF_AREA_SIZE = (SHELF_AREA_WIDTH, SHELF_AREA_HEIGHT)
SHELF_RAND_HEIGHT = 30

SHELF_AREA_X = 65
SHELF_AREA1_Y = 200
SHELF_AREA2_Y = 383
SHELF_AREA3_Y = 557
SHELF_AREA4_Y = 736
FLOOR_AREA_YS = (869, 868)
shelf_ys = (SHELF_AREA1_Y, SHELF_AREA2_Y, SHELF_AREA3_Y, SHELF_AREA4_Y)
all_ys = shelf_ys + FLOOR_AREA_YS
RAND_AREA_X1 = 71
RAND_AREA_X2 = 1260
DISPLAY_YS = (139, 868)

SHELF_AREA_COLOR = (0, 255, 0)
ACTIVE_SHELF_AREA_COLOR = (255, 255, 0)
DROP_AREA_COLOR = (0, 255, 255)

CONTROL_BAR_TIME_X = 210
CONTROL_BAR_SCORE_X = 1430
CONTROL_BAR_Y = 60

# Jerry animation
JERRY_START_TIME = 300
END_DELAY_TIME = 13
JERRY_W = 373
JERRY_H = 493
JERRY_SIZE_1 = (JERRY_W / 2, JERRY_H / 2)
JERRY_POS_1 = (1822, 406)
JERRY_SIZE_2 = (JERRY_W / 1.7, JERRY_H / 1.7)
JERRY_POS_2 = (1796, 411)
JERRY_SIZE_3 = (JERRY_W / 1.5, JERRY_H / 1.5)
JERRY_POS_3 = (1755, 420)
JERRY_SIZE_4 = (JERRY_W / 1.3, JERRY_H / 1.3)
JERRY_POS_4 = (1691, 433)
JERRY_SIZE_5 = (JERRY_W / 1.15, JERRY_H / 1.15)
JERRY_POS_5 = (1590, 454)
JERRY_SIZE_6 = (JERRY_W, JERRY_H)
JERRY_POS_6 = (1410, 492)
JERRY_ANGRY_SIZE = (297, JERRY_H)
JERRY_ANGRY_POS = (1445, 492)
JERRY_HAPPY_SIZE = JERRY_SIZE_6
JERRY_HAPPY_POS = (1410, 492)
jerry_sizes = (JERRY_SIZE_1, JERRY_SIZE_2, JERRY_SIZE_3, JERRY_SIZE_4, JERRY_SIZE_5, JERRY_SIZE_6)
jerry_poses = (JERRY_POS_1, JERRY_POS_2, JERRY_POS_3, JERRY_POS_4, JERRY_POS_5, JERRY_POS_6)
jerry_times = (30, 25, 20, 15, 10, 5, 0)

# toy types and size
toy_size = {'teddy': (169, 140),
            'ball': (118, 118),
            'hat': (171, 112),
            'barbie': (73, 135),
            'action_figure': (95, 137),
            'puzzle': (150, 111),
            'slime': (40, 50),
            'lego': (158, 100)}

# toy types and grid params (x, count)
toy_grid_params = {'teddy': {'x': 15, 'count': 7, 'drop_correct_x': 100, 'drop_correct_y': 15},
                   'ball': {'x': 10, 'count': 10, 'drop_correct_x': 80, 'drop_correct_y': 15},
                   'hat': {'x': 12, 'count': 7, 'drop_correct_x': 80, 'drop_correct_y': 40},
                   'barbie': {'x': 6, 'count': 16, 'drop_correct_x': 20, 'drop_correct_y': 20},
                   'action_figure': {'x': 12, 'count': 12, 'drop_correct_x': 30, 'drop_correct_y': 30},
                   'puzzle': {'x': 11, 'count': 8, 'drop_correct_x': 40, 'drop_correct_y': 30},
                   'lego': {'x': 17, 'count': 7, 'drop_correct_x': 80, 'drop_correct_y': 50},
                   'slime': {'x': 6, 'count': 28, 'drop_correct_x': 15, 'drop_correct_y': 15,\
                             '2nd_row_x': 23, '2nd_row_count': 27,\
                             '3rd_row_x': 43, '3rd_row_count': 26},
                   }
