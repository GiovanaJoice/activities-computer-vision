import cv2 as cv
import numpy as np 

imagemCinza = cv.imread('C:/enviroment/learningOpenCV/08/imagemOriginal.jpg')
cv.imshow('Cinza', imagemCinza)


altura, largura, c = imagemCinza.shape #preto e branco tem 2 dimensões e colorida tem 3 


imagemreduzida = cv.resize(imagemCinza, (altura//2, largura//2), interpolation=cv.INTER_AREA) #ver os parâmetros do resize + rever conceito
imagemDuplicada = cv.resize(imagemCinza, (altura*2, largura*2), interpolation=cv.INTER_LINEAR)


#comparativo = "Altura: {altura}\nLargura: {largura}\nCanais: {c}"

print('Altura original: \n Altura reduzida: \n Altura duplicada: ', altura, altura//2, altura*2)
print('Largura original: \n Largura reduzida: \n Largura duplicada: ', largura, largura//2, largura*2)
print('Canais: \n ', c) 
print(comparativo)

cv.imshow('Reduzida', imagemreduzida)
cv.imshow('Duplicada', imagemDuplicada)

cv.waitKey(0)
cv.destroyAllWindows()