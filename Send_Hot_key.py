import platform

first_key = None
second_key = None
third_key = None

# Check if system is not running Windows
if first_key == 'win' or second_key == 'win' or third_key == 'win':
    force_pyautogui = True
if platform.system() != "Windows" or force_pyautogui:
    from pyautogui import hotkey
    hotkey('alt','tab')
