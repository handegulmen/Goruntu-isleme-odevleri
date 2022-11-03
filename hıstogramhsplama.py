#Hande Gülmen 02205076013 -gri seviyeli görüntünün histogramı hesaplama-
import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread("goruntu.png")
s=img.shape
cv2.imshow('goruntu',img)

path=cv2.imread("goruntu.png",0)

Hist = np.zeros(shape=(256,1))
for i in range (s[0]):
    for j in range (s[1]):
        k=path[i,j]
        Hist[k,0]=Hist[k,0]+1

plt.plot(Hist)
plt.show()
cv2.waitkey(0)
