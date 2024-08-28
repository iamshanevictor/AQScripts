import time
import random
from time import sleep
from random import randint
from tkinter import N
import pyautogui
import pydirectinput

while True:
    for x in range(10):
        
        if x == 5:
            pyautogui.click(242,777) #ChatBox
            sleep(1)
            pyautogui.click(355,846) #BlackBars
            sleep(1)

        for x in range(1):
            pyautogui.press('4')
            sleep(1)                        
            pydirectinput.press('2')
            sleep(1)
            pydirectinput.press('3')
            sleep(1)
            pydirectinput.press('5')
            sleep(1.2)
            pydirectinput.press('2')
            sleep(1)
            pydirectinput.press('3')
            sleep(1.2)

        
        for x in range(1):
            if x == 0: #first row
                pyautogui.click(185,401)    #3rdRow (116,443) #1stRow (185,401) #2ndRow(115,423)
                sleep(1.3)
            elif x == 1: #Second Row
                pyautogui.click(115,423)    #3rdRow (116,443) #1stRow (185,401) #2ndRow(115,423)
                sleep(1.3)
            elif x == 2:
                pyautogui.click(116,443)    #3rdRow (116,443) #1stRow (185,401) #2ndRow(115,423)
                sleep(1.3)

            pyautogui.click(183,697) #TurnInButton
            pyautogui.click(clicks=3, interval=0.25)
            sleep(1)
            pyautogui.click(85, 697) #DeclineButton
            sleep(1)