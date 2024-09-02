import pyautogui
import time
pos = pyautogui.position()

while True:
    x, y = pyautogui.position()
    print(x,y)
    time.sleep(1)