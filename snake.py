import os
import random
import shutil
import sys
import time
import keyboard
import pygame

os_name = os.name

def main(score = None):
    os.system('cls' if os_name == 'nt' else 'clear')
    pygame.mixer.init()
    sound_menu_roll = pygame.mixer.Sound('sounds/menu-roll.mp3')
    sound_menu_enter = pygame.mixer.Sound('sounds/menu-enter.mp3')
    menu_buttons = [("Play", player_mode_menu),("Help", help_menu), ("Exit", sys.exit)]
    menu_buttons_len = len(menu_buttons)-1
    
    selected_button = 0

    columns, lines = shutil.get_terminal_size(fallback=())

    if score:
        print(f"\033[{lines//2-1};{columns//2}H"+f"|END WITH SCORE: {score}|")
    for i, button in enumerate(menu_buttons):
        button_name, button_function = button
        if i == selected_button:
            print(f"\033[{(lines//2+i)};{columns//2-(len(button_name))//2}H>{button_name}<",end='')
        else:
            print(f"\033[{(lines//2+i)};{columns//2-(len(button_name))//2}H {button_name} ",end='')
    print(f"\033[{(lines-2)};{0}H" + "Menu Controls:",end='')
    print(f"\033[{(lines-1)};{0}H" + "Arrow UP, Arrow DOWN, W, S, ENTER",end='')
    print(f"\033[{(lines)};{0}H" + "Snake v0.65 (2023)",end='')
    sys.stdout.flush()
    while(True):
        event = keyboard.read_event()
        columns, lines = shutil.get_terminal_size(fallback=())
        if event.name == 'up' and event.event_type == 'up' or event.name == 'w' and event.event_type  == 'up' or event.name == 'ц' and event.event_type  == 'up':
            sound_menu_roll.play()
            selected_button-=1
            if selected_button < 0:
                selected_button = menu_buttons_len
        elif event.name == 'down' and event.event_type == 'up' or event.name == 's' and event.event_type  == 'up' or event.name == 'ы' and event.event_type  == 'up':
            sound_menu_roll.play()
            selected_button+=1
            if selected_button > menu_buttons_len:
                selected_button = 0
        for i, button in enumerate(menu_buttons):
            button_name, button_function = button
            if event.name == 'enter' and event.event_type == 'up' and i == selected_button:
                sound_menu_enter.play()
                button_function()
            if i == selected_button:
                print(f"\033[{(lines//2+i)};{columns//2-(len(button_name))//2}H>{button_name}<")
            else:
                print(f"\033[{(lines//2+i)};{columns//2-(len(button_name))//2}H {button_name} ")

def player_mode_menu():
    os.system('cls' if os_name == 'nt' else 'clear')
    pygame.mixer.init()
    sound_menu_roll = pygame.mixer.Sound('sounds/menu-roll.mp3')
    sound_menu_enter = pygame.mixer.Sound('sounds/menu-enter.mp3')
    menu_buttons = [("Single Player", start_game_single_player),("Multi Player", start_game_multi_player), ("Back", main)]
    menu_buttons_len = len(menu_buttons)-1
    
    selected_button = 0

    columns, lines = shutil.get_terminal_size(fallback=())

    for i, button in enumerate(menu_buttons):
        button_name, button_function = button
        if i == selected_button:
            print(f"\033[{(lines//2+i)};{columns//2-(len(button_name))//2}H>{button_name}<",end='')
        else:
            print(f"\033[{(lines//2+i)};{columns//2-(len(button_name))//2}H {button_name} ",end='')
    print(f"\033[{(lines-2)};{0}H" + "Menu Controls:",end='')
    print(f"\033[{(lines-1)};{0}H" + "Arrow UP, Arrow DOWN, W, S, ENTER",end='')
    print(f"\033[{(lines)};{0}H" + "Snake v0.65 (2023)",end='')
    sys.stdout.flush()
    while(True):
        event = keyboard.read_event()
        columns, lines = shutil.get_terminal_size(fallback=())
        if event.name == 'up' and event.event_type == 'up' or event.name == 'w' and event.event_type  == 'up' or event.name == 'ц' and event.event_type  == 'up':
            sound_menu_roll.play()
            selected_button-=1
            if selected_button < 0:
                selected_button = menu_buttons_len
        elif event.name == 'down' and event.event_type == 'up' or event.name == 's' and event.event_type  == 'up' or event.name == 'ы' and event.event_type  == 'up':
            sound_menu_roll.play()
            selected_button+=1
            if selected_button > menu_buttons_len:
                selected_button = 0
        for i, button in enumerate(menu_buttons):
            button_name, button_function = button
            if event.name == 'enter' and event.event_type == 'up' and i == selected_button:
                sound_menu_enter.play()
                button_function()
            if i == selected_button:
                print(f"\033[{(lines//2+i)};{columns//2-(len(button_name))//2}H>{button_name}<")
            else:
                print(f"\033[{(lines//2+i)};{columns//2-(len(button_name))//2}H {button_name} ")

