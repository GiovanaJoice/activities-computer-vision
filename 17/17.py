import cv2 as cv
import numpy as np

imagemOriginal = cv.imread('C:/enviroment/learningOpenCV/17/upAltasAventuras.jpg')
imagemCinza = cv.cvtColor(imagemOriginal, cv.COLOR_BGR2GRAY)

altura, largura = imagemCinza.shape
totalDePixels = altura * largura
print('Total de pixels: ', totalDePixels)
print('Largura: ', largura, 'Altura: ', altura)


histograma = np.zeros(256, dtype=np.int32)
for i in range(altura):
  for j in range(largura):
    tom = imagemCinza[i, j]
    histograma[tom] += 1 #conta quantas vezes cada tom aparece na imagem

cdf = np.zeros(256, dtype=np.float32) #cada posição cdf[i] guarda a proporção acumulada de pixels até o tom i
soma_acumulada = 0

for i in range(256):
  soma_acumulada += histograma[i] #soma quantos pixels de cada tom até o tom i
  cdf[i] = soma_acumulada / totalDePixels #calcula a proporção 

tabela_mapeamento = np.zeros(256, dtype=np.uint8)
for i in range(256):
  tabela_mapeamento[i] = np.round(cdf[i] * 255) #amazena o novo tom de cinza (o antigo vai ser multiplicado)

imagemEqualizada = tabela_mapeamento[imagemCinza] #aplica a tabela de mapeamento na imagem original

cv.imshow('Original', imagemOriginal)
cv.imshow('Cinza', imagemCinza)
cv.imshow('Equalizada', imagemEqualizada)
cv.imwrite('C:/enviroment/learningOpenCV/17/imagem_cinza.jpg', imagemCinza)
cv.imwrite('C:/enviroment/learningOpenCV/17/imagem_equalizada.jpg', imagemEqualizada)

cv.waitKey(0)
cv.destroyAllWindows()