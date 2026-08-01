import cv2 as cv
import numpy as np 

imagemOriginal = cv.imread('C:/enviroment/learningOpenCV/08/imagemOriginal.jpg')
imagemCinza = cv.imread('C:/enviroment/learningOpenCV/08/imagemOriginal.jpg', 0)
cv.imshow('Imagem Original', imagemCinza)


altura, largura = imagemCinza.shape #preto e branco tem 2 dimensões e colorida tem 3 


imagemreduzida = cv.resize(imagemCinza, (altura//2, largura//2), interpolation=cv.INTER_AREA) #ver os parâmetros do resize + rever conceito
imagemDuplicada = cv.resize(imagemCinza, (altura*2, largura*2), interpolation=cv.INTER_LINEAR)


#comparativo = "Altura: {altura}\nLargura: {largura}\nCanais: {c}"

print('Altura original: \n Altura reduzida: \n Altura duplicada: ', altura, altura//2, altura*2)
print('Largura original: \n Largura reduzida: \n Largura duplicada: ', largura, largura//2, largura*2)
#print('Canais: \n ', c) 
print('comparativo')

cv.imshow('Original', imagemOriginal)
cv.imshow('Reduzida', imagemreduzida)
cv.imshow('Duplicada', imagemDuplicada)

cv.imwrite('C:/enviroment/learningOpenCV/08/imagemReduzida.jpg', imagemreduzida)
cv.imwrite('C:/enviroment/learningOpenCV/08/imagemDuplicada.jpg', imagemDuplicada)

cv.waitKey(0)
cv.destroyAllWindows()