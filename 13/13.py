import cv2 as cv
import numpy as np

imagemOriginal = cv.imread('C:/enviroment/learningOpenCV/13/coraline.jpg')
imagemCinza = cv.cvtColor(imagemOriginal, cv.COLOR_BGR2GRAY)

altura, largura = imagemCinza.shape
print('Largura: ', largura)
print('Altura: ', altura)

cv.imshow('Original', imagemOriginal)
cv.imshow('Cinza', imagemCinza)

sobelX = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobelY = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

matrizDaImagem = np.zeros((altura, largura), dtype=np.uint8) #y, x



for i in range(1, largura - 1):
    for j in range(1, altura - 1):
        regiao = imagemCinza[j - 1:j + 2, i - 1:i + 2] #posicao anterior, atual, proxima (usar 2 n significa que considera 1 posição a menos que ele)
        valorX = np.sum(regiao * sobelX)
        valorY = np.sum(regiao * sobelY)
        valorFinal = np.sqrt(valorX ** 2 + valorY ** 2)
        matrizDaImagem[j, i] = min(255, int(valorFinal)) #visualização das cores/intensidade da borda

cv.imshow('Sobel', matrizDaImagem)
cv.imwrite('C:/enviroment/learningOpenCV/13/coraline_sobel.jpg', matrizDaImagem)

cv.waitKey(0)
cv.destroyAllWindows()

#0preto, 255 branco