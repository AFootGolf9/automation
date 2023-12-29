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

time.sleep(3)
for i in range(600, 800):
    gui.click(i, 1000)
time.sleep(3)
gui.click(1500, 840)
time.sleep(5)
gui.click(1400, 1000)
time.sleep(5)
gui.click(1900, 55)