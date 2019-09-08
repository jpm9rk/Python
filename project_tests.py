# Final project in python computer science class
# Creates a game
# Code written in conjunction with Sean McDonald at the University of Virginia


import pygame
import gamebox

# Set camera
camera = gamebox.Camera(800, 600)

# Set booleans for title screen and game over screen
title_screen = True
instructions_screen = False
character_select_screen = False
end_game = False
current_level = 1
# Set traits for player/tiles/enemies
tile_color = 'white'
tile_width = 30
tile_height = 30
player = gamebox.from_image(30, 300, 'donald.png')
finish_index = 0
# Active level tiles
tiles = []
collectible_list = []
enemies_list = []

# Level tiles locations
level_1 = [[100, 100, 'start'],
           [130, 100],
           [160, 100],
           [190, 100],
           [220, 100],
           [250, 100],
           [280, 100],
           [340, 100],
           [400, 100],
           [460, 100],
           [520, 100, "finish"],  # finish block
           [280, 130],  # down branch starts here
           [280, 160],
           [280, 190],
           [280, 220],
           [280, 250],
           [280, 280],
           [310, 280],
           [340, 280, "collectible"],  # collectible here

           ]
# Tile coordinates for level 2
level_2 = [[30, 300, 'start'],
           [60, 300],
           [90, 300],
           [120, 300],
           [120, 270],
           [120, 240, "collectible"],
           [120, 330],
           [120, 360],
           [120, 390],
           [120, 420],
           [60, 450],
           [90, 450, "collectible"],
           [120, 450],
           [150, 450],
           [180, 450],
           [210, 450],
           [240, 450],
           [270, 450],
           [270, 420],
           [270, 390],
           [270, 480],
           [270, 510],
           [330, 450],
           [390, 450],
           [450, 450],
           [510, 450],
           [570, 450],
           [630, 450],
           [150, 300],
           [180, 300],
           [210, 300],
           [240, 300],
           [270, 300],
           [300, 300],
           [330, 300],
           [360, 300],
           [390, 300],
           [420, 300],
           [450, 300],
           [480, 300],
           [510, 300],
           [540, 300],
           [570, 300],
           [630, 300, "finish"],
           [180, 240],
           [180, 210],
           [180, 180],
           [210, 180],
           [240, 180],
           [270, 180],
           [300, 180],
           [330, 180],
           [360, 180],
           [390, 180],
           [420, 180],
           [450, 180],
           [480, 180],
           [480, 210],
           [480, 240],
           [330, 330],
           [330, 360],
           [330, 390],
           [360, 390],
           [390, 390],
           [390, 360, "collectible"],
           [390, 330],
           [630, 390, "collectible"]
           ]

