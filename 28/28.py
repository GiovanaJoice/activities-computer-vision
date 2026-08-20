import cv2 as cv
import numpy

imagemOriginal = cv.imread('C:/enviroment/learningOpenCV/28/caracal.webp')
imagemCinza = cv.cvtColor(imagemOriginal, cv.COLOR_BGR2GRAY)

imagemComBlur = cv.GaussianBlur(imagemCinza, (3,3), 0)
limiarCalculado, imagemLimiarizada = cv.threshold(imagemComBlur, 10, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

print(limiarCalculado)

cv.imshow("Imagem original", imagemOriginal)
cv.imshow("Imagem cinza", imagemCinza)
cv.imshow("Imagem limiar", imagemLimiarizada)
cv.imwrite('C:/enviroment/learningOpenCV/28/imagemcinza.png', imagemCinza)
cv.imwrite('C:/enviroment/learningOpenCV/28/imagemlimiarizada.png', imagemLimiarizada)


cv.waitKey(0)
cv.destroyAllWindows()
