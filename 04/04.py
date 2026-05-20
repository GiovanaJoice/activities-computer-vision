import numpy as np
import cv2 as cv

imagem = cv.imread('C:/enviroment/learningOpenCV/04/imgcolorida4.jpg')
b, g, r = cv.split(imagem)