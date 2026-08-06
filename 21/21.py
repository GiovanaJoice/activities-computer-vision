import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import pyautogui

imagemOriginal = cv.imread('C:/enviroment/learningOpenCV/21/imagemGerada.png')
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
  listaDePixels = [seed] #lista criada começando com a seed sendo passada e ela n pode ser vazia
  pixelsVisitados = np.zeros((altura, largura), dtype=bool)
  pixelsVisitados[seed] = True
  
  vizinhos = [(-1, 0), (1, 0), (0, -1), (0, 1)] #cima, baixo, esquerda, direita

  while len(listaDePixels) > 0:
     yAtual, xAtual = listaDePixels.pop(0)
     regiao[yAtual, xAtual] = 255 #marca o pixel atual como parte da região
     for dy, dx in vizinhos:
        yVizinho = yAtual + dy
        xVizinho = xAtual + dx

        if 0 <= yVizinho < altura and 0 <= xVizinho < largura:
           if not pixelsVisitados[yVizinho, xVizinho]: #Se for falso, significa que o pixel ainda não foi visitado
              pixelsVisitados[yVizinho, xVizinho] = True
              if imagemCinza[yVizinho, xVizinho] < 127:
                 listaDePixels.append((yVizinho, xVizinho)) #adiciona a coordenada no final da fila
  cv.imshow('Regiao Crescida', regiao)

nomeJanela = 'Clique na imagem para selecionar a seed'
cv.namedWindow(nomeJanela)
cv.setMouseCallback(nomeJanela, selecionarSeed)
cv.imshow(nomeJanela, imagemCinza)
cv.waitKey(0)
cv.destroyAllWindows()