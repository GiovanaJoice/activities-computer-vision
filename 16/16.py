import cv2 as cv
import numpy as np

camera = cv.VideoCapture(0)

rodando = True

while rodando:
  status, frame = camera.read()

  framecinza = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
  frameEqualizado = cv.equalizeHist(framecinza)

  cv.imshow('Camera', frame)
  cv.imshow('Camera Cinza', framecinza)
  cv.imshow('Camera Equalizada', frameEqualizado)

  opcao = cv.waitKey(1) 
  if opcao == ord('x'):
    cv.imwrite('C:/enviroment/learningOpenCV/16/camera.jpg', framecinza)
    cv.imwrite('C:/enviroment/learningOpenCV/16/camera_equalizada.jpg', frameEqualizado)
    rodando = False

  
camera.release()
cv.destroyAllWindows()

cv.imshow('Camera cinza', framecinza)
cv.imshow('Camera com Filtro Equalizado', frameEqualizado)
cv.waitKey(0)
cv.destroyAllWindows()
