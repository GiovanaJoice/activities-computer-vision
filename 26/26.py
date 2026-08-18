import cv2 as cv
import numpy as np

imagemOriginal = cv.imread('C:/enviroment/learningOpenCV/26/formasGeometricas.png')
imagemCinza = cv.cvtColor(imagemOriginal, cv.COLOR_BGR2GRAY)
altura, largura = imagemCinza.shape

matrizRotulos = np.zeros((altura, largura), dtype=np.int32)
imagemResultado = np.zeros((altura, largura, 3), dtype=np.uint8)

def gerarCorAleatoria():
    return [int(c) for c in np.random.randint(50, 255, size=3)]

def algoritmoDeCrescimentoDeRegiao(seed, numRegiao, cor):
    listaDePixels = [seed]
    matrizRotulos[seed] = numRegiao
    imagemResultado[seed] = cor
    vizinhos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while len(listaDePixels) > 0:
        yAtual, xAtual = listaDePixels.pop(0)
        for dy, dx in vizinhos:
            yVizinho = yAtual + dy
            xVizinho = xAtual + dx

            if 0 <= yVizinho < altura and 0 <= xVizinho < largura:
                if imagemCinza[yVizinho, xVizinho] < 127 and matrizRotulos[yVizinho, xVizinho] == 0:
                    matrizRotulos[yVizinho, xVizinho] = numRegiao
                    imagemResultado[yVizinho, xVizinho] = cor
                    listaDePixels.append((yVizinho, xVizinho))

contadorObjetos = 0

for i in range(altura):
    for j in range(largura):
        if imagemCinza[i, j] < 127 and matrizRotulos[i, j] == 0:
            contadorObjetos += 1
            corObjeto = gerarCorAleatoria()
            print(f"Objeto {contadorObjetos} detectado na coordenada ({j}, {i})")
            algoritmoDeCrescimentoDeRegiao((i, j), contadorObjetos, corObjeto)

print(f"\ntotal de objetos detectados: {contadorObjetos}")
cv.imshow('original (Cinza)', imagemCinza)
cv.imshow('objetos rotulados', imagemResultado)
cv.imwrite('C:/enviroment/learningOpenCV/26/resultado.png', imagemResultado)
cv.waitKey(0)
cv.destroyAllWindows()