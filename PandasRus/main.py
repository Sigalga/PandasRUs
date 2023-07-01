# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from graphics import *
import random
import pygame
import os


def init_game():
    global screen
    pygame.init()
    pygame.mixer.init()

    # Create a canvas on which to display everything
    screen = pygame.display.set_mode(WINDOW_DIMENSIONS, 0, 32)
    pygame.display.set_caption('Organize')


class Block(pygame.sprite.Sprite):
    def __init__(self, image, block_size, toy_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, block_size)
        self.rect = self.image.get_rect()
        self.toy_type = toy_type


class Shelf(pygame.sprite.Sprite):
    def __init__(self, area_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(area_size)
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.score = 0

    toy_count_in_shelf = {'teddy': 0,
                          'ball': 0,
                          'hat': 0,
                          'barbie': 0,
                          'action_figure': 0,
                          'puzzle': 0,
                          'slime': 0,
                          'lego': 0}

    def restart_shelf(self):
        for toy in self.toy_count_in_shelf.keys():
            self.toy_count_in_shelf[toy] = 0

    def calc_score(self):
        self.score = 0
        for toy in self.toy_count_in_shelf.keys():
            if toy == 'slime':
                if self.toy_count_in_shelf[toy] == 12:
                    self.score += 12.5
            elif self.toy_count_in_shelf[toy] == 3:
                self.score += 12.5


class DropArea(pygame.sprite.Sprite):
    def __init__(self, toy_type):
        pygame.sprite.Sprite.__init__(self)
        self.toy_type = toy_type
        self.image = pygame.Surface(toy_size[toy_type])
        self.image.fill(DROP_AREA_COLOR)
        self.rect = self.image.get_rect()

    toy_type = 'none'


class ToyGrid:
    def __init__(self, toy_type):
        self.toy_type = toy_type

    toy_type = 'none'

    def create_row_grid(self, row_count_key, row_x_key, is_small, row_number, shelf, grid):
        for i in range(0, toy_grid_params[self.toy_type][row_count_key], 1):
            drop_area = DropArea(self.toy_type)

            left_space = SHELF_AREA_X + 10
            if is_small:
                left_space = (left_space + toy_grid_params[self.toy_type][row_x_key])

            x = left_space + (toy_size[self.toy_type][0] * i) + (toy_grid_params[self.toy_type]['x'] * (i + 1))
            y = shelf + SHELF_AREA_HEIGHT - (toy_size[self.toy_type][1] * row_number)

            drop_area.rect.x = x
            drop_area.rect.y = y
            grid.add(drop_area)

    def create_grid(self):
        grid = pygame.sprite.Group()
        for shelf in shelf_ys:
            self.create_row_grid('count', 'x', False, 1, shelf, grid)
        return grid

    def create_grid_small(self):
        grid = pygame.sprite.Group()
        for shelf in shelf_ys:
            self.create_row_grid('count', 'x', True, 1, shelf, grid)
            self.create_row_grid('2nd_row_count', '2nd_row_x', True, 2, shelf, grid)
            self.create_row_grid('3rd_row_count', '3rd_row_x', True, 3, shelf, grid)
        return grid


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([1, 1])
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()

    carry_block_list = []

    def update(self):
        pos = pygame.mouse.get_pos()
        diff_x = self.rect.x - pos[0]
        diff_y = self.rect.y - pos[1]

        for block in self.carry_block_list:
            block.rect.x -= diff_x
            block.rect.y -= diff_y

        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Jerry(pygame.sprite.Sprite):
    def __init__(self, image, area_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(area_size)
        self.image.fill(SHELF_AREA_COLOR)
        self.rect = self.image.get_rect()


class Button(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.size_w = size[0]
        self.size_h = size[1]
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size)
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        screen.blit(self.image, (self.pos_x, self.pos_y))

    def click(self, event):
        curr_page1 = True
        curr_page2 = True
        next_page = False
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.pos_x < x < (self.pos_x + self.size_w) and self.pos_y < y < (self.pos_y + self.size_h):
                    curr_page1 = False
                    curr_page2 = False
                    next_page = True
        return curr_page1, curr_page2, next_page


def create_toys(item, block_group, all_sprites_group):
    block = Block(item['img'], item['size'], item['type'])

    rand_ys = []
    for y in all_ys:
        rand_ys.append(random.randint(y, y + SHELF_RAND_HEIGHT))

    block.rect.y = random.choice(rand_ys)
    block.rect.x = random.randint(RAND_AREA_X1, RAND_AREA_X2)

    block_group.add(block)
    all_sprites_group.add(block)


def create_next_page_button(next_page_img, button_pos, button_size, done, prev_page1, prev_page2, next_page):
    screen.blit(next_page_img, (0, 0))
    restart_game_button = Button(button_pos, button_size)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        else:
            prev_page1, prev_page2, next_page = restart_game_button.click(event)
    return done, prev_page1, prev_page2, next_page


def create_next_page_button_(next_page_img, button_pos, button_size, done, prev_page, next_page):
    done, prev_page1, prev_page2, next_page = create_next_page_button(next_page_img, button_pos, button_size, done,
                                                                      prev_page, prev_page, next_page)
    prev_page = prev_page1
    return done, prev_page, next_page


def main():
    init_game()

    # background music
    music = pygame.mixer.music.load(os.path.join('sound', 'tunetank.com_5412_rooftop-sunsets_by_alexey-anisimov.mp3'))

    block_group = pygame.sprite.Group()
    all_sprites_group = pygame.sprite.Group()
    shelf_group = pygame.sprite.Group()

    player = Player()
    all_sprites_group.add(player)

    # create store items   #TODO: fix restart bug
    for item in item_list:
        for i in range(0, 3, 1):
            create_toys(item, block_group, all_sprites_group)
    for item in item_list_small:
        for i in range(0, 2, 1):
            create_toys(item, block_group, all_sprites_group)
    is_toys_created = True

    # create shelves
    for shelf_y in shelf_ys:
        shelf = Shelf(SHELF_AREA_SIZE)
        shelf.rect.x = SHELF_AREA_X
        shelf.rect.y = shelf_y
        shelf_group.add(shelf)

    # create jerry
    jerry_timer = JERRY_START_TIME
    end_delay_time = END_DELAY_TIME
    jerry_img = jerry_away
    jerry_location = (0, 0)

    is_dropped = False
    # is_toys_created = False

    # page_choices
    welcome_page = True
    game_page = False
    game_over_page = False
    win_page = False
    end_game = False
    credits_page = False
    close = False

    clock = pygame.time.Clock()
    done = False
    pygame.mixer.music.play(-1)
    # -------------- Game loop -----------------------------------------------------
    while not done:
        if welcome_page:
            pygame.mixer.music.pause()
            done, welcome_page, game_page = create_next_page_button_(
                open_screen_img, (732, 604), (415, 96), done, welcome_page, game_page)

            # reset jerry
            jerry_timer = JERRY_START_TIME
            end_delay_time = END_DELAY_TIME
            jerry_img = jerry_away
            jerry_location = (0, 0)

            # if not is_toys_created:   #TODO: fix restart bug
            #     # create store items
            #     for item in item_list:
            #         for i in range(0, 3, 1):
            #             create_toys(item, block_group, all_sprites_group)
            #     for item in item_list_small:
            #         for i in range(0, 2, 1):
            #             create_toys(item, block_group, all_sprites_group)
            #     is_toys_created = True

        elif game_page:
            pygame.mixer.music.unpause()
            screen.blit(bg_img, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if 0 < jerry_timer:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        blocks_hit_list = pygame.sprite.spritecollide(player, block_group, False)
                        if len(blocks_hit_list) > 0:
                            player.carry_block_list.append(blocks_hit_list[-1])
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if len(player.carry_block_list) > 0:
                            is_dropped = True
                        player.carry_block_list = []

            block_group.update()
            all_sprites_group.update()
            if is_dropped:
                pygame.mixer.Sound.play(drop_click)
                is_dropped = False

            if jerry_timer > 0:
                jerry_timer -= 1

            # total score calculation
            score = 0
            for shelf in shelf_group:
                shelf.restart_shelf()
                for block in block_group:
                    if (shelf.rect.left <= block.rect.left and block.rect.right <= shelf.rect.right) and \
                            (shelf.rect.top <= block.rect.top and block.rect.bottom <= shelf.rect.bottom):
                        # toy is in shelf area
                        shelf.toy_count_in_shelf[block.toy_type] += 1
                shelf.calc_score()
                if shelf.score >= 24:
                    shelf.image.set_alpha(20)
                    shelf.image.fill(ACTIVE_SHELF_AREA_COLOR)
                else:
                    # shelf.image.fill(SHELF_AREA_COLOR)
                    shelf.image.set_alpha(0)
                score += shelf.score

            # Jerry animation
            if jerry_timer > 0:
                for j in range(0, len(jerry_times) - 1, 1):
                    if jerry_times[j+1] < jerry_timer < jerry_times[j]:
                        jerry_img = jerry_list[j][0]
                        jerry_location = jerry_list[j][1]
            else:
                if score < WIN_SCORE:
                    jerry_img = jerry_angry
                    jerry_location = JERRY_ANGRY_POS
                    game_over_page = True
                else:
                    jerry_img = jerry_happy
                    jerry_location = JERRY_HAPPY_POS
                    win_page = True
                end_delay_time -= 1
                if end_delay_time == 0:
                    game_page = False
                    end_game = True
            screen.blit(jerry_img, jerry_location)

            # create drop area grids
            grid_list = {}
            for toy_type in toy_grid_params.keys():
                toy_grid_inst = ToyGrid(toy_type)
                if toy_type == 'slime':
                    grid = toy_grid_inst.create_grid_small()
                else:
                    grid = toy_grid_inst.create_grid()
                grid_list[toy_type] = grid

            # toy dropping logics
            drop_click = pygame.mixer.Sound(os.path.join('sound', 'mixkit-cool-interface-click-tone-2568.wav'))
            for grid_key in grid_list.keys():
                for block in block_group:
                    if block.toy_type == grid_key:
                        for drop_area in grid_list[grid_key]:
                            correct_x = toy_grid_params[grid_key]['drop_correct_x']
                            correct_y = toy_grid_params[grid_key]['drop_correct_y']
                            if drop_area.rect.left - correct_x <= block.rect.left \
                                    and block.rect.right <= drop_area.rect.right + correct_x \
                                    and drop_area.rect.top - correct_y <= block.rect.top \
                                    and block.rect.bottom <= drop_area.rect.bottom + correct_y:
                                block.rect.x = drop_area.rect.x
                                block.rect.y = drop_area.rect.y

            shelf_group.draw(screen)
            # grid.draw(screen)
            block_group.draw(screen)
            all_sprites_group.draw(screen)

            # create control panel
            screen.blit(frame_img, (0, 0))
            controls_font = pygame.font.Font(os.path.join('fonts', 'TitanOne-Regular.ttf'), 40)
            surf = controls_font.render('TIME LEFT: %d' % jerry_timer, True, FONT_COLOR)
            screen.blit(surf, (CONTROL_BAR_TIME_X, CONTROL_BAR_Y))
            surf = controls_font.render('SCORE: %d' % score, True, FONT_COLOR)
            screen.blit(surf, (CONTROL_BAR_SCORE_X, CONTROL_BAR_Y))

            clock.tick(200)

        if end_game:
            pygame.mixer.music.pause()
            if game_over_page:
                done, end_game, game_over_page, welcome_page = create_next_page_button(
                    game_over_img, (741, 361), (480, 96), done, end_game, game_over_page, welcome_page)
                # is_toys_created = False   #TODO: fix restart bug
            elif win_page:
                done, win_page, credits_page = create_next_page_button_(
                    win_img, (817, 361), (287, 95), done, win_page, welcome_page)
            elif credits_page:
                done, credits_page, close = create_next_page_button_(
                    credits_img, (817, 539), (287, 96), done, credits_page, close)
            elif close:
                done = True

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
