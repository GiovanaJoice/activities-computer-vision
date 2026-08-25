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

print(f"Total de objetos encontrados: {len(contornos)}")
for i, contorno in enumerate(contornos):
    x, y, largura, altura = cv.boundingRect(contorno)
    canto_superior_esquerdo = (x, y)
    canto_inferior_direito = (x + largura, y + altura)
    cv.rectangle(imagemResultado, canto_superior_esquerdo, canto_inferior_direito, (0, 0, 255), 2)
    cv.putText(
        imagemResultado, 
        f"Obj {i + 1}", 
        (x, max(y - 8, 15)), 
        cv.FONT_HERSHEY_SIMPLEX, 
        0.5, 
        (255, 0, 0), 
        1, 
        cv.LINE_AA
    )
    print(f"-> Objeto {i + 1}: x={x}, y={y}, largura={largura}px, altura={altura}px")

caminho_saida = pasta_atual / "resultado_bounding_box.png"
cv.imwrite(str(caminho_saida), imagemResultado)

cv.imshow('imagem original', imagemOriginal)
cv.imshow('bounding box', imagemResultado)

cv.waitKey(0)
cv.destroyAllWindows()