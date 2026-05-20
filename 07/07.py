import cv2 as cv
import numpy as np

imagemCinza = cv.imread('C:/enviroment/learningOpenCV/07/onepieceColorido07.jpg', 0)
cv.imshow('Cinza', imagemCinza)

imagemcomLimiar = cv.threshold(imagemCinza, 110, 190, cv.THRESH_BINARY)[1] 
cv.imshow('Limiar', imagemcomLimiar)

cv.imwrite('C:/enviroment/learningOpenCV/07/onepieceCinza.jpg', imagemCinza)
cv.imwrite('C:/enviroment/learningOpenCV/07/onepiececomLimiar.jpg', imagemcomLimiar)

cv.waitKey(0)
cv.destroyAllWindows()  