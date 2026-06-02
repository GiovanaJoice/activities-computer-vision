import cv2 as cv
import numpy as np
import sys 

imagemOriginal = cv.imread('C:/enviroment/learningOpenCV/09/giantscausewaycolorido.jpg')
imagemCinza = cv.imread('C:/enviroment/learningOpenCV/09/giantscausewaycolorido.jpg', 0)
cv.imshow('Cinza', imagemCinza)

#essa aq tem 1200x900
#altura, largura, canais = imagemOriginal.shape

matrizDaImagem = imagemCinza
caminho = 'C:/enviroment/learningOpenCV/09/dados.txt' #usando write n dava certo
#matrizDaImagem = np.array(imagemOriginal) #transforma a imagem em uma matriz
np.savetxt(caminho, matrizDaImagem, fmt='%d') #salva a matriz em um txt
print(matrizDaImagem) 


#print(f'Altura: {altura}, Largura: {largura}, Canais: {canais}')

cv.waitKey(0)
cv.destroyAllWindows()