import cv2  as cv
import numpy as np

imagemOriginal = cv.imread('C:/enviroment/learningOpenCV/10/cusco.jpg')
cv.imshow('Original', imagemOriginal)

imagemCinza = cv.cvtColor(imagemOriginal, cv.COLOR_BGR2GRAY)
cv.imshow('Cinza', imagemCinza)




altura, largura = imagemCinza.shape
print('Altura: \n Largura: ', altura, largura)

matrizDaImagem = np.zeros((altura, largura), dtype=np.uint8)

matrizDaImagemComLimiar = np.zeros((altura, largura), dtype=np.uint8)

limiar = 110
valorMaximo = 190

for i in range(altura):
    for j in range(largura):
        pixel = imagemCinza[i, j]
        matrizDaImagem[i, j] = pixel
        if pixel > limiar:
            matrizDaImagemComLimiar[i, j] = valorMaximo
        else:
            matrizDaImagemComLimiar[i, j] = 0

#identifico o pixel atual com os contadores, atribuo ele na respectiva
# coordenada da matriz e comparo: esse pixel é maior do que o limiar? 
# se sim, atribuo o valor máximo, se não, atribuo 0. 


caminho = 'C:/enviroment/learningOpenCV/10/matrizdaimagem.txt'
caminho2 = 'C:/enviroment/learningOpenCV/10/matrizdaimagemcomlimiar.txt'

np.savetxt(caminho, matrizDaImagem, fmt='%d') 
np.savetxt(caminho2, matrizDaImagemComLimiar, fmt='%d') #ver o efeito limiar na matriz
print(matrizDaImagem)

cv.imshow('Matriz', matrizDaImagem)  
cv.imshow('Matriz com limiar', matrizDaImagemComLimiar)

cv.waitKey(0)
cv.destroyAllWindows()