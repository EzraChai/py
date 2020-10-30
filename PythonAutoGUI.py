import pyautogui,time,keyboard
word="Hello"

print("Auto Typing Hello System is starting in ")

for x in range (1,6):
    print(x)
    time.sleep(1)

print("\nPress backspace for 1 second to stop the System.")

def typeHello():
        pyautogui.typewrite(word)
        pyautogui.press("enter")
        time.sleep(1)

while 1:
    if keyboard.is_pressed("backspace"):
        exit(0)
    typeHello()