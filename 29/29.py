
import cv2 as cv
import numpy as np

caminho = 'C:/enviroment/learningOpenCV/29/formasGeometricas.png'
imagemOriginal = cv.imread(caminho)
imagemCinza = cv.cvtColor(imagemOriginal, cv.COLOR_BGR2GRAY)
imagemSuavizada = cv.GaussianBlur(imagemCinza, (9, 9), 2)#evita ruídos
circulos = cv.HoughCircles(imagemSuavizada,cv.HOUGH_GRADIENT,
    dp=1,
    minDist=50,
    param1=50,
    param2=30,
    minRadius=10,
    maxRadius=200
)
imagemResultado = imagemOriginal.copy()

if circulos is not None:
    circulos = np.uint16(np.around(circulos))
    print(f"total de círculos detectados: {len(circulos[0])}")
    for c in circulos[0, :]:
        centro = (c[0], c[1])
        raio = c[2]
        cv.circle(imagemResultado, centro, raio, (0, 255, 0), 3)
        cv.circle(imagemResultado, centro, 2, (0, 0, 255), 5)
else:
    print("nenhum círculo encontrado! Ajuste o param2.")

cv.imshow('original', imagemOriginal)
cv.imshow('Hough (circulos detectados)', imagemResultado)
cv.imwrite('C:/enviroment/learningOpenCV/29/imagemGerada.png', imagemResultado)

cv.waitKey(0)
cv.destroyAllWindows()