import pyautogui
import time
import random
from random import randint
from pyautogui import keyDown, keyUp, press


x = 0
x1 = 445
y1 = 505
x2 = 452
y2 = 552
x3 = 900
y3 = 329
timing = time.time()
end_time = time.time() + (60 * 42 )
key1 = 'q'
key2 = 'e'
key3 = 'w'
waiting_time = 160

def queue(korrakx, korraky, joinx, joiny, ax, ay, waiting_time):
    press("i")
    pyautogui.moveTo(korrakx, korraky)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(joinx, joiny)
    pyautogui.click()
    time.sleep(waiting_time)
    pyautogui.moveTo(ax, ay)
    pyautogui.click()
    time.sleep(125)

def movement(a, b, c):
    keyDown(c)
    time.sleep(4)
    keyUp(c)
    time.sleep(1)
    keyDown(b)
    time.sleep(12)
    keyUp(b)
    time.sleep(1)
    press('1')
    time.sleep(10)
    keyDown(c)
    time.sleep(5)
    keyUp(c)
    time.sleep(1)
    keyDown(a)
    time.sleep(2)
    keyUp(a)
    time.sleep(1)
    keyDown(c)
    time.sleep(15)
    keyUp(c)

print('Focus on WoW window')
for i in reversed(range(5)):
    print('Starting in ' + str(i + 1) + ' seconds!')
    time.sleep(1)

while timing < end_time:
    while x == 1:
        time_between_actions = randint(20, 59)
        inner_sleep = random.random()
        actions = randint(1, 6)
        keyDown(key1)
        time.sleep(random.uniform(0.3,0.6))
        keyUp(key1)
        keyDown(key2)
        time.sleep(random.uniform(0.3,0.6))
        keyUp(key2)
        time.sleep(random.uniform(0.3,0.6))
        press("space")
        time.sleep(random.uniform(1,1.4))

    else:
        queue(x1, y1, x2, y2, x3, y3, waiting_time)
        movement(key1, key2, key3)
        x = 1

else:
    x = x - 1
    timing *= 0
