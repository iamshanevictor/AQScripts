import time
import random
from time import sleep
from random import randint
from tkinter import N
import pyautogui
import pydirectinput


import pyautogui
import pydirectinput
from time import sleep

def run_key_presses():
    for _ in range(10):
        pyautogui.press('3')      
        sleep(1.5)                        
        pydirectinput.press('5')
        sleep(1.5)
        pydirectinput.press('2')
        sleep(1.5)
        pydirectinput.press('4')
        sleep(1.5)
        pydirectinput.press('1')
        sleep(1.5)

def run_mouse_clicks():
    pyautogui.click(1500, 721)
    sleep(2)33
    pyautogui.click(1500, 410)
    sleep(2)

def main():
    while True:
        run_key_presses()
        run_mouse_clicks()

if __name__ == "__main__":
    main()


'''
while True: #ShadowScytheGen
    pyautogui.press('2')      
    sleep(1.5)                        
    pydirectinput.press('3')
    sleep(1.5)
    pydirectinput.press('4')3
    sleep(1.5)
    pydirectinput.press('5') '''