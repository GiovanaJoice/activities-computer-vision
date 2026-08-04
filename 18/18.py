import cv2 as cv
import numpy as np

imagemOriginal = cv.imread('C:/enviroment/learningOpenCV/18/brotogerischiriri.jpg')
imagemCinza = cv.cvtColor(imagemOriginal, cv.COLOR_BGR2GRAY)

cv.imshow('imagem Cinza', imagemCinza)


imagemLaplaciana = cv.Laplacian(imagemCinza, cv.CV_64F)
cv.imshow('Laplaciana', imagemLaplaciana)

laplacianaAbsoluta = cv.convertScaleAbs(imagemLaplaciana)
#cv.imshow('Laplaciana Absoluta', laplacianaAbsoluta)


laplacianaEqualizada = cv.equalizeHist(laplacianaAbsoluta)
cv.imshow('Laplaciana Equalizada', laplacianaEqualizada)
cv.imwrite('C:/enviroment/learningOpenCV/18/cinza.jpg', imagemCinza)
cv.imwrite('C:/enviroment/learningOpenCV/18/laplacianaEqualizada.jpg', laplacianaEqualizada)


cv.waitKey(0)
cv.destroyAllWindows()