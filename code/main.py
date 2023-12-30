# Script to get free epic games

import tkinter
import pyautogui as gui
import setup
import time

while not gui.pixelMatchesColor(35, 156, (255, 255, 255)):
    time.sleep(1)

found = False
where = None
while not found:
    gui.scroll(-10)
    img = gui.screenshot()
    for i in range(0, 1080, 10):
        color = img.getpixel((500, i))
        where = i
        if color == (0, 120, 242, 255):
            found = True
            break

gui.moveTo(500, where-50)
gui.click()

time.sleep(5)
gui.click(950, 690)
time.sleep(3)
for i in range(650, 900, 5):
    gui.click(1400, i)
    time.sleep(0.1)
time.sleep(5)
gui.click(1400, 1000)
time.sleep(10)
gui.click(1900, 55)