import pyautogui,time,keyboard
word="Hello"

def typeHello():
        pyautogui.typewrite(word)
        pyautogui.press("enter")
        time.sleep(1)

time.sleep(5)
while 1:
    if keyboard.is_pressed("q"):
        exit(0)
    typeHello()