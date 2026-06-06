import cv2 as cv
import numpy as np

arquivoTXT = 'C:/enviroment/learningOpenCV/10/matrizdaimagem.txt'
matrizDaImagem = np.loadtxt(arquivoTXT, dtype=np.uint8)
cv.imshow('Matriz da Imagem', matrizDaImagem)

print(matrizDaImagem.shape)
      
cv.waitKey(0)

cv.destroyAllWindows()