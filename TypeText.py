import platform
text = ' SoliDeoGlory and follow white rabbit'
interval_seconds = 0.01

# Set keyboard layout for Windows platform
if platform.system() != "Windows":
    from pyautogui import typewrite
    typewrite(text, interval=interval_seconds)

import win32com.client
shell = win32com.client.Dispatch("WScript.Shell")
import time
for character in text:
    shell.SendKeys(easy_key_translation(character), 0)
    time.sleep(interval_seconds)
