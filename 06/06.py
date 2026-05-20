import cv2 as cv
import numpy as np



imagemColorida = cv.imread('C:/enviroment/learningOpenCV/06/gatoLaranja06.jpg', 0)
cv.imshow('Colorida', imagemColorida)

imagemComPassAlta = cv.Canny(imagemColorida, 10, 200)
cv.imshow('Canny', imagemComPassAlta)


cv.imwrite('C:/enviroment/learningOpenCV/06/gatoLaranjaCinza.jpg', imagemColorida)
cv.imwrite('C:/enviroment/learningOpenCV/06/gatoLaranjaCanny.jpg', imagemComPassAlta)


cv.waitKey(0)
cv.destroyAllWindows()