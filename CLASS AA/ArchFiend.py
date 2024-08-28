import time
import random
from time import sleep
from random import randint
from tkinter import N
import pyautogui
import pydirectinput

while True:
    pyautogui.press('4')
    sleep(1.3)
    for x in range(5):
        pyautogui.press('3')
        sleep(1)
        pyautogui.press('2')    
        sleep(1.3)