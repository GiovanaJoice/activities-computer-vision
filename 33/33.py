import cv2 as cv
import numpy as np
from pathlib import Path

pasta_atual = Path(__file__).parent
caminho_imagem = pasta_atual / "romeroBritto.jpg"
imagemOriginal = cv.imread(str(caminho_imagem))
imagemCinza = cv.cvtColor(imagemOriginal, cv.COLOR_BGR2GRAY)
imagemSuavizada = cv.GaussianBlur(imagemCinza, (5, 5), 0)
bordasCanny = cv.Canny(imagemSuavizada, 50, 150)
contornos, _ = cv.findContours(
    bordasCanny, 
    cv.RETR_EXTERNAL, 
    cv.CHAIN_APPROX_SIMPLE
)
pasta_subimagens = pasta_atual / "subimagens"
pasta_subimagens.mkdir(exist_ok=True)
print("=" * 45)
print(f"Total de contornos para recortar: {len(contornos)}")
print("=" * 45)

for i, contorno in enumerate(contornos):
    x, y, largura, altura = cv.boundingRect(contorno)
    subimagem = imagemOriginal[y : y + altura, x : x + largura]
    nome_arquivo = f"subimagem_obj_{i + 1}.png"
    caminho_saida_sub = pasta_subimagens / nome_arquivo
    cv.imwrite(str(caminho_saida_sub), subimagem)
    cv.imshow(f"Objeto {i + 1}", subimagem)
    print(f"-> Salvo: {nome_arquivo} | Dimensões: {largura}x{altura}px")

print("=" * 45)
cv.imshow('Imagem Original Completa', imagemOriginal)
cv.waitKey(0)
cv.destroyAllWindows()