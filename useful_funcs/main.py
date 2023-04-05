"""
Useful functions for botting writen by me
"""

import pyautogui as pg
import time
from os.path import abspath, dirname

screen_size = pg.size()
file_directory = dirname(abspath(__file__))

def mclick(x,y, d=0):
    """This function makes 'd' clicks on 'x' and 'y' positions on the screen """
    pg.moveTo(x,y,0.2)
    time.sleep(0.5)
    if d == 0:
        pg.click()
    if d == 1:
        pg.doubleClick()
    if d >= 2:
        for c in range(d):
            pg.click()
    time.sleep(0.5)

def checker(name, check=0):
    """This function locates on screen a similar image 'name' on root folder"""
    confianza = 0.5
    if check == 0:
        try:
            l,t,w,h = pg.locateOnScreen(file_directory + "\\" + name, confidence = confianza)
            time.sleep(1)
            return l,t,w,h
        except:
            print(name + " no encontrado")
            l,t,w,h = -1,-1,-1,-1
            return l,t,w,h    #failure

def wrapper(name):
    """This function sets up the route of the directory and the image 'name'"""
    return file_directory + "\\" + name

def looker(name):
    """This function looks for 'name' on windows search box"""
    pg.press("winleft")
    time.sleep(1)
    pg.typewrite(name, 0.02)
    pg.press('enter')
    time.sleep(1)

def maximizer(title):
    """This function maximizes window with title 'title'"""
    time.sleep(1)
    pg.getWindowsWithTitle(title)[0].maximize()
    time.sleep(1)

def writer(text):
    """This function writes 'text'"""
    time.sleep(1)
    pg.typewrite(text, 0.02)
    time.sleep(1)

def checker(name, check=0):
    """This function locates on screen a similar image 'name' on root folder"""
    confianza = 0.5
    if check == 0:
        try:
            l,t,w,h = pg.locateOnScreen(file_directory + "\\" + name, confidence = confianza)
            time.sleep(1)
            return l,t,w,h
        except:
            print(name + " no encontrado")
            l,t,w,h = -1,-1,-1,-1
            return l,t,w,h    #failure