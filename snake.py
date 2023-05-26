import os
import random
import shutil
import sys
import time
import keyboard

os_name = os.name
#check
def main(score = None):
    os.system('cls' if os_name == 'nt' else 'clear')
    menu_buttons = [("Почати гру", start_game), ("Вихід", sys.exit)]
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

def restart_menu(score):
    os.system('cls' if os_name == 'nt' else 'clear')
    menu_buttons = [("Заново", start_game), 
                    ("Головне меню", main), ("Вихід", sys.exit)]
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
    snake = [(0, 0)]


    appleXY = [(0,0)]
    apple = "X"

    Xspeed = 1
    Yspeed = 0.5

    score = 0

    last_key_pressed = "right"
    os.system('cls' if os_name == 'nt' else 'clear')
    last_segment = snake[-1]
    while(True):
        if keyboard.is_pressed('up') and last_key_pressed != 'down':
            last_key_pressed = "up"
        elif keyboard.is_pressed('down') and last_key_pressed != 'up':
            last_key_pressed = "down"
        elif keyboard.is_pressed('left') and last_key_pressed != 'right':
            last_key_pressed = "left"
        elif keyboard.is_pressed('right') and last_key_pressed != 'left':
            last_key_pressed = "right"
        columns, lines = shutil.get_terminal_size(fallback=())
        aspect_ratio = lines/columns
        if snake[0] == appleXY[0]:
            appleXY = [(random.randint(0, lines),random.randint(0, columns))]
            # calculate the position of the new segment
            last_segment = snake[-1]
            new_segment = (last_segment[0], last_segment[1]-1)
            # add the new segment to the snake
            snake.append(new_segment)
            score+=1
        last_segment = snake[-1]
        if last_key_pressed == "down":
            if snake[0][0] < lines:
                for i in range(len(snake)-1, 0, -1):
                    snake[i] = snake[i-1]
                snake[0] = (snake[0][0]+Yspeed, snake[0][1])
            else:
                for i in range(len(snake)-1, 0, -
                               1):
                    snake[i] = snake[i-1]
                snake[0] = (0,snake[0][1])
        if last_key_pressed == "up":
            if snake[0][0] > 0:
                for i in range(len(snake)-1, 0, -1):
                    snake[i] = snake[i-1]
                snake[0] = (snake[0][0]-Yspeed, snake[0][1])
            else:
                for i in range(len(snake)-1, 0, -1):
                    snake[i] = snake[i-1]
                snake[0] = (lines,snake[0][1])
        if last_key_pressed == "right":
            if snake[0][1] <= columns:
                for i in range(len(snake)-1, 0, -1):
                    snake[i] = snake[i-1]
                snake[0] = (snake[0][0], snake[0][1]+1)
            else:
                for i in range(len(snake)-1, 0, -1):
                    snake[i] = snake[i-1]
                snake[0] = (snake[0][0],0)
        if last_key_pressed == "left":
            if snake[0][1] >= 0:
                for i in range(len(snake)-1, 0, -1):
                    snake[i] = snake[i-1]
                snake[0] = (snake[0][0], snake[0][1]-1)
            else:
                for i in range(len(snake)-1, 0, -1):
                    snake[i] = snake[i-1]
                snake[0] = (snake[0][0],columns)
        if len(snake) != len(set(snake)):
            restart_menu(score)
        print(f"\033[{0};{0}H|Score: {score}|")
        print(f'\033[{int(last_segment[0])};{last_segment[1]}H ', end='')
        for segment in snake:
            print(f'\033[{int(segment[0])};{segment[1]}H■', end='')
        print(f"\033[{appleXY[0][0]};{appleXY[0][1]}H{apple}", end='')
        time.sleep(0.05)

if __name__ == '__main__':
    main()