# To draw spiral in ms-paint with python
import pyautogui, time
time.sleep(5)
pyautogui.click()
distance = 400 #total distance
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2) # move in right direction
    distance -=50
    pyautogui.dragRel(0, distance, duration=0.2) # move in down direction
    pyautogui.dragRel(-distance, 0, duration=0.2) # move in left direction
    distance -= 50
    pyautogui.dragRel(0, -distance, duration=0.2) # move in up direction