level_3 = [[60, 260, 'start'],
           [90, 50],
           [90, 80],
           [90, 110],
           [90, 140],
           [90, 170],
           [90, 200],
           [90, 230],
           [90, 260],
           [120, 260],
           [120, 230],
           [120, 200],
           [120, 170],
           [120, 140],
           [120, 110],
           [120, 80],
           [120, 50],
           [150, 50],
           [150, 80],
           [150, 110],
           [150, 140],
           [150, 170],
           [150, 200],
           [150, 230],
           [150, 260],
           [180, 260],
           [180, 230],
           [180, 200],
           [180, 170],
           [180, 140],
           [180, 110],
           [180, 80],
           [180, 50],
           [210, 50],
           [210, 80],
           [210, 110],
           [210, 140],
           [210, 170],
           [210, 200],
           [210, 230],
           [210, 260],
           [240, 260],
           [240, 230],
           [240, 200],
           [240, 170],
           [240, 140],
           [240, 110],
           [240, 80],
           [240, 50],
           [270, 50],
           [270, 80],
           [270, 110],
           [270, 140],
           [270, 170],
           [270, 200],
           [270, 230, 'collectible'],
           [270, 260],
           [300, 260],
           [300, 230],
           [300, 200],
           [300, 170],
           [300, 140],
           [300, 110],
           [300, 80],
           [300, 50],
           [330, 50],
           [330, 80],
           [330, 110],
           [330, 140],
           [330, 170],
           [330, 200],
           [330, 230, 'collectible'],
           [330, 260],
           [360, 260],
           [360, 230],
           [360, 200],
           [360, 170],
           [360, 140],
           [360, 110],
           [360, 80],
           [360, 50],
           [390, 50],
           [390, 80],
           [390, 110],
           [390, 140, 'collectible'],
           [390, 170],
           [390, 200],
           [390, 230],
           [390, 260],
           [420, 260],
           [420, 230],
           [420, 200],
           [420, 170],
           [420, 140],
           [420, 110],
           [420, 80],
           [420, 50],
           [450, 50],
           [450, 80],
           [450, 110],
           [450, 140],
           [450, 170],
           [450, 200],
           [450, 230],
           [450, 260],
           [480, 260, 'collectible'],
           [480, 230],
           [480, 200],
           [480, 170],
           [480, 140],
           [480, 110],
           [480, 80],
           [480, 50],
           [510, 50],
           [510, 80],
           [510, 110],
           [510, 140],
           [510, 170],
           [510, 200],
           [510, 230],
           [510, 260],
           [540, 260],
           [540, 230],
           [540, 200],
           [540, 170],
           [540, 140],
           [540, 110],
           [540, 80],
           [540, 50],
           [570, 50],
           [570, 80, 'collectible'],
           [570, 110],
           [570, 140],
           [570, 170],
           [570, 200],
           [570, 230],
           [570, 260],
           [600, 260],
           [600, 230],
           [600, 200],
           [600, 170],
           [600, 140],
           [600, 110],
           [600, 80],
           [600, 50],
           [600, 260],
           [720, 260, 'finish'],
           [90, 290],
           [90, 320],
           [90, 350],
           [90, 380],
           [90, 410],
           [90, 440],
           [90, 470],
           [90, 500],
           [120, 500],
           [120, 470],
           [120, 440],
           [120, 410],
           [120, 380],
           [120, 350],
           [120, 320],
           [120, 290],
           [150, 290],
           [150, 320],
           [150, 350],
           [150, 380],
           [150, 410],
           [150, 440],
           [150, 470],
           [150, 500],
           [180, 500],
           [180, 470],
           [180, 440],
           [180, 410],
           [180, 380],
           [180, 350],
           [180, 320],
           [180, 290],
           [210, 290],
           [210, 320],
           [210, 350],
           [210, 380],
           [210, 410],
           [210, 440],
           [210, 470],
           [210, 500],
           [240, 500],
           [240, 470],
           [240, 440],
           [240, 410],
           [240, 380],
           [240, 350],
           [240, 320],
           [240, 290],
           [270, 290],
           [270, 320],
           [270, 350],
           [270, 380],
           [270, 410],
           [270, 440],
           [270, 470],
           [270, 500],
           [300, 500],
           [300, 470],
           [300, 440],
           [300, 410],
           [300, 380],
           [300, 350],
           [300, 320],
           [300, 290],
           [330, 290],
           [330, 320],
           [330, 350],
           [330, 380],
           [330, 410],
           [330, 440],
           [330, 470],
           [330, 500],
           [360, 500],
           [360, 470],
           [360, 440],
           [360, 410],
           [360, 380],
           [360, 350],
           [360, 320],
           [360, 290],
           [390, 290],
           [390, 320],
           [390, 350],
           [390, 380],
           [390, 410],
           [390, 440],
           [390, 470],
           [390, 500],
           [420, 500],
           [420, 470],
           [420, 440],
           [420, 410],
           [420, 380],
           [420, 350],
           [420, 320],
           [420, 290],
           [450, 290],
           [450, 320],
           [450, 350],
           [450, 380],
           [450, 410],
           [450, 440],
           [450, 470],
           [450, 500],
           [480, 500],
           [480, 470],
           [480, 440],
           [480, 410],
           [480, 380],
           [480, 350],
           [480, 320],
           [480, 290],
           [510, 290],
           [510, 320],
           [510, 350],
           [510, 380],
           [510, 410],
           [510, 440],
           [510, 470],
           [510, 500],
           [540, 500],
           [540, 470],
           [540, 440],
           [540, 410],
           [540, 380],
           [540, 350],
           [540, 320],
           [540, 290],
           [570, 290],
           [570, 320],
           [570, 350],
           [570, 380],
           [570, 410],
           [570, 440],
           [570, 470],
           [570, 500],
           [600, 500, 'collectible'],
           [600, 470],
           [600, 440],
           [600, 410],
           [600, 380],
           [600, 350],
           [600, 320],
           [600, 290]]