def help_menu():
    os.system('cls' if os_name == 'nt' else 'clear')
    pygame.mixer.init()
    sound_menu_enter = pygame.mixer.Sound('sounds/menu-enter.mp3')
    help_articles = ["Keyboard Bindings:","Menu - arrow UP, arrow DOWN, W, S, ENTER","Snake - arrow UP, arrow DOWN, arrow LEFT, arrow RIGHT or W, A, S, D","How To Play:","Your task is to eat as many apples as possible (indicated by the symbol O)","And make sure that the snake does not touch itself."]
    menu_buttons = [("Back", main)]
    max_article_len = len(max(help_articles, key=len))
    help_articles_len = len(help_articles)+1
    menu_buttons_len = len(menu_buttons)-1
    selected_button = 0
    columns, lines = shutil.get_terminal_size(fallback=())
    for i, article in enumerate(help_articles):
        print(f"\033[{(lines//2+i)};{columns//2-max_article_len//2}H{article}")
    for i, button in enumerate(menu_buttons):
        button_name, button_function = button
        if i == selected_button:
            print(f"\033[{(lines//2+i+help_articles_len)};{columns//2-(len(button_name))//2}H>{button_name}<")
        else:
            print(f"\033[{(lines//2+i+help_articles_len)};{columns//2-(len(button_name))//2}H {button_name} ")
    while(True):
        event = keyboard.read_event()
        columns, lines = shutil.get_terminal_size(fallback=())
        if event.name == 'up' and event.event_type == 'up' or event.name == 'w' and event.event_type  == 'up' or event.name == 'ц' and event.event_type  == 'up':
            selected_button-=1
            if selected_button < 0:
                selected_button = menu_buttons_len
        elif event.name == 'down' and event.event_type == 'up' or event.name == 's' and event.event_type  == 'up' or event.name == 'ы' and event.event_type  == 'up':
            selected_button+=1
            if selected_button > menu_buttons_len:
                selected_button = 0
        for i, button in enumerate(menu_buttons):
            button_name, button_function = button
            if event.name == 'enter' and event.event_type == 'up' and i == selected_button:
                sound_menu_enter.play()
                button_function()
            if i == selected_button:
                print(f"\033[{(lines//2+i+help_articles_len)};{columns//2-(len(button_name))//2}H>{button_name}<")
            else:
                print(f"\033[{(lines//2+i+help_articles_len)};{columns//2-(len(button_name))//2}H {button_name} ")

def restart_menu_single_player(score):
    os.system('cls' if os_name == 'nt' else 'clear')
    pygame.mixer.init()
    sound_menu_roll = pygame.mixer.Sound('sounds/menu-roll.mp3')
    sound_menu_enter = pygame.mixer.Sound('sounds/menu-enter.mp3')
    menu_buttons = [("Retry", start_game_single_player), ("Main menu", main), ("Exit", sys.exit)]
    menu_buttons_len = len(menu_buttons)-1
    selected_button = 0
    columns, lines = shutil.get_terminal_size(fallback=())
    filename = 'max_score.bin'
    max_score = None
    if not os.path.exists(filename):
        with open(filename, 'wb') as f:
            f.write((0).to_bytes(4, byteorder='big'))
    with open(filename, 'rb') as f:
        max_score = int.from_bytes(f.read(4), byteorder='big')
    if score > max_score:
        with open(filename, 'wb') as f:
            f.write(score.to_bytes(4, byteorder='big'))
        max_score = score
    print_line_len = len(f"|MAX SCORE: {max_score}|")
    print(f"\033[{lines//2-2};{columns//2-print_line_len//2}H|MAX SCORE: {max_score}|")
    print_line_len = len(f"|END WITH SCORE: {score}|")
    print(f"\033[{lines//2-1};{columns//2-print_line_len//2}H|END WITH SCORE: {score}|")
    for i, button in enumerate(menu_buttons):
        button_name, button_function = button
        if i == selected_button:
            print(f"\033[{(lines//2+i)};{columns//2-(len(button_name))//2}H>{button_name}<")
        else:
            print(f"\033[{(lines//2+i)};{columns//2-(len(button_name))//2}H {button_name} ")
    while(True):
        event = keyboard.read_event()
        columns, lines = shutil.get_terminal_size(fallback=())
        if event.name == 'up' and event.event_type == 'up' or event.name == 'w' and event.event_type  == 'up' or event.name == 'ц' and event.event_type  == 'up':
            sound_menu_roll.play()
            selected_button-=1
            if selected_button < 0:
                selected_button = menu_buttons_len
        elif event.name == 'down' and event.event_type == 'up' or event.name == 's' and event.event_type  == 'up' or event.name == 'ы' and event.event_type  == 'up':
            sound_menu_roll.play()
            selected_button+=1
            if selected_button > menu_buttons_len:
                selected_button = 0
        for i, button in enumerate(menu_buttons):
            button_name, button_function = button
            if event.name == 'enter' and event.event_type == 'up' and i == selected_button:
                sound_menu_enter.play()
                button_function()
            if i == selected_button:
                print(f"\033[{(lines//2+i)};{columns//2-(len(button_name))//2}H>{button_name}<")
            else:
                print(f"\033[{(lines//2+i)};{columns//2-(len(button_name))//2}H {button_name} ")

def restart_menu_multi_player(number_of_player):
    os.system('cls' if os_name == 'nt' else 'clear')
    pygame.mixer.init()
    sound_menu_roll = pygame.mixer.Sound('sounds/menu-roll.mp3')
    sound_menu_enter = pygame.mixer.Sound('sounds/menu-enter.mp3')
    menu_buttons = [("Retry", start_game_multi_player), ("Main menu", main), ("Exit", sys.exit)]
    menu_buttons_len = len(menu_buttons)-1
    selected_button = 0
    columns, lines = shutil.get_terminal_size(fallback=())
    print_line_len = len(f"|Player {number_of_player} Win|")
    print(f"\033[{lines//2-1};{columns//2-print_line_len//2}H|Player {number_of_player} Win|")
    for i, button in enumerate(menu_buttons):
        button_name, button_function = button
        if i == selected_button:
            print(f"\033[{(lines//2+i)};{columns//2-(len(button_name))//2}H>{button_name}<")
        else:
            print(f"\033[{(lines//2+i)};{columns//2-(len(button_name))//2}H {button_name} ")
    while(True):
        event = keyboard.read_event()
        columns, lines = shutil.get_terminal_size(fallback=())
        if event.name == 'up' and event.event_type == 'up' or event.name == 'w' and event.event_type  == 'up' or event.name == 'ц' and event.event_type  == 'up':
            sound_menu_roll.play()
            selected_button-=1
            if selected_button < 0:
                selected_button = menu_buttons_len
        elif event.name == 'down' and event.event_type == 'up' or event.name == 's' and event.event_type  == 'up' or event.name == 'ы' and event.event_type  == 'up':
            sound_menu_roll.play()
            selected_button+=1
            if selected_button > menu_buttons_len:
                selected_button = 0
        for i, button in enumerate(menu_buttons):
            button_name, button_function = button
            if event.name == 'enter' and event.event_type == 'up' and i == selected_button:
                sound_menu_enter.play()
                button_function()
            if i == selected_button:
                print(f"\033[{(lines//2+i)};{columns//2-(len(button_name))//2}H>{button_name}<")
            else:
                print(f"\033[{(lines//2+i)};{columns//2-(len(button_name))//2}H {button_name} ")

