import cv2 as cv
import numpy as np
import sys 

imagemOriginal = cv.imread('C:/enviroment/learningOpenCV/09/giantscausewaycolorido.jpg')
imagemCinza = cv.imread('C:/enviroment/learningOpenCV/09/giantscausewaycolorido.jpg', 0)
cv.imshow('Cinza', imagemCinza)

#essa aq tem 1200x900
altura, largura = imagemCinza.shape

matrizDaImagem = np.zeros((altura, largura), dtype=np.uint8) #cria uma matriz de zeros com o mesmo tamanho da imagem

#cópia pixel a pixel
for y in range(altura):
    for x in range(largura):
        matrizDaImagem[y, x] = imagemCinza[y, x] #preenche a matriz 

caminho = 'C:/enviroment/learningOpenCV/09/dados.txt' #usando write n dava certo
#matrizDaImagem = np.array(imagemOriginal) #transforma a imagem em uma matriz
np.savetxt(caminho, matrizDaImagem, fmt='%d') #salva a matriz em um txt
print(matrizDaImagem) 


#print(f'Altura: {altura}, Largura: {largura}, Canais: {canais}')

cv.waitKey(0)
cv.destroyAllWindows()