# level_3.append([600, 260])
# level_3.append([630, 260])
# level_3.append([660, 260])
# level_3.append([690, 260, 'finish'])



enemies_level_3 = [
    {
        'enemy': gamebox.from_image(300, 200, 'slime.png'),
        'start': [300, 200],
        'finish': [300, 260],
        'direction': 'vertical',
        'speed': 7.5
    },
    {
        'enemy': gamebox.from_image(540, 60, 'slime.png'),
        'start': [540, 60],
        'finish': [540, 320],
        'direction': 'vertical',
        'speed': 2.5
    },
    {
        'enemy': gamebox.from_image(330, 200, 'slime.png'),
        'start': [330, 200],
        'finish': [540, 200],
        'direction': 'horizontal',
        'speed': 2.5
    },
    {
        'enemy': gamebox.from_image(300, 350, 'slime.png'),
        'start': [300, 350],
        'finish': [600, 350],
        'direction': 'horizontal',
        'speed': 5
    },
    {
        'enemy': gamebox.from_image(540, 440, 'slime.png'),
        'start': [540, 440],
        'finish': [540, 500],
        'direction': 'vertical',
        'speed': 7.5
    },
    {
        'enemy': gamebox.from_image(600, 440, 'slime.png'),
        'start': [540, 440],
        'finish': [600, 440],
        'direction': 'horizontal',
        'speed': 7.5
    },
    {
        'enemy': gamebox.from_image(360, 230, 'slime.png'),
        'start': [360, 230],
        'finish': [360, 500],
        'direction': 'vertical',
        'speed': 2
    },
    {
        'enemy': gamebox.from_image(450, 90, 'slime.png'),
        'start': [450, 90],
        'finish': [450, 180],
        'direction': 'vertical',
        'speed': 2
    },
    {
        'enemy': gamebox.from_image(180, 50, 'slime.png'),
        'start': [180, 50],
        'finish': [180, 500],
        'direction': 'vertical',
        'speed': 5
    },
    {
        'enemy': gamebox.from_image(180, 110, 'slime.png'),
        'start': [180, 110],
        'finish': [360, 110],
        'direction': 'horizontal',
        'speed': 2.5
    }

]


# The enemies lists will be a list of dictionaries, each containing 5 keys that give information about that enemy. 'enemy' is the gamebox,
# 'start' should be the coordinate furthest left (horizontal) or furthest up (vertical), 'direction' should be either horizontal or vertical, 'speed' can be any number you want
enemies_level_2 = [
    {
        'enemy': gamebox.from_image(60, 450, 'slime.png'),
        'start': [60, 450],
        'finish': [210, 450],
        'direction': 'horizontal',
        'speed': 2.5
    }, {
        'enemy': gamebox.from_image(270, 390, 'slime.png'),
        'start': [270, 390],
        'finish': [270, 510],
        'direction': 'vertical',
        'speed': 2.5
    }, {
        'enemy': gamebox.from_image(180, 300, 'slime.png'),
        'start': [180, 300],
        'finish': [480, 300],
        'direction': 'horizontal',
        'speed': 10
    }, {
        'enemy': gamebox.from_image(330, 300, 'slime.png'),
        'start': [330, 300],
        'finish': [390, 300],
        'direction': 'horizontal',
        'speed': 2
    }

]


