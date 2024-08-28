import pygetwindow as gw
import pyautogui

# Find the window
window = gw.getWindowsWithTitle('Facebook')[1]

# Bring the window to the foreground
window.activate()

# Now use pyautogui or pydirectinput to send inputs
pyautogui.click(100, 200)