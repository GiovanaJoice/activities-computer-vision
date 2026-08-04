import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

imagemOriginal = cv.imread('C:/enviroment/learningOpenCV/19/passarosdonordeste.jpg')
imagemCinza = cv.cvtColor(imagemOriginal, cv.COLOR_BGR2GRAY)

imagemSobelX = cv.Sobel(imagemCinza, cv.CV_64F, 1, 0, ksize=5)
imagemSobelY = cv.Sobel(imagemCinza, cv.CV_64F, 0, 1, ksize=5)

xAbsoluta = cv.convertScaleAbs(imagemSobelX)
yAbsoluta = cv.convertScaleAbs(imagemSobelY)

imagemSobel = cv.addWeighted(xAbsoluta, 0.5, yAbsoluta, 0.5, 0) #juntando os dois eixos
#imagemLaplaciana = cv.Laplacian(imagemCinza, cv.CV_32F)
#imagemLaplaciana = cv.convertScaleAbs(imagemLaplaciana) #módulo

histogramaSObel = cv.calcHist([imagemSobel], [0], None, [256], [0, 256])

cv.imshow('Sobel X', xAbsoluta)
cv.imshow('Sobel Y', yAbsoluta)
cv.imshow('Sobel', imagemSobel)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 2)
plt.plot(histogramaSObel, color='black')
plt.title('Histograma Sobel')
plt.xlabel('Intensidade de Pixel ou nível de cinza (0-255)')
plt.ylabel('Número de Pixels ou frequência')
plt.grid(True)
plt.tight_layout()
plt.show()


cv.waitKey(0)
cv.destroyAllWindows()
