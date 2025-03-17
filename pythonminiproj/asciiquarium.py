import curses
import random
import time

# Fish list with different styles
FISH = [
    "><(((('>",
    "><{{{'>",
    "<°)))><",
    "><((('>",
    "><((('>",
    "<'(((('<"
]

def draw_fish(screen, fish_list):
    screen.clear()
    height, width = screen.getmaxyx()
    
    for fish in fish_list:
        y, x, fish_str = fish
        if x < width:
            screen.addstr(y, x, fish_str)
    
    screen.refresh()

def update_fish(fish_list, height, width):
    new_fish_list = []
    for y, x, fish_str in fish_list:
        x += random.choice([-1, 1])  # Move left or right
        if 0 < x < width:
            new_fish_list.append((y, x, fish_str))
    
    if random.random() < 0.2:  # Add new fish sometimes
        new_fish_list.append((random.randint(1, height - 2), 0, random.choice(FISH)))

    return new_fish_list

def aquarium(screen):
    curses.curs_set(0)
    screen.nodelay(True)
    height, width = screen.getmaxyx()
    fish_list = []

    while True:
        fish_list = update_fish(fish_list, height, width)
        draw_fish(screen, fish_list)
        time.sleep(0.2)

        key = screen.getch()
        if key == ord('q'):
            break  # Quit on 'q'

curses.wrapper(aquarium)
