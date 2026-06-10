import cv2 as cv
import numpy as np

camera = cv.VideoCapture(0)

rodando = True

while rodando:
  status, frame = camera.read()

  framecinza = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

  if not status or cv.waitKey(1) & 0xFF == ord('x'): #aperte x pra fechar a camera
    rodando = False
    break

  cv.imshow('Camera', frame)
  cv.imshow('Camera Cinza', framecinza)

  cv.imwrite('C:/enviroment/learningOpenCV/15/camera.jpg', framecinza)

  
camera.release()
cv.destroyAllWindows()

cv.imshow('Camera cinza', framecinza)
frameComFiltroCanny = cv.Canny(framecinza, 100, 168)
cv.imshow('Camera com Filtro Canny', frameComFiltroCanny)
cv.imwrite('C:/enviroment/learningOpenCV/15/camera_canny.jpg', frameComFiltroCanny)
cv.waitKey(0)
cv.destroyAllWindows()
