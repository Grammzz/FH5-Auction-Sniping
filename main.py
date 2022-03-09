import pyautogui
import time

#pyautogui.mouseInfo()
time.sleep(9)

i = 0;
while i == 0:
    pyautogui.press('enter')
    time.sleep(.3)
    pyautogui.press('enter')
    time.sleep(1.1)
    if pyautogui.pixelMatchesColor(110, 286, (255, 0, 126), tolerance=10):
        pyautogui.press('y')
        time.sleep(.25)
        pyautogui.press('s')
        time.sleep(.25)
        pyautogui.press('enter')
        time.sleep(.3)
        pyautogui.press('enter')
        time.sleep(7)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(.5)
        pyautogui.press('esc')
        time.sleep(1)
    else:
        pyautogui.press('esc')
        time.sleep(.85)

