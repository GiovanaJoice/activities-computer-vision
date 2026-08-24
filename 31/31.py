import cv2 as cv
import numpy as np
from pathlib import Path # adaptacao dos caminhos no mac

pasta_atual = Path(__file__).parent
caminho_imagem = pasta_atual / "romeroBritto.jpg"
imagemOriginal = cv.imread(str(caminho_imagem))
imagemCinza = cv.cvtColor(imagemOriginal, cv.COLOR_BGR2GRAY)
imagemSuavizada = cv.GaussianBlur(imagemCinza, (5, 5), 0)
bordasCanny = cv.Canny(imagemSuavizada, 40, 100)

contornos, hierarquia = cv.findContours(
    bordasCanny, 
    cv.RETR_EXTERNAL, #detecta apenas as bordas externas (1 contorno por objeto)
    cv.CHAIN_APPROX_SIMPLE #comprime segmentos redundantes
)

imagemResultado = imagemOriginal.copy()
cv.drawContours(imagemResultado, contornos, -1, (0, 255, 0), 2)
quantidadeObjetos = len(contornos)
print(f"Total de objetos/contornos detectados: {quantidadeObjetos}")
cv.imshow('imagem de entrada', imagemOriginal)
cv.imshow('bordas com Canny', bordasCanny)
cv.imshow('contornos identificados', imagemResultado)

caminho_saida = pasta_atual / "imagemGerada.png"
cv.imwrite(str(caminho_saida), imagemResultado)

caminho_saida = pasta_atual / "imagemCanny.png"
cv.imwrite(str(caminho_saida), bordasCanny)

cv.waitKey(0)
cv.destroyAllWindows()