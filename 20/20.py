import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

imagemOriginal = cv.imread('C:/enviroment/learningOpenCV/20/imagemGerada.png')
imagemCinza = cv.cvtColor(imagemOriginal, cv.COLOR_BGR2GRAY)
altura, largura = imagemCinza.shape
print(f'Altura: {altura}, Largura: {largura}')
semente = (120, 160)

regiao = np.zeros((altura, largura), dtype=np.uint8) #eh isso q inverte o fundo, deixa = 0 (preto)
listaDePixels = [semente] #lista criada começando com a seed sendo passada e ela n pode ser vazia
pixelsvisitados = np.zeros((altura, largura), dtype=bool)
pixelsvisitados[semente] = True
vizinhos = [(-1, 0), (1, 0), (0, -1), (0, 1)] #cima, baixo, esquerda, direita (lista de deslocamentos)
##as coordenadas sao do ssistema de cordenadas de matriz, então a coordenada (0, 0) é o pixel do canto superior esquerdo da imagem

while len(listaDePixels) > 0: #pra todos os pixels serem checados até zerar
  yAtual, xAtual = listaDePixels.pop(0) #pop remove o primeiro elemento da lista e retorna ele pra x e y atual
  regiao[yAtual, xAtual] = 255 #marca o pixel atual como parte da região
  for dy, dx in vizinhos: #direção da a coordenada do pixel atual para checar os vizinhos
    yVizinho  = yAtual + dy #coordenada final/real do vizinho
    xVizinho = xAtual + dx

    if 0 <= yVizinho < altura and 0 <= xVizinho < largura:
      if not pixelsvisitados[yVizinho, xVizinho]:
        pixelsvisitados[yVizinho, xVizinho] = True
        if imagemCinza[yVizinho, xVizinho] < 127:
          listaDePixels.append((yVizinho, xVizinho)) #adiciona a coordenada no final da fila

cv.imshow('Imagem Original', imagemOriginal)
cv.imshow('Imagem Cinza', imagemCinza)
cv.imshow('Regiao Crescida', regiao)
cv.imwrite('C:/enviroment/learningOpenCV/20/imagemCinza.png', imagemCinza)
cv.imwrite('C:/enviroment/learningOpenCV/20/regiaoCrescida.png', regiao)
cv.waitKey(0)
cv.destroyAllWindows()