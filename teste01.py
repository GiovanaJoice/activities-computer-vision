"""
import cv2
import numpy as np
print("Versão do OpenCV:", cv2.__version__)
print("Versão do NumPy:", np.__version__)
"""

import numpy as np
import cv2 as cv
# Load a color image in grayscale
img = cv.imread('messi5.jpg', 0) #nomes de janelas precisam ser diferentes
#digitar 0 implica que a imagem ficará aberta por tempo indeterminado 
cv.imshow('image',img)


cv.waitKey(0)
cv.destroyAllWindows() #parÂmetro vazio = fecha tudp, pra ser específico tem q botar o nome da janela entre os parênteses

#perguntar sobre salvar