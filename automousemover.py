#script moves mouse to each of the 4 corners of the screen, taking 2 seconds to complete movement. Pause for 5 seconds
import pyautogui

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 2

screenWidth, screenHeight = pyautogui.size()

def loopOfMyCount(count):
	while count >= 0:
		pyautogui.moveRel(None, 100, duration=1) #move down 100
		pyautogui.moveRel(-100, None, duration=1) #move left 100
		pyautogui.moveRel(None, -100, duration=1) #move up 100
		pyautogui.moveRel(100, None, duration=1) #move right 100
		pyautogui.moveRel(None, 100, duration=1) #move down 100
		count = count - 1
loopOfMyCount(5)