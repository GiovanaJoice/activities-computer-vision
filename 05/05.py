import cv2 as cv
import numpy as np

imagemCinza = cv.imread('C:/enviroment/learningOpenCV/05/paisagemColorida.jpg', 0)
cv.imshow('Cinza', imagemCinza)

imagemBaixaMediaana = cv.medianBlur(imagemCinza, 25) 
cv.imshow('Baixa Mediana', imagemBaixaMediaana)

imagemComBlur = cv.blur(imagemCinza, (25, 25)) #ver os paametros do blur + reverconceito
cv.imshow('Blur', imagemComBlur)

cv.imwrite('C:/enviroment/learningOpenCV/05/paisagemCinza.jpg', imagemCinza)
cv.imwrite('C:/enviroment/learningOpenCV/05/paisagemBaixaMedianaa.jpg', imagemBaixaMediaana)
cv.imwrite('C:/enviroment/learningOpenCV/05/paisagemBlur.jpg', imagemComBlur)

cv.waitKey(0)
cv.destroyAllWindows()