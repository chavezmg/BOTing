"""
This scripts types whatever is in 'readme.txt'
"""

import pyautogui as pg
import pyperclip
import time

with open('readme.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
f.close()

time.sleep(5)
for line in lines:
    time.sleep(1)
    pyperclip.copy(line)
    pg.hotkey("ctrl", "v")
    pg.press('enter')
    time.sleep(1)

