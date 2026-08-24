import cv2 as cv
import numpy as np
from pathlib import Path

pasta_atual = Path(__file__).parent
caminho_imagem = pasta_atual / "romeroBritto.jpg"
imagemOriginal = cv.imread(str(caminho_imagem))

imagemCinza = cv.cvtColor(imagemOriginal, cv.COLOR_BGR2GRAY)
imagemSuavizada = cv.GaussianBlur(imagemCinza, (5, 5), 0)

bordasCanny = cv.Canny(imagemSuavizada, 50, 150)

contornos, hierarquia = cv.findContours(
    bordasCanny, 
    cv.RETR_EXTERNAL, 
    cv.CHAIN_APPROX_SIMPLE
)

imagemResultado = imagemOriginal.copy()
print("=" * 45)
print(f"Total de objetos encontrados: {len(contornos)}")
print("=" * 45)

for i, contorno in enumerate(contornos):
    area = cv.contourArea(contorno)
    x, y, largura, altura = cv.boundingRect(contorno)
    canto1 = (x, y)
    canto2 = (x + largura, y + altura)
    cv.rectangle(imagemResultado, canto1, canto2, (0, 0, 255), 2)
    texto_area = f"Obj {i + 1}: {int(area)}px"
    cv.putText(
        imagemResultado, 
        texto_area, 
        (x, max(y - 8, 15)), 
        cv.FONT_HERSHEY_SIMPLEX, 
        0.45, 
        (255, 0, 0), 
        1, 
        cv.LINE_AA
    )
    print(f"Objeto {i + 1}: Área = {area:.2f} pixels² | Posição=({x}, {y}) | Largura={largura}px | Altura={altura}px")
print("=" * 45)

caminho_saida = pasta_atual / "resultado_areas.png"
cv.imwrite(str(caminho_saida), imagemResultado)
cv.imshow('1 - Imagem Original', imagemOriginal)
cv.imshow('2 - Objetos com Retangulos e Areas (Q32)', imagemResultado)

cv.waitKey(0)
cv.destroyAllWindows()