import cv2 as cv
import numpy as np

img=cv.imread('squrril.jpg')
cv.imshow("squrril",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow("Laplacian",lap)

#soble1

soblex=cv.Sobel(gray,cv.CV_64F,1,0)
sobley=cv.Sobel(gray,cv.CV_64F,0,1)
combined_soble=cv.bitwise_or(soblex,sobley)

cv.imshow('Soble X',soblex)
cv.imshow('Soble Y',sobley)
cv.imshow('soble combined',combined_soble)
cv.waitKey(0)