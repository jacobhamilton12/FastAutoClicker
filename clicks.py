import sys

def clicks(delay, numClicks, ticRate):
    import pyautogui
    import keyboard
    import time
    press = False
    numClicks = int(numClicks)
    delay = float(delay)
    ticRate = float(ticRate)
    while True:
        try:
            while press:
                pyautogui.click(clicks=numClicks)
                time.sleep(delay)
                if keyboard.is_pressed('alt'):
                    press = False
                    while keyboard.is_pressed('alt'):
                        time.sleep(ticRate)
            while keyboard.is_pressed('alt'):
                time.sleep(ticRate)
                press = True
        except Exception:
            pass
        time.sleep(ticRate)
    return 0
try:
    clicks(sys.argv[1], sys.argv[2], sys.argv[3])
except:
    print("Error: Num arguments \nUsage: clicks.py [delay] [numClicks] [ticRate]")
    
    

