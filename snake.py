import os
import random
import shutil
import sys
import time
import keyboard

os_name = os.name

def main(score = None):
    os.system('cls' if os_name == 'nt' else 'clear')
    menu_buttons = [("Start Game", start_game), ("Quit", sys.exit)]
    menu_buttons_len = len(menu_buttons)-1
    selected_button = 0

    columns, lines = shutil.get_terminal_size(fallback=())

    if score:
        print(f"\033[{lines//2-1};{columns//2}H"+f"|END WITH SCORE: {score}|")
    for i, button in enumerate(menu_buttons):
        button_name, button_function = button
        if i == selected_button:
            print(f"\033[{(lines//2+i)};{columns//2}H>{button_name}")
        else:
            print(f"\033[{(lines//2+i)};{columns//2}H {button_name}")
    print(f"\033[{(lines-1)};{0}H" + "Snake v0.1 (2023)")
    while(True):
        event = keyboard.read_event()
        columns, lines = shutil.get_terminal_size(fallback=())
        if event.name == 'up' and event.event_type == 'up':
            selected_button-=1
            if selected_button < 0:
                selected_button = menu_buttons_len
        elif event.name == 'down' and event.event_type == 'up':
            selected_button+=1
            if selected_button > menu_buttons_len:
                selected_button = 0
        for i, button in enumerate(menu_buttons):
            button_name, button_function = button
            if event.name == 'enter' and event.event_type == 'up' and i == selected_button:
                button_function()
            if i == selected_button:
                print(f"\033[{(lines//2+i)};{columns//2}H>{button_name}")
            else:
                print(f"\033[{(lines//2+i)};{columns//2}H {button_name}")

def restart_menu(score):
    os.system('cls' if os_name == 'nt' else 'clear')
    menu_buttons = [("Retry", start_game), ("Main menu", main), ("Exit", sys.exit)]
    menu_buttons_len = len(menu_buttons)-1
    selected_button = 0
    columns, lines = shutil.get_terminal_size(fallback=())
    if score:
        print(f"\033[{lines//2-1};{columns//2}H|END WITH SCORE: {score}|")
    for i, button in enumerate(menu_buttons):
        button_name, button_function = button
        if i == selected_button:
            print(f"\033[{(lines//2+i)};{columns//2}H>{button_name}")
        else:
            print(f"\033[{(lines//2+i)};{columns//2}H {button_name}")
    while(True):
        event = keyboard.read_event()
        columns, lines = shutil.get_terminal_size(fallback=())
        if event.name == 'up' and event.event_type == 'up':
            selected_button-=1
            if selected_button < 0:
                selected_button = menu_buttons_len
        elif event.name == 'down' and event.event_type == 'up':
            selected_button+=1
            if selected_button > menu_buttons_len:
                selected_button = 0
        for i, button in enumerate(menu_buttons):
            button_name, button_function = button
            if event.name == 'enter' and event.event_type == 'up' and i == selected_button:
                button_function()
            if i == selected_button:
                print(f"\033[{(lines//2+i)};{columns//2}H>{button_name}")
            else:
                print(f"\033[{(lines//2+i)};{columns//2}H {button_name}")

