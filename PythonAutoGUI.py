import pyperclip,pyautogui,time,keyboard

word=" ♥我爱你♥ "

print("Auto Typing [heart]I love you[heart] System is starting in ")

for x in range (1,6):
    print(x)
    time.sleep(1)

def typeHello():
    i = 0
    while i < 521:
        pyautogui.typewrite(str(i))
        pyperclip.copy(word)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('shift', 'enter')
        i += 1
        time.sleep(0.01)


typeHello()