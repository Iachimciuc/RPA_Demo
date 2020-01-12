from pyautogui import position
from time import sleep

delay = None
to_clipboard = False

if delay:
    sleep(delay)

coord = position()

if to_clipboard:
    set_to_clipboard("x=" + str(coord[0]) + ", y=" + str(coord[1]))

print(coord[0])
print(coord[1])
