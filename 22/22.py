import cv2 as cv
import numpy as np

imagemOriginal = cv.imread('C:/enviroment/learningOpenCV/22/imagemGerada.png')
imagemCinza = cv.cvtColor(imagemOriginal, cv.COLOR_BGR2GRAY)
altura, largura = imagemCinza.shape
print(f'Altura: {altura}, Largura: {largura}')

def selecionarSeed(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(f'Seed selecionada: ({x}, {y})')
        seed = (y, x)
        algoritmoDeCrescimentoDeRegiao(seed)

def algoritmoDeCrescimentoDeRegiao(seed):
    regiao = np.zeros((altura, largura), dtype=np.uint8)
    listaDePixels = [seed]
    pixelsVisitados = np.zeros((altura, largura), dtype=bool)
    pixelsVisitados[seed] = True
    
    vizinhos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while len(listaDePixels) > 0:
        yAtual, xAtual = listaDePixels.pop(0)
        regiao[yAtual, xAtual] = 255
        
        for dy, dx in vizinhos:
            yVizinho = yAtual + dy
            xVizinho = xAtual + dx

            if 0 <= yVizinho < altura and 0 <= xVizinho < largura:
                if not pixelsVisitados[yVizinho, xVizinho]:
                    pixelsVisitados[yVizinho, xVizinho] = True
                    if imagemCinza[yVizinho, xVizinho] < 127:
                        listaDePixels.append((yVizinho, xVizinho))

    imagemResultado = np.zeros((altura, largura, 3), dtype=np.uint8)
    imagemResultado[regiao == 255] = [255, 0, 0]
    
    somaX = 0
    somaY = 0
    contadorDePixels = 0
    
    for i in range(altura):
        for j in range(largura):
            if regiao[i, j] == 255:
                somaX += j
                somaY += i
                contadorDePixels += 1

    if contadorDePixels > 0:
        xc = somaX // contadorDePixels
        yc = somaY // contadorDePixels
        print(f"Centróide calculated: Xc={xc}, Yc={yc}")
        
        cv.circle(imagemResultado, (xc, yc), 4, (0, 255, 0), -1)

        cv.imshow('Regiao azul com centroide', imagemResultado)
        cv.imwrite('C:/enviroment/learningOpenCV/22/resultadoQ22.png', imagemResultado)

nomeJanela = 'Clique na imagem para selecionar a seed'
cv.namedWindow(nomeJanela)
cv.setMouseCallback(nomeJanela, selecionarSeed)
cv.imshow(nomeJanela, imagemCinza)

cv.waitKey(0)
cv.destroyAllWindows()