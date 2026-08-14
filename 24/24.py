import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#import pyautogui


imagemOriginal = cv.imread('C:/enviroment/learningOpenCV/24/louvaaDeus.jpg')
altura, largura, canal = imagemOriginal.shape
print(f'Altura: {altura}, Largura: {largura}')

def selecionarSeed(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(f'Seed selecionada: ({x}, {y})')
        seed = (y, x)
        algoritmoDeCrescimentoDeRegiao(seed)

def algoritmoDeCrescimentoDeRegiao(seed):
   corSemente = imagemOriginal[seed]
   rangeTolerado = 95 #definindo a variacao de cor q aceitamos
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
              pixelsVisitados[yVizinho, xVizinho] = True #marca como visitado
              corVizinho = imagemOriginal[yVizinho, xVizinho] #pegando a cor bgr dos pixels vizinho na imagem original
              distancia = np.linalg.norm(corVizinho.astype(int) - corSemente.astype(int))

              if distancia < rangeTolerado:
                 listaDePixels.append((yVizinho, xVizinho)) #adiciona a coordenada no final da fila
  
   #CoDIGO DA Questao 11 reaproveitado
   contadorX = 0
   contadorY = 0
   contadorPixels = 0

   for i in range(altura): #linha  -> y
      for j in range(largura): #coluna -> x
         pixel = regiao[i, j]
         if pixel == 255: #se o pixel for parte da região crescida
               contadorX += j
               contadorY += i
               contadorPixels += 1

   if contadorPixels > 0:
      centroX = contadorX / contadorPixels
      centroY = contadorY / contadorPixels
      #achando as coordenadas do centro
      print('Centro X: ', centroX)
      print('Centro Y: ', centroY)

      imagemColorida = np.zeros((altura, largura, 3), dtype=np.uint8)
      imagemColorida[regiao == 255] = [255, 0, 0]  # Azul para a região crescida
      cv.circle(imagemColorida, (int(centroX), int(centroY)), 5, (0, 255, 0), -1)
      cv.imwrite('C:/enviroment/learningOpenCV/24/imagemGerada.jpg', imagemColorida)
      cv.imshow('Imagem com Centro', imagemColorida)
   else:
      print('Nenhum pixel  encontrado na imagem.')

nomeJanela = 'Clique na imagem para selecionar a seed'
cv.namedWindow(nomeJanela)
cv.setMouseCallback(nomeJanela, selecionarSeed)
cv.imshow(nomeJanela, imagemOriginal)

cv.waitKey(0)
cv.destroyAllWindows()