def start_game_single_player():
    columns, lines = shutil.get_terminal_size(fallback=())
    pygame.mixer.init()
    sound_game_apple = pygame.mixer.Sound('sounds/game-apple.mp3')
    sound_game_fail = pygame.mixer.Sound('sounds/game-fail.mp3')
    sound_game = pygame.mixer.Sound('sounds/game.mp3')
    sound_game.play(-1)
    top_box_side_pos = 0
    bottom_box_side_pos = lines
    left_box_side_pos = int(columns // 2.25 - lines)
    right_bot_side_pos = columns - left_box_side_pos
    min_columns_position = left_box_side_pos + 3
    max_columns_position = right_bot_side_pos - 3
    min_lines_position = top_box_side_pos + 2
    max_lines_position = bottom_box_side_pos - 1

    snake_segments_XY = [(lines//2, columns//2)]

    appleXY = [(random.randint(0, max_lines_position),random.randint(min_columns_position, max_columns_position))]
    apple = "O"

    Xspeed = 1
    Yspeed = 0.5

    score = 0


    last_key_direction = "right"
    last_segment = snake_segments_XY[-1]

    os.system('cls' if os_name == 'nt' else 'clear')

    for i in range(lines+1):
        print(f"\033[{i};{left_box_side_pos}H" + "█",end='')
        print(f"\033[{i};{right_bot_side_pos}H" + "█",end='')
        print(f"\033[{i};{left_box_side_pos-1}H" + "█",end='')
        print(f"\033[{i};{right_bot_side_pos-1}H" + "█",end='')
    for i in range(left_box_side_pos + 1, right_bot_side_pos):
        print(f"\033[{top_box_side_pos};{i}H" + "█", end='')
        print(f"\033[{bottom_box_side_pos};{i}H" + "█", end='')

    while(True):
        if keyboard.is_pressed('up') and last_key_direction != 'down' or keyboard.is_pressed('w') and last_key_direction != 'down' or keyboard.is_pressed('ц') and last_key_direction != 'down':
            last_key_direction = "up"
        elif keyboard.is_pressed('down') and last_key_direction != 'up' or keyboard.is_pressed('s') and last_key_direction != 'up' or keyboard.is_pressed('ы') and last_key_direction != 'up':
            last_key_direction = "down"
        elif keyboard.is_pressed('left') and last_key_direction != 'right' or keyboard.is_pressed('a') and last_key_direction != 'right' or keyboard.is_pressed('ф') and last_key_direction != 'right':
            last_key_direction = "left"
        elif keyboard.is_pressed('right') and last_key_direction != 'left' or keyboard.is_pressed('d') and last_key_direction != 'left' or keyboard.is_pressed('в') and last_key_direction != 'left':
            last_key_direction = "right"
        if (columns, lines) != shutil.get_terminal_size(fallback=()):
            os.system('cls' if os_name == 'nt' else 'clear')
            columns, lines = shutil.get_terminal_size(fallback=())
            left_box_side_pos = int(columns // 2.25 - lines)
            right_bot_side_pos = columns - left_box_side_pos
            bottom_box_side_pos = lines
            min_columns_position = left_box_side_pos + 3
            max_columns_position = right_bot_side_pos - 3
            min_lines_position = top_box_side_pos + 2
            max_lines_position = bottom_box_side_pos - 1
            for i in range (len(snake_segments_XY)):
                snake_segments_XY[i] = (lines//2+i, columns//2+i)
            for i in range(lines+1):
                print(f"\033[{i};{left_box_side_pos}H" + "█",end='')
                print(f"\033[{i};{right_bot_side_pos}H" + "█",end='')
                print(f"\033[{i};{left_box_side_pos-1}H" + "█",end='')
                print(f"\033[{i};{right_bot_side_pos-1}H" + "█",end='')
            for i in range(left_box_side_pos + 1, right_bot_side_pos):
                print(f"\033[{top_box_side_pos};{i}H" + "█", end='')
                print(f"\033[{bottom_box_side_pos};{i}H" + "█", end='')
        if tuple(map(int, snake_segments_XY[0])) == appleXY[0]:
            appleXY = [(random.randint(min_lines_position+2, max_lines_position),random.randint(min_columns_position, max_columns_position))]
            # calculate the position of the new segment
            last_segment = snake_segments_XY[-1]
            new_segment = (last_segment[0], last_segment[1]-1)
            # add the new segment to the snake_segments_XY
            snake_segments_XY.append(new_segment)
            score+=1
            sound_game_apple.play()
        last_segment = snake_segments_XY[-1]
        if last_key_direction == "down":
            if snake_segments_XY[0][0] < max_lines_position:
                for i in range(len(snake_segments_XY)-1, 0, -1):
                    snake_segments_XY[i] = snake_segments_XY[i-1]
                snake_segments_XY[0] = (snake_segments_XY[0][0]+Yspeed, snake_segments_XY[0][1])
            else:
                for i in range(len(snake_segments_XY)-1, 0, -1):
                    snake_segments_XY[i] = snake_segments_XY[i-1]
                snake_segments_XY[0] = (min_lines_position,snake_segments_XY[0][1])
        elif last_key_direction == "up":
            if snake_segments_XY[0][0] > min_lines_position:
                for i in range(len(snake_segments_XY)-1, 0, -1):
                    snake_segments_XY[i] = snake_segments_XY[i-1]
                snake_segments_XY[0] = (snake_segments_XY[0][0]-Yspeed, snake_segments_XY[0][1])
            else:
                for i in range(len(snake_segments_XY)-1, 0, -1):
                    snake_segments_XY[i] = snake_segments_XY[i-1]
                snake_segments_XY[0] = (max_lines_position,snake_segments_XY[0][1])
        elif last_key_direction == "right":
            if snake_segments_XY[0][1] <= max_columns_position:
                for i in range(len(snake_segments_XY)-1, 0, -1):
                    snake_segments_XY[i] = snake_segments_XY[i-1]
                snake_segments_XY[0] = (snake_segments_XY[0][0], snake_segments_XY[0][1]+Xspeed)
            else:
                for i in range(len(snake_segments_XY)-1, 0, -1):
                    snake_segments_XY[i] = snake_segments_XY[i-1]
                snake_segments_XY[0] = (snake_segments_XY[0][0],min_columns_position)
        elif last_key_direction == "left":
            if snake_segments_XY[0][1] >= min_columns_position:
                for i in range(len(snake_segments_XY)-1, 0, -1):
                    snake_segments_XY[i] = snake_segments_XY[i-1]
                snake_segments_XY[0] = (snake_segments_XY[0][0], snake_segments_XY[0][1]-Xspeed)
            else:
                for i in range(len(snake_segments_XY)-1, 0, -1):
                    snake_segments_XY[i] = snake_segments_XY[i-1]
                snake_segments_XY[0] = (snake_segments_XY[0][0],max_columns_position)
        relative_snake_segments_XY = [(int(x), int(y)) for x, y in snake_segments_XY]
        if len(snake_segments_XY) != len(set(snake_segments_XY)):
            sound_game.stop()
            sound_game_fail.play()
            restart_menu_single_player(score)
        score_str = f"Score: {score}"
        print(f"\033[{lines//2};{left_box_side_pos-(len(score_str)+2)}H{score_str}")
        print(f'\033[{int(last_segment[0])};{last_segment[1]}H ', end='')
        for segment in relative_snake_segments_XY:
            print(f'\033[{int(segment[0])};{segment[1]}H■', end='')
        print(f"\033[{appleXY[0][0]};{appleXY[0][1]}H{apple}", end='')
        time.sleep(0.08)

def start_game_multi_player():
    columns, lines = shutil.get_terminal_size(fallback=())
    pygame.mixer.init()
    sound_game_apple = pygame.mixer.Sound('sounds/game-apple.mp3')
    sound_game_fail = pygame.mixer.Sound('sounds/game-fail.mp3')
    sound_game = pygame.mixer.Sound('sounds/game.mp3')
    sound_game.play(-1)
    top_box_side_pos = 0
    bottom_box_side_pos = lines
    left_box_side_pos = int(columns // 2.25 - lines)
    right_bot_side_pos = columns - left_box_side_pos
    min_columns_position = left_box_side_pos + 3
    max_columns_position = right_bot_side_pos - 3
    min_lines_position = top_box_side_pos + 2
    max_lines_position = bottom_box_side_pos - 1

    player1_snake_segments_XY = [(min_lines_position, min_columns_position)]
    player2_snake_segments_XY = [(max_lines_position, max_columns_position)]

    appleXY = [(random.randint(0, max_lines_position),random.randint(min_columns_position, max_columns_position))]
    apple = "O"

    Xspeed = 1
    Yspeed = 0.5

    player1_score = 0
    player2_score = 0


    player1_last_key_direction = "right"
    player2_last_key_direction = "right"
    player1_last_segment = player1_snake_segments_XY[-1]
    player2_last_segment = player2_snake_segments_XY[-1]

    os.system('cls' if os_name == 'nt' else 'clear')

    for i in range(lines+1):
        print(f"\033[{i};{left_box_side_pos}H" + "█",end='')
        print(f"\033[{i};{right_bot_side_pos}H" + "█",end='')
        print(f"\033[{i};{left_box_side_pos-1}H" + "█",end='')
        print(f"\033[{i};{right_bot_side_pos-1}H" + "█",end='')
    for i in range(left_box_side_pos + 1, right_bot_side_pos):
        print(f"\033[{top_box_side_pos};{i}H" + "█", end='')
        print(f"\033[{bottom_box_side_pos};{i}H" + "█", end='')

    while(True):
        if keyboard.is_pressed('w') and player1_last_key_direction != 'down' or keyboard.is_pressed('ц') and player1_last_key_direction != 'down':
            player1_last_key_direction = "up"
        elif keyboard.is_pressed('s') and player1_last_key_direction != 'up' or keyboard.is_pressed('ы') and player1_last_key_direction != 'up':
            player1_last_key_direction = "down"
        elif keyboard.is_pressed('a') and player1_last_key_direction != 'right' or keyboard.is_pressed('ф') and player1_last_key_direction != 'right':
            player1_last_key_direction = "left"
        elif keyboard.is_pressed('d') and player1_last_key_direction != 'left' or keyboard.is_pressed('в') and player1_last_key_direction != 'left':
            player1_last_key_direction = "right"
        
        if keyboard.is_pressed('up') and player2_last_key_direction != 'down':
            player2_last_key_direction = "up"
        elif keyboard.is_pressed('down') and player2_last_key_direction != 'up':
            player2_last_key_direction = "down"
        elif keyboard.is_pressed('left') and player2_last_key_direction != 'right':
            player2_last_key_direction = "left"
        elif keyboard.is_pressed('right') and player2_last_key_direction != 'left':
            player2_last_key_direction = "right"

        if (columns, lines) != shutil.get_terminal_size(fallback=()):
            os.system('cls' if os_name == 'nt' else 'clear')
            columns, lines = shutil.get_terminal_size(fallback=())
            left_box_side_pos = int(columns // 2.25 - lines)
            right_bot_side_pos = columns - left_box_side_pos
            bottom_box_side_pos = lines
            min_columns_position = left_box_side_pos + 3
            max_columns_position = right_bot_side_pos - 3
            min_lines_position = top_box_side_pos + 2
            max_lines_position = bottom_box_side_pos - 1
            for i in range(len(player1_snake_segments_XY)):
                player1_snake_segments_XY[i] = (lines//2+i, columns//2+i)
            for i in range(lines+1):
                print(f"\033[{i};{left_box_side_pos}H" + "█",end='')
                print(f"\033[{i};{right_bot_side_pos}H" + "█",end='')
                print(f"\033[{i};{left_box_side_pos-1}H" + "█",end='')
                print(f"\033[{i};{right_bot_side_pos-1}H" + "█",end='')
            for i in range(left_box_side_pos + 1, right_bot_side_pos):
                print(f"\033[{top_box_side_pos};{i}H" + "█", end='')
                print(f"\033[{bottom_box_side_pos};{i}H" + "█", end='')
        if tuple(map(int, player1_snake_segments_XY[0])) == appleXY[0]:
            appleXY = [(random.randint(min_lines_position+2, max_lines_position),random.randint(min_columns_position, max_columns_position))]
            # calculate the position of the new segment
            player1_last_segment = player1_snake_segments_XY[-1]
            new_segment = (player1_last_segment[0], player1_last_segment[1]-1)
            # add the new segment to the snake_segments_XY
            player1_snake_segments_XY.append(new_segment)
            player1_score+=1
            sound_game_apple.play()
        
        if tuple(map(int, player2_snake_segments_XY[0])) == appleXY[0]:
            appleXY = [(random.randint(min_lines_position+2, max_lines_position),random.randint(min_columns_position, max_columns_position))]
            # calculate the position of the new segment
            player2_last_segment = player2_snake_segments_XY[-1]
            new_segment = (player2_last_segment[0], player2_last_segment[1]-1)
            # add the new segment to the snake_segments_XY
            player2_snake_segments_XY.append(new_segment)
            player2_score+=1
            sound_game_apple.play()

        player1_last_segment = player1_snake_segments_XY[-1]
        player2_last_segment = player2_snake_segments_XY[-1]
        if player1_last_key_direction == "down":
            if player1_snake_segments_XY[0][0] < max_lines_position:
                for i in range(len(player1_snake_segments_XY)-1, 0, -1):
                    player1_snake_segments_XY[i] = player1_snake_segments_XY[i-1]
                player1_snake_segments_XY[0] = (player1_snake_segments_XY[0][0]+Yspeed, player1_snake_segments_XY[0][1])
            else:
                for i in range(len(player1_snake_segments_XY)-1, 0, -1):
                    player1_snake_segments_XY[i] = player1_snake_segments_XY[i-1]
                player1_snake_segments_XY[0] = (min_lines_position,player1_snake_segments_XY[0][1])
        elif player1_last_key_direction == "up":
            if player1_snake_segments_XY[0][0] > min_lines_position:
                for i in range(len(player1_snake_segments_XY)-1, 0, -1):
                    player1_snake_segments_XY[i] = player1_snake_segments_XY[i-1]
                player1_snake_segments_XY[0] = (player1_snake_segments_XY[0][0]-Yspeed, player1_snake_segments_XY[0][1])
            else:
                for i in range(len(player1_snake_segments_XY)-1, 0, -1):
                    player1_snake_segments_XY[i] = player1_snake_segments_XY[i-1]
                player1_snake_segments_XY[0] = (max_lines_position,player1_snake_segments_XY[0][1])
        elif player1_last_key_direction == "right":
            if player1_snake_segments_XY[0][1] <= max_columns_position:
                for i in range(len(player1_snake_segments_XY)-1, 0, -1):
                    player1_snake_segments_XY[i] = player1_snake_segments_XY[i-1]
                player1_snake_segments_XY[0] = (player1_snake_segments_XY[0][0], player1_snake_segments_XY[0][1]+Xspeed)
            else:
                for i in range(len(player1_snake_segments_XY)-1, 0, -1):
                    player1_snake_segments_XY[i] = player1_snake_segments_XY[i-1]
                player1_snake_segments_XY[0] = (player1_snake_segments_XY[0][0],min_columns_position)
        elif player1_last_key_direction == "left":
            if player1_snake_segments_XY[0][1] >= min_columns_position:
                for i in range(len(player1_snake_segments_XY)-1, 0, -1):
                    player1_snake_segments_XY[i] = player1_snake_segments_XY[i-1]
                player1_snake_segments_XY[0] = (player1_snake_segments_XY[0][0], player1_snake_segments_XY[0][1]-Xspeed)
            else:
                for i in range(len(player1_snake_segments_XY)-1, 0, -1):
                    player1_snake_segments_XY[i] = player1_snake_segments_XY[i-1]
                player1_snake_segments_XY[0] = (player1_snake_segments_XY[0][0],max_columns_position)

        if player2_last_key_direction == "down":
            if player2_snake_segments_XY[0][0] < max_lines_position:
                for i in range(len(player2_snake_segments_XY)-1, 0, -1):
                    player2_snake_segments_XY[i] = player2_snake_segments_XY[i-1]
                player2_snake_segments_XY[0] = (player2_snake_segments_XY[0][0]+Yspeed, player2_snake_segments_XY[0][1])
            else:
                for i in range(len(player2_snake_segments_XY)-1, 0, -1):
                    player2_snake_segments_XY[i] = player2_snake_segments_XY[i-1]
                player2_snake_segments_XY[0] = (min_lines_position,player2_snake_segments_XY[0][1])
        elif player2_last_key_direction == "up":
            if player2_snake_segments_XY[0][0] > min_lines_position:
                for i in range(len(player2_snake_segments_XY)-1, 0, -1):
                    player2_snake_segments_XY[i] = player2_snake_segments_XY[i-1]
                player2_snake_segments_XY[0] = (player2_snake_segments_XY[0][0]-Yspeed, player2_snake_segments_XY[0][1])
            else:
                for i in range(len(player2_snake_segments_XY)-1, 0, -1):
                    player2_snake_segments_XY[i] = player2_snake_segments_XY[i-1]
                player2_snake_segments_XY[0] = (max_lines_position,player2_snake_segments_XY[0][1])
        elif player2_last_key_direction == "right":
            if player2_snake_segments_XY[0][1] <= max_columns_position:
                for i in range(len(player2_snake_segments_XY)-1, 0, -1):
                    player2_snake_segments_XY[i] = player2_snake_segments_XY[i-1]
                player2_snake_segments_XY[0] = (player2_snake_segments_XY[0][0], player2_snake_segments_XY[0][1]+Xspeed)
            else:
                for i in range(len(player2_snake_segments_XY)-1, 0, -1):
                    player2_snake_segments_XY[i] = player2_snake_segments_XY[i-1]
                player2_snake_segments_XY[0] = (player2_snake_segments_XY[0][0],min_columns_position)
        elif player2_last_key_direction == "left":
            if player2_snake_segments_XY[0][1] >= min_columns_position:
                for i in range(len(player2_snake_segments_XY)-1, 0, -1):
                    player2_snake_segments_XY[i] = player2_snake_segments_XY[i-1]
                player2_snake_segments_XY[0] = (player2_snake_segments_XY[0][0], player2_snake_segments_XY[0][1]-Xspeed)
            else:
                for i in range(len(player2_snake_segments_XY)-1, 0, -1):
                    player2_snake_segments_XY[i] = player2_snake_segments_XY[i-1]
                player2_snake_segments_XY[0] = (player2_snake_segments_XY[0][0],max_columns_position)
        player1_relative_snake_segments_XY = [(int(x), int(y)) for x, y in player1_snake_segments_XY]
        player2_relative_snake_segments_XY = [(int(x), int(y)) for x, y in player2_snake_segments_XY]

        if len(player1_snake_segments_XY) != len(set(player1_snake_segments_XY)) or player1_snake_segments_XY[0] in player2_snake_segments_XY[1:]:
            sound_game.stop()
            sound_game_fail.play()
            restart_menu_multi_player(2)
        elif len(player2_snake_segments_XY) != len(set(player2_snake_segments_XY)) or player2_snake_segments_XY[0] in player1_snake_segments_XY[1:]:
            sound_game.stop()
            sound_game_fail.play()
            restart_menu_multi_player(1)
        player1_score_str = f"Player 1 score: {player1_score}"
        player2_score_str = f"Player 2 score: {player2_score}"
        print(f"\033[{lines//2};{left_box_side_pos-(len(player1_score_str)+2)}H{player1_score_str}")
        print(f"\033[{lines//2+1};{left_box_side_pos-(len(player2_score_str)+2)}H{player2_score_str}")
        print(f'\033[{int(player1_last_segment[0])};{player1_last_segment[1]}H ', end='')
        print(f'\033[{int(player2_last_segment[0])};{player2_last_segment[1]}H ', end='')
        for segment in player1_relative_snake_segments_XY:
            print(f'\033[{int(segment[0])};{segment[1]}H■', end='')
        for segment in player2_relative_snake_segments_XY:
            print(f'\033[{int(segment[0])};{segment[1]}H■', end='')
        print(f"\033[{appleXY[0][0]};{appleXY[0][1]}H{apple}", end='')
        time.sleep(0.08)

if __name__ == '__main__':
    main()