# این برنامه یک ربات ساده چت است که برای چت کردن باید برنامه ای که میخواهید در آن چت کنبد را باز کنید
# سپس باید مختصات محلی که تایپ میکنید را به آن بدهید تا تایپ کند

import pyautogui
from time import sleep
from random import choice

lst= ["hello!", "hi", "i am robot", "reza"]
for i in range(4):
    sleep(1)
    pyautogui.click(410, 986) #در این مختصات کلیک میکنه 
    pyautogui.write(choice(lst), interval=0.1)
    pyautogui.hotkey('shift', 'enter')

pyautogui.press("enter")
