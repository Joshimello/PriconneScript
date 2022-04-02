import pyautogui
import time

def find(img):
	target = img+'.png'
	coord = pyautogui.locateOnScreen(target, confidence=0.8, grayscale=True)
	if coord != None:
		pyautogui.click(pyautogui.center(coord))
		time.sleep(1.5)
	else:
		return 'nothing'

def loop():
	find('new')
	find('new')
	find('load')
	while True:
		menu = pyautogui.locateOnScreen('menu.png', confidence=0.8)
		if menu != None:
			break
	find('menu')
	find('skip')
	find('skipconf')
	while True:
		close = pyautogui.locateOnScreen('close.png', confidence=0.8)
		if close != None:
			break
	find('close')
	find('back')
	loop()
loop()