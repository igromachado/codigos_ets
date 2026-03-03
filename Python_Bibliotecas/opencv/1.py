import cv2
import numpy as np
import random

def funcao(event, x, y, flags, param):
	global a,b,c
	if event == cv2.EVENT_LBUTTONDOWN:
		a = random.randint(0,255)
		b = random.randint(0,255)
		c = random.randint(0,255)
a = 0
b = 0
c = 0

cv2.namedWindow('janela')
cv2.setMouseCallback('janela', funcao)
while(True):
	img = np.full((512,512,3), (a,b,c), np.uint8)
	cv2.imshow('janela', img)
	if cv2.waitKey(10) & 0xFF == 27:
		break
cv2.destroyAllWindows()