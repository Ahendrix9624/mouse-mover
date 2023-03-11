"""
USAGE - The code uses the PyAutoGUI library to move the mouse cursor randomly between 
        the coordinates (600,200) and (700,600) with a duration of 0.5 seconds. 
        It continues this action indefinitely using a while loop with a sleep time 
        of 2 seconds between each mouse movement.
        
AUTHOR - https://github.com/Ahendrix9624/
"""
import pyautogui as pag
import random
import time

while True:
    x = random.randint(600, 700)
    y = random.randint(200, 600)
    pag.moveTo(x,y,0.5)
    time.sleep(2)
