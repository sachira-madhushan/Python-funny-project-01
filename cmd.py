import keyboard
import time
import os
curserColumn=2
curserRaw=2

def pattern():
	print("w:up s:down a:left d:right")
	for i in range(5):
		for a in range(5):
			if a==curserColumn and i==curserRaw:
				print(" - ",end="")
			else:
				print(" * ",end="")
		print()

os.system("cls")
pattern()
while(True):
	if keyboard.is_pressed('w'):
		print("w pressed")
		curserRaw-=1
		time.sleep(1)
		os.system("cls")
		pattern()
	elif keyboard.is_pressed('a'):
		print("a pressed")
		curserColumn-=1
		time.sleep(1)
		os.system("cls")
		pattern()
	elif keyboard.is_pressed('s'):
		print("s pressed")
		curserRaw+=1
		time.sleep(1)
		os.system("cls")
		pattern()
	elif keyboard.is_pressed('d'):
		print("d pressed")
		curserColumn+=1
		time.sleep(1)
		os.system("cls")
		pattern()

	elif keyboard.is_pressed('x'):
		print("bye bye.........")
		time.sleep(1)
		break
