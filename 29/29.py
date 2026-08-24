
import cv2 as cv
import numpy as np
from pathlib import Path # adaptacao dos caminhos no mac

pasta_atual = Path(__file__).parent
caminho_imagem = pasta_atual / "formasGeometricas.png"
imagemOriginal = cv.imread(str(caminho_imagem))

imagemCinza = cv.cvtColor(imagemOriginal, cv.COLOR_BGR2GRAY)
imagemSuavizada = cv.GaussianBlur(imagemCinza, (3, 3), 2)#evita ruídos pq houg [e] sensivel a [pixels serrilhados
#quando eu tentei com o kernel 9x9 mais de um circulo foi detectado na regiao de apenas um circulo
#ja com com sigma em 0 um circulo que tinha um formato de elipse nem foi detectado

circulos = cv.HoughCircles(imagemSuavizada,cv.HOUGH_GRADIENT,
    dp=1,
    minDist=50,
    param1=50,
    param2=30,
    minRadius=10,
    maxRadius=200
)
imagemResultado = imagemOriginal.copy()#sobrepoe os desenhoss de resultado na img original

if circulos is not None: #se houverem circulos, faca
    circulos = np.uint16(np.around(circulos))
    print(f"total de círculos detectados: {len(circulos[0])}")
    for c in circulos[0, :]:#tipo uma matriz x , y, raio
        centro = (c[0], c[1]) #x, y
        raio = c[2]#tamanho do raio
        cv.circle(imagemResultado, centro, raio, (0, 255, 0), 3) 
        cv.circle(imagemResultado, centro, 2, (0, 0, 255), 5)
else:
    print("nenhum círculo encontrado")

cv.imshow('original', imagemOriginal)
cv.imshow('Hough (circulos detectados)', imagemResultado)
caminho_saida = pasta_atual / "imagemGerada.png"
cv.imwrite(str(caminho_saida), imagemResultado)

cv.waitKey(0)
cv.destroyAllWindows()