import tkinter
import pyautogui as gui
import setup
import time

while not gui.pixelMatchesColor(35, 156, (255, 255, 255)):
    time.sleep(1)

while not gui.pixelMatchesColor(500, 1000, (0, 120, 242)):
    gui.scroll(-1)
    time.sleep(1)
