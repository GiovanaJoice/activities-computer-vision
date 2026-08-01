import cv2 as cv
import numpy as np

imagemOriginal = cv.imread('C:/enviroment/learningOpenCV/17/upAltasAventuras.jpg')
imagemCinza = cv.cvtColor(imagemOriginal, cv.COLOR_BGR2GRAY)

cv.imshow('Original', imagemOriginal)
cv.imshow('Cinza', imagemCinza)

altura, largura = imagemCinza.shape
totalDePixels = altura * largura
print('Total de pixels: ', totalDePixels)
print('Largura: ', largura, 'Altura: ', altura)

for i range(altura):
  for j in range(largura):
  tom = imagemCinza[i, j]
  histograma[tom] += 1

cdf.np.zeros(256, dtype=np.float)
soma_acumulada = 0

for i in range(256):
  soma_acumulada += histograma[i]
  cdf[i] = soma_acumulada / totalDePixels

tabela_mapeamento = np.zeros(256, dtype=np.uint8)
for i in range(256):
  tabela_mapeamento[i] = np.round(cdf[i] * 255)

cv.waitKey(0)
cv.destroyAllWindows()