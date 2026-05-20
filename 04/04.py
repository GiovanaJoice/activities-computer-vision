import numpy as np
import cv2 as cv

imagemAntes = cv.imread('C:/enviroment/learningOpenCV/04/imgcolorida4.jpg')

imagemDepois = cv.cvtColor(imagemAntes, cv.COLOR_BGR2HSV) 

h, s, v = cv.split(imagemDepois)

cv.imshow('H', h)
cv.imshow('S', s)
cv.imshow('V', v)

cv.imwrite('C:/enviroment/learningOpenCV/04/filtroH.jpg', h)
cv.imwrite('C:/enviroment/learningOpenCV/04/filtroS.jpg', s)
cv.imwrite('C:/enviroment/learningOpenCV/04/filtroV.jpg', v)

cv.waitKey(0)

cv.destroyAllWindows()  
