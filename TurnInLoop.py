import time
import random
from time import sleep
from random import randint
from tkinter import N
import pyautogui
import pydirectinput

run = 0

while True:

    run+=1
    print("Counter:",run)

    for FirstRow in range(1): #8x
        for x in range(1): #150x
            pyautogui.press('4')
            sleep(1.3)
            print(x)
            for y in range(5):
                pyautogui.press('3')
                sleep(1)
                pyautogui.press('2')
                sleep(1.3)
            
            if x % 20 == 0:
                pyautogui.click(931,732) #NextRoom
                sleep(3)
                pyautogui.press('l')
                sleep(2)

                for BLM in range(5):
                    pyautogui.click(242,777) #ChatBox
                    sleep(1)
                    pyautogui.click(116,443)    #3rdRow (116,443) #1stRow (185,401) #2ndRow(115,423)
                    sleep(1.5)
                    pyautogui.click(183,697) #TurnInButton
                    pyautogui.click(clicks=5, interval=0.25)
                    sleep(2.5)
                    pyautogui.click(85, 697) #DeclineButton
                    sleep(2)
                    print("BLM:",BLM)

                pyautogui.press('l')
                sleep(1.5)
                pyautogui.click(238,324) #NextRoom
                sleep(1.5)
            
        pyautogui.click(931,732) #NextRoom
        sleep(3)
        pyautogui.press('l')
        sleep(2) 

        for TurnIn1 in range(38): #38x
            if TurnIn1 == 2:
                pyautogui.click(242,777) #ChatBox
                sleep(1)
            elif TurnIn1 % 5 == 0:
                pyautogui.click(242,777) #ChatBox
                sleep(1)
                pyautogui.click(355,846) #BlackBars
                pyautogui.press('l')
                sleep(2)
                pyautogui.press('l')
                sleep(1.5)

            pyautogui.click(185,401)    #3rdRow (116,443) #1stRow (185,401) #2ndRow(115,423)
            sleep(1.5)
            pyautogui.click(183,697) #TurnInButton
            pyautogui.click(clicks=5, interval=0.25)
            sleep(2.5)
            pyautogui.click(85, 697) #DeclineButton
            sleep(2)
            print("Turn in 1st Row:",TurnIn1)
        pyautogui.press('l')
        sleep(2)
        pyautogui.click(238,324) #NextRoom
        sleep(2)

    for SecondRow in range(1):
        for x in range(1):
            pyautogui.press('4')
            sleep(1.3)
            for y in range(5):
                pyautogui.press('3')
                sleep(1)
                pyautogui.press('2')
                sleep(1.3) 
        pyautogui.click(931,732) #NextRoom
        sleep(3)
        pyautogui.press('l')
        sleep(2)    

        for TurnIn2 in range(120): #120x
            if TurnIn2 == 2:
                pyautogui.click(242,777) #ChatBox
                sleep(1.5)
            elif TurnIn2 % 5 == 0:
                pyautogui.click(355,846) #BlackBars
                sleep(1)
                pyautogui.press('l')
                sleep(2)
                pyautogui.press('l')
                sleep(1.5)

            pyautogui.click(115,423) #3rdRow (116,443) #1stRow (185,401) #2ndRow(115,423)
            sleep(1.5)
            pyautogui.click(183,697) #TurnInButton
            pyautogui.click(clicks=5, interval=0.25)
            sleep(2.5)
            pyautogui.click(85, 697) #DeclineButton
            sleep(1.5)
            print("Turn in 2nd Row",TurnIn2)

        pyautogui.press('l')
        sleep(1.5)
        pyautogui.click(238,324) #NextRoom
        sleep(1.5)