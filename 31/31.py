import cv2 as cv
import numpy as np
from pathlib import Path

# 1. Carrega a imagem original da questão 30
pasta_atual = Path(__file__).parent
caminho_imagem = pasta_atual / "desenho_formas.png"
imagemOriginal = cv.imread(str(caminho_imagem))

# 2. Converte para escala de cinza e suaviza
imagemCinza = cv.cvtColor(imagemOriginal, cv.COLOR_BGR2GRAY)
imagemSuavizada = cv.GaussianBlur(imagemCinza, (5, 5), 0)

# 3. Detecta as bordas com Canny
bordasCanny = cv.Canny(imagemSuavizada, 50, 150)

# 4. Encontra os contornos externos (cvFindContours moderno)
contornos, hierarquia = cv.findContours(
    bordasCanny, 
    cv.RETR_EXTERNAL, 
    cv.CHAIN_APPROX_SIMPLE
)

# 5. Cria uma cópia da imagem para desenhar os retângulos
imagemResultado = imagemOriginal.copy()

print(f"Total de objetos encontrados: {len(contornos)}")

# 6. Percorre cada contorno encontrado de forma correta
for i, contorno in enumerate(contornos):
    # Calcula o retângulo delimitador do contorno atual (cvContourBoundingRect)
    x, y, largura, altura = cv.boundingRect(contorno)
    
    # Define os dois cantos opostos do retângulo:
    canto_superior_esquerdo = (x, y)
    canto_inferior_direito = (x + largura, y + altura)
    
    # Desenha o retângulo delimitador (Vermelho, espessura 2)
    cv.rectangle(imagemResultado, canto_superior_esquerdo, canto_inferior_direito, (0, 0, 255), 2)
    
    # Escreve o índice do objeto logo acima da caixa
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

# 7. Salva a imagem gerada
caminho_saida = pasta_atual / "resultado_bounding_box.png"
cv.imwrite(str(caminho_saida), imagemResultado)

# 8. Exibe a imagem de entrada e o resultado final
cv.imshow('1 - Imagem Original (Entrada)', imagemOriginal)
cv.imshow('2 - Objetos com Bounding Box (Q31)', imagemResultado)

cv.waitKey(0)
cv.destroyAllWindows()