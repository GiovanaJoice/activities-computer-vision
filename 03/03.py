#Lemos as imagens na ordem invertida: BGR (Azul, Verde e Vermelho). 
#O Canal 0 é o Azul, o Canal 1 é o Verde e o Canal 2 é o Vermelho.

import numpy as np
import cv2 as cv

imagem = cv.imread('C:/enviroment/learningOpenCV/03/imgcolorida3.jpg')
b, g, r = cv.split(imagem) 

cv.imshow('Azul', b)
cv.imshow('Verde', g)
cv.imshow('Vermelho', r)

cv.imwrite('C:/enviroment/learningOpenCV/03/filtroazul.jpg', b)
cv.imwrite('C:/enviroment/learningOpenCV/03/filtroverde.jpg', g )
cv.imwrite('C:/enviroment/learningOpenCV/03/filtrovermelho.jpg', r)

cv.waitKey(0)
cv.destroyAllWindows()