def start_game():
    columns, lines = shutil.get_terminal_size(fallback=())

    
    left_box_side_pos = 11
    right_bot_side_pos = columns - 11
    min_columns_position = left_box_side_pos + 1
    max_columns_position = right_bot_side_pos - 1

    snake_segments_XY = [(lines//2, columns//2)]

    appleXY = [(random.randint(0, lines),random.randint(0, columns))]
    apple = "X"

    Xspeed = 1
    Yspeed = 0.6

    score = 0


    last_key_pressed = "right"
    last_segment = snake_segments_XY[-1]

    os.system('cls' if os_name == 'nt' else 'clear')
    while(True):
        if keyboard.is_pressed('up') and last_key_pressed != 'down':
            last_key_pressed = "up"
        elif keyboard.is_pressed('down') and last_key_pressed != 'up':
            last_key_pressed = "down"
        elif keyboard.is_pressed('left') and last_key_pressed != 'right':
            last_key_pressed = "left"
        elif keyboard.is_pressed('right') and last_key_pressed != 'left':
            last_key_pressed = "right"
        if (columns, lines) != shutil.get_terminal_size(fallback=()):
            columns, lines = shutil.get_terminal_size(fallback=())
            left_box_side_pos = 11
            right_bot_side_pos = columns - 11
            min_columns_position = left_box_side_pos + 1
            max_columns_position = right_bot_side_pos - 1
        if tuple(map(int, snake_segments_XY[0])) == appleXY[0]:
            appleXY = [(random.randint(0, lines),random.randint(min_columns_position, max_columns_position))]
            # calculate the position of the new segment
            last_segment = snake_segments_XY[-1]
            new_segment = (last_segment[0], last_segment[1]-1)
            # add the new segment to the snake_segments_XY
            snake_segments_XY.append(new_segment)
            score+=1
        last_segment = snake_segments_XY[-1]
        if last_key_pressed == "down":
            if snake_segments_XY[0][0] < lines:
                for i in range(len(snake_segments_XY)-1, 0, -1):
                    snake_segments_XY[i] = snake_segments_XY[i-1]
                snake_segments_XY[0] = (snake_segments_XY[0][0]+Yspeed, snake_segments_XY[0][1])
            else:
                for i in range(len(snake_segments_XY)-1, 0, -1):
                    snake_segments_XY[i] = snake_segments_XY[i-1]
                snake_segments_XY[0] = (0,snake_segments_XY[0][1])
        if last_key_pressed == "up":
            if snake_segments_XY[0][0] > 0:
                for i in range(len(snake_segments_XY)-1, 0, -1):
                    snake_segments_XY[i] = snake_segments_XY[i-1]
                snake_segments_XY[0] = (snake_segments_XY[0][0]-Yspeed, snake_segments_XY[0][1])
            else:
                for i in range(len(snake_segments_XY)-1, 0, -1):
                    snake_segments_XY[i] = snake_segments_XY[i-1]
                snake_segments_XY[0] = (lines,snake_segments_XY[0][1])
        if last_key_pressed == "right":
            if snake_segments_XY[0][1] <= max_columns_position:
                for i in range(len(snake_segments_XY)-1, 0, -1):
                    snake_segments_XY[i] = snake_segments_XY[i-1]
                snake_segments_XY[0] = (snake_segments_XY[0][0], snake_segments_XY[0][1]+1)
            else:
                for i in range(len(snake_segments_XY)-1, 0, -1):
                    snake_segments_XY[i] = snake_segments_XY[i-1]
                snake_segments_XY[0] = (snake_segments_XY[0][0],min_columns_position)
        if last_key_pressed == "left":
            if snake_segments_XY[0][1] >= min_columns_position:
                for i in range(len(snake_segments_XY)-1, 0, -1):
                    snake_segments_XY[i] = snake_segments_XY[i-1]
                snake_segments_XY[0] = (snake_segments_XY[0][0], snake_segments_XY[0][1]-1)
            else:
                for i in range(len(snake_segments_XY)-1, 0, -1):
                    snake_segments_XY[i] = snake_segments_XY[i-1]
                snake_segments_XY[0] = (snake_segments_XY[0][0],max_columns_position)
        relative_snake_segments_XY = [(int(x), int(y)) for x, y in snake_segments_XY]
        if len(snake_segments_XY) != len(set(snake_segments_XY)):
            restart_menu(score)
        for i in range(lines):
            print(f"\033[{i};{left_box_side_pos}H" + "|")
            print(f"\033[{i};{right_bot_side_pos}H" + "|")
        print(f"\033[{lines//2};{0}H|Score: {score}|")
        print(f'\033[{int(last_segment[0])};{last_segment[1]}H ', end='')
        for segment in relative_snake_segments_XY:
            print(f'\033[{int(segment[0])};{segment[1]}H■', end='')
        print(f"\033[{appleXY[0][0]};{appleXY[0][1]}H{apple}", end='')
        time.sleep(0.05)

if __name__ == '__main__':
    main()