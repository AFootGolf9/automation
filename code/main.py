import tkinter
import pyautogui as gui
import setup
import time
import threading as thr

t1=thr.Thread(setup.setup())
t1.start()
t1.join()

time.sleep(10)

print(gui.locateCenterOnScreen('./img/epicLogo.png'))
