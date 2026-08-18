import cv2 as cv
import numpy as np

imagemOriginal = cv.imread('C:/enviroment/learningOpenCV/25/formasGeometricas.png')
imagemCinza = cv.cvtColor(imagemOriginal, cv.COLOR_BGR2GRAY)
altura, largura = imagemCinza.shape

imagemGerada = np.zeros((altura, largura, 3), dtype=np.uint8) #cria uma tela preta tridimensional (BGR) onde os objetos serao pintados em cores
matrizRotulos = np.zeros((altura, largura), dtype=np.uint8) #matriz 2d pra contagem de elementos e fundo

listaDeCores = [[0, 0, 255], [255, 0, 0],[0, 255, 0]] #BGR
contadorDeCliques = 0

def escolherSeed(event, x, y, flags, param):
    global contadorDeCliques
    if event == cv.EVENT_LBUTTONDOWN:
        if contadorDeCliques < 3:
            seed = (y, x)
            contadorDeCliques += 1
            print(f'pintando objeto {contadorDeCliques}...')
            algoritmoDeCrescimentoDeRegiao(seed, contadorDeCliques)
        else:
            print('todos os 3 objetos já foram pintados')

def algoritmoDeCrescimentoDeRegiao(seed, numRegiao):
    pixelsVisitados = np.zeros((altura, largura), dtype=bool)
    listaDePixels = [seed]
    pixelsVisitados[seed] = True
    
    corAtual = listaDeCores[numRegiao - 1]
    vizinhos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while len(listaDePixels) > 0:
        yAtual, xAtual = listaDePixels.pop(0)
        matrizRotulos[yAtual, xAtual] = numRegiao
        imagemGerada[yAtual, xAtual] = corAtual
        for dy, dx in vizinhos:
            yVizinho = yAtual + dy
            xVizinho = xAtual + dx

            if 0 <= yVizinho < altura and 0 <= xVizinho < largura:
                if not pixelsVisitados[yVizinho, xVizinho]:
                    pixelsVisitados[yVizinho, xVizinho] = True
                    if imagemCinza[yVizinho, xVizinho] < 127:
                        listaDePixels.append((yVizinho, xVizinho))
    cv.imshow('Imagem Resultado', imagemGerada)
    #cv.imshow('Imagem invertida', matrizRotulos)
    cv.imwrite('C:/enviroment/learningOpenCV/25/resultado.png', imagemGerada)

nomeJanela = 'Clique nos objetos (1:Vermelho, 2:Azul, 3:Verde)'
cv.namedWindow(nomeJanela)
cv.setMouseCallback(nomeJanela, escolherSeed)
cv.imshow(nomeJanela, imagemCinza)
cv.imshow('Original', imagemOriginal)
cv.waitKey(0)
cv.destroyAllWindows()