import cv2 as cv
import numpy as np
imagemOriginal = cv.imread('C:/enviroment/learningOpenCV/27/formasGeometricas.png')
imagemCinza = cv.cvtColor(imagemOriginal, cv.COLOR_BGR2GRAY)
altura, largura = imagemCinza.shape
matrizRotulos = np.zeros((altura, largura), dtype=np.int32)
imagemResultado = np.zeros((altura, largura, 3), dtype=np.uint8)
contadorObjetos = 0

def gerarCorAleatoria():
    return [int(c) for c in np.random.randint(50, 255, size=3)]

def crescerRegiao(seed, numRegiao, cor):
    listaDePixels = [seed]
    matrizRotulos[seed] = numRegiao
    imagemResultado[seed] = cor
    vizinhos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while len(listaDePixels) > 0:
        yAtual, xAtual = listaDePixels.pop(0)
        for dy, dx in vizinhos:
            yVizinho, xVizinho = yAtual + dy, xAtual + dx
            if 0 <= yVizinho < altura and 0 <= xVizinho < largura:
                if imagemCinza[yVizinho, xVizinho] < 127 and matrizRotulos[yVizinho, xVizinho] == 0:
                    matrizRotulos[yVizinho, xVizinho] = numRegiao
                    imagemResultado[yVizinho, xVizinho] = cor
                    listaDePixels.append((yVizinho, xVizinho))

for i in range(altura):
    for j in range(largura):
        if imagemCinza[i, j] < 127 and matrizRotulos[i, j] == 0:
            contadorObjetos += 1
            corObjeto = gerarCorAleatoria()
            crescerRegiao((i, j), contadorObjetos, corObjeto)

#esse e o looping responsavel por gerar as iimagens 
for k in range(1, contadorObjetos + 1): #(comecando de um pq 0 é o fundo e +1 pra não parar no penultimo e ignorar o ultimo elemento)
    linhas, colunas = np.where(matrizRotulos == k) #se k vai correspondendo ao objeto contado, a comparação
                                                   #em where sginifica que linhas, colunas armazenam os endereços que contém o numero 
                                                   # correspondente ao objeto
    subImagem = imagemOriginal[min(linhas):max(linhas)+1, min(colunas):max(colunas)+1] #recortes dos limites onde o objeto termina
    cv.imshow(f'Objeto {k}', subImagem)
    cv.imwrite(f'C:/enviroment/learningOpenCV/27/subimagem_{k}.png', subImagem)

cv.imshow('Objetos Rotulados (Geral)', imagemResultado)
cv.imwrite('C:/enviroment/learningOpenCV/27/resultado_geral.png', imagemResultado)
cv.waitKey(0)
cv.destroyAllWindows()