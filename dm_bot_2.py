import pyautogui
import pyperclip
from time import sleep
from pynput.keyboard import Key, Controller
from keyboard import press

sleep(1)
print(pyautogui.position())

pyautogui.moveTo(2413, 237)

x = 0

while True:
    pyautogui.rightClick()

    pyautogui.moveTo(2351, 300)

    pyautogui.click()

    sleep(1.5)

    pyautogui.moveTo(1626, 1398)

    pyautogui.click()

    pyautogui.write('Testing Smth ignore')

    press('enter')

    pyautogui.moveTo(30,150, duration=1)

    pyautogui.click()

    pyautogui.moveTo(2413, 237)

    pyautogui.scroll(-1000 - x)
    
    x += 40
    
    sleep(1)

'''
pyautogui.moveTo(1626,1398)

pyautogui.click()

keyboard.press(Key.ctrl)
keyboard.press('c')
keyboard.release('c')
keyboard.release(Key.ctrl)
'''
