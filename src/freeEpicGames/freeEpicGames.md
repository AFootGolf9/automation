# Free Epic Games

This script is used to automate the process of getting free games from the Epic Games Store.

# Dependencies

- tkinter: A Python binding to the Tk GUI toolkit.
- pyautogui: A Python module for programmatically controlling the mouse and keyboard.
- time: A Python module for time-related functions.

# How it works

1. The script first waits until the pixel at the coordinates (35, 156) matches the color white (255, 255, 255).

2. It then scrolls upwards until it finds a pixel with the color (0, 120, 242, 255) on the line x=500. This color is used to identify a specific element on the screen.

3. Once the element is found, the script moves the mouse to the position (500, y), where y is the position of the found pixel minus 50, and performs a click.

4. The script then waits for 5 seconds and clicks at the position (950, 690).

5. t waits for another 3 seconds and then performs a series of clicks from the y-coordinate 650 to 900 at the x-coordinate 1400, with a 0.1 second delay between each click.

6. After waiting for 5 more seconds, it clicks at the position (1400, 1000).

7. It waits for 10 more seconds and finally clicks at the position (1900, 55).

Please note that the specific coordinates and colors used in this script are likely tailored to a specific screen resolution and website layout. If you are trying to use or adapt this script, you may need to adjust these values to match your own setup.