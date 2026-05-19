import numpy as np
import cv2 as cv
# Load a color image in grayscale
img = cv.imread('C:/enviroment/learningOpenCV/01/imgcolorida.jpg', 0) #nomes de janelas precisam ser diferentes
#digitar 0 implica que a imagem ficará aberta por tempo indeterminado 

cv.imshow('image',img)
k = cv.waitKey(0) & 0xFF #recebe do teclado
if k == 27:         # o ESC 
    cv.destroyAllWindows() #sai
elif k == ord('s'): # o s 
    cv.imwrite('C:/enviroment/learningOpenCV/02/messigray.png',img) #salva
    cv.destroyAllWindows()