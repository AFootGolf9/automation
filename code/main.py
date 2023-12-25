import tkinter
import pyautogui as gui
import setup
import time

while not gui.pixelMatchesColor(35, 156, (255, 255, 255)):
    time.sleep(1)

found = False

while not found:
    gui.scroll(-10)
    img = gui.screenshot()
    for i in range(0, 1080, 10):
        color = img.getpixel((500, i))
        if color == (0, 120, 242, 255):
            found = True
            break



#while not gui.pixelMatchesColor(500, 1000, (0, 120, 242)):
#    gui.scroll(-1)
#    time.sleep(1)