# This function puts the enemy dictionaries for a level into the general enemies list
def place_enemies(level_enemies_list):
    """
    Accesses enemies list and then appends to this list all the enemies in the level enemy list.

    :param level_enemies_list: (list) Starts as empty list
    :return: None
    """
    global enemies_list
    enemies_list = []
    for enemy in level_enemies_list:
        enemies_list.append(enemy)


def place_collectibles(x, y):
    """
    Accesses collectible list and then places collectibles at x,y positions passed as arguments.

    :param x: (int) x-position of collectible
    :param y: (int) y-position of collectible
    :return: None
    """
    global collectible_list
    collectible_list.append(
        gamebox.from_image(x, y, 'potion.png'))  # places collectibles based on x, y coordinates (used in build_level)


# Level generation function (Does not display, just translates coordinates to tiles that can be drawn)
def build_level(coordinate_list):
    """
    Builds a level based on a list of coordinates given containing info about blocks and collectibles.

    Accesses the tile list, and for each element in coordinate list, appends this element to tiles[]
    :param coordinate_list:(list) Each element contains a pair of coordinates
    :return: None
    """
    global tiles
    global finish_index
    global start_index
    global collectible_list
    collectible_list = []
    i = 0
    for pair in coordinate_list:
        if i % 2 == 0:
            tile_color = 'white'
        else:
            tile_color = 'grey'
        if 'finish' in pair:  # changes color of tiles marked with "finish"
            tile_color = 'green'
            finish_index = i
        if 'start' in pair:
            player.center = (pair[0], pair[1])
        if 'collectible' in pair:  # sets a collectible on tiles marked "collectible"
            place_collectibles(pair[0], pair[1])
        new_tile = gamebox.from_color(pair[0], pair[1], tile_color, tile_width, tile_height)
        tiles.append(new_tile)
        i += 1


def reset_level_lose_health():  # moves player to the start level, and builds that level
    """
    Drop player health by one,recenter them at the start of the current level, and remove any movement bonus.

    :return:  None
    """
    global num_lives
    global health_bar
    global movement_bonus
    num_lives -= 1
    health_bar = gamebox.from_color(100, 20, 'red', 20 * num_lives, 10)
    if current_level == 1:
        player.center = [100, 100]
        build_level(level_1)
    if current_level == 2:
        player.center = [30, 300]
        build_level(level_2)
    if current_level == 3:
        player.center = [60, 260]
        build_level(level_3)
    movement_bonus = 0


def next_level():  # changes is_game_finished to true, resets tiles, builds the next level
    """
    Build the next level and increment the current level counter by 1.

    Resets the is_game_finished flag to False, resets movement bonus, resets tile list to [].
    Build level consists of calling the build_level and place_enemies functions for the respective level
    :return:None
    """
    global current_level
    global tiles
    global movement_bonus
    global is_game_finished
    is_game_finished = False
    tiles = []
    movement_bonus = 0
    if current_level == 1:
        build_level(level_2)
        place_enemies(enemies_level_2)
    if current_level == 2:
        build_level(level_3)
        place_enemies(enemies_level_3)
    # if current_level == 3:
    #     #     build_level(level_3)
    #     #     place_enemies(enemies_level_3)
    current_level += 1


movement_bonus = 0
is_game_finished = False
did_player_lose = False
num_lives = 3
health_bar = gamebox.from_color(100, 20, 'red', 60, 10)


# Game flow
def tick(keys):
    global title_screen
    global instructions_screen
    global character_select_screen
    global movement_bonus
    global collectible
    global is_game_finished
    global did_player_lose
    global num_lives
    global health_bar
    global player

    finish_screen = False
    # Starting game logic
    # If we are on the title screen
    if title_screen:  # if they haven't pressed space show the title screen
        camera.clear('black')  # make a black background

        # Placeholder Title Screen
        title_screen_content = gamebox.from_image(400, 300, 'title_screen.png')
        camera.draw(title_screen_content)

        # Testing stage bypass
        if pygame.K_1 in keys:
            title_screen = False
            build_level(level_1)

        if pygame.K_2 in keys:
            title_screen = False
            build_level(level_2)
            place_enemies(enemies_level_2)

        if pygame.K_3 in keys:
            title_screen = False
            build_level(level_3)
            place_enemies(enemies_level_3)

        # Move to the instructions screen
        if pygame.K_SPACE in keys:
            title_screen = False
            instructions_screen = True
        keys.clear()

    elif instructions_screen:
        instructions_content = gamebox.from_image(400, 300, 'instructions.png')
        camera.draw(instructions_content)
        if pygame.K_SPACE in keys:
            instructions_screen = False
            character_select_screen = True
        keys.clear()

    elif character_select_screen:
        character_select_content = gamebox.from_image(400, 400, 'character_select.png')
        camera.draw(character_select_content)
        if pygame.K_d in keys:
            character_select_screen = False
            player = gamebox.from_image(30, 300, 'donald.png')
            build_level(level_1)
        if pygame.K_g in keys:
            character_select_screen = False
            player = gamebox.from_image(30, 300, 'gondalf.png')
            build_level(level_1)
        if pygame.K_s in keys:
            character_select_screen = False
            player = gamebox.from_image(30, 300, 'SirDay.png')
            build_level(level_1)
        player.scale_by(.92)
        keys.clear()

    elif (not did_player_lose) and (not is_game_finished):
        finish = tiles[finish_index]
        camera.clear('black')
        for tile in tiles:
            camera.draw(tile)
        for collectible in collectible_list:
            camera.draw(collectible)
        # If the player presses a key move their character 30 pixels in that direction
        if pygame.K_LEFT in keys:
            player.x -= 30 + movement_bonus * 30
        if pygame.K_RIGHT in keys:
            player.x += 30 + movement_bonus * 30
        if pygame.K_DOWN in keys:
            player.y += 30 + movement_bonus * 30
        if pygame.K_UP in keys:
            player.y -= 30 + movement_bonus * 30
        # If the player runs into a collectible increase their speed by 1
        if len(collectible_list) != 0:
            for collectible in collectible_list:
                if player.touches(collectible):
                    collectible_list.remove(collectible)
                    movement_bonus += 1
        # Enemy Movement Mechanism
        for dct in enemies_list:
            enemy = dct['enemy']
            if player.touches(enemy):
                reset_level_lose_health()  # build the level and place player back at start
            if dct['direction'] == 'horizontal':
                if enemy.x == dct['start'][0]:
                    enemy.speedx = dct['speed']
                if enemy.x == dct['finish'][0]:
                    enemy.speedx = dct['speed'] * -1
            if dct['direction'] == 'vertical':
                if enemy.y == dct['start'][1]:
                    enemy.speedy = dct['speed']
                if enemy.y == dct['finish'][1]:
                    enemy.speedy = dct['speed'] * -1
            enemy.move_speed()
            camera.draw(enemy)

        # If the player makes contact with the finish line block, change the finished flag to true and
        # display the finish screen
        if player.touches(finish):
            is_game_finished = True
            finish_screen = gamebox.from_text(400, 400, "YOU WIN!", 50, 'red')
            if current_level == 3:
                camera.draw(finish_screen)
                gamebox.pause()
            else:
                next_level()  # is_game_finished changed to false and tiles resets to []
        keys.clear()
        camera.draw(player)

        # lose health if player moves off of map
        on_map = 0
        for block in tiles:
            if player.touches(block):
                on_map += 1
        if on_map == 0:
            reset_level_lose_health()
        if num_lives == 0:
            did_player_lose = True

        health_meter = gamebox.from_text(35, 20, 'HEALTH: ', 20, 'red')
        camera.draw(health_bar)
        camera.draw(health_meter)
    elif did_player_lose:
        game_lost_screen = gamebox.from_text(400, 400, "YOU LOSE!", 50, 'red')
        camera.draw(game_lost_screen)



    camera.display()


gamebox.timer_loop(30, tick)






