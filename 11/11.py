import cv2 as cv
import numpy as np 

imagemOriginal = cv.imread('C:/enviroment/learningOpenCV/11/quadradoPreto.jpg')
cv.imshow('Original', imagemOriginal)

imagemCinza = cv.cvtColor(imagemOriginal, cv.COLOR_BGR2GRAY) #deixa uma camada e nao 3
cv.imshow('Cinza', imagemCinza)

altura, largura = imagemCinza.shape
print('Altura e largura: ', altura, largura)

matrizDaImagem = np.zeros((altura, largura), dtype=np.uint8)


contadorX = 0
contadorY = 0
contadorPixels = 0


for i in range(altura): #linha  -> y
    for j in range(largura): #coluna -> x
        pixel = imagemCinza[i, j]
        if pixel == 0:
            contadorX += j
            contadorY += i
            contadorPixels += 1
#se as coordenadas do pixel atual forem pretas (0,0), então
#os contadores identificam que eles fazem parte do quadrado
#e as coordenadas, x e y, sao incrementados para contagem



if contadorPixels > 0:
    centroX = contadorX / contadorPixels
    centroY = contadorY / contadorPixels
    #achando as coordenadas do centro
    print('Centro X: ', centroX)
    print('Centro Y: ', centroY)


    imagemComCirculo = cv.circle(imagemOriginal, (int(centroX), int(centroY)), 5, (0, 0, 255), -1)
    cv.imwrite('C:/enviroment/learningOpenCV/11/imagemComCentro.jpg', imagemComCirculo)
    cv.imshow('Imagem com Centro', imagemComCirculo)
    cv.waitKey(0)
else:
    print('Nenhum pixel preto encontrado na imagem.')


cv.waitKey(0)
cv.destroyAllWindows()