import cv2
import numpy as np
import os

Kamera = cv2.VideoCapture(1)
kernel = np.ones((8, 8,), np.uint8)

isim = "Olurum TURKIYEM"
while True:
    ret, Kare = Kamera.read()
    Kesilmiş_Kare= Kare[0:300, 0:300]
    Kesilmiş_Kare_Gri = cv2.cvtColor(Kesilmiş_Kare, cv2.COLOR_BGR2GRAY)
    Kesilmiş_Kare_HSV = cv2.cvtColor(Kesilmiş_Kare, cv2.COLOR_BGR2HSV)

    Alt_Değerler = np.array([0, 20, 50])
    Üst_Değerler = np.array([90, 255, 255])

    Renk_Filtresi_Sonucu = cv2.inRange(Kesilmiş_Kare_HSV, Alt_Değerler, Üst_Değerler)
    Renk_Filtresi_Sonucu = cv2.morphologyEx(Renk_Filtresi_Sonucu, cv2.MORPH_CLOSE,kernel)

    Sonuç = Kesilmiş_Kare.copy()

    cnts, _ = cv2.findContours(Renk_Filtresi_Sonucu, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    Max_Genişlik = 0
    Max_Uzunluk = 0
    Max_Index = -1
    for t in range(len(cnts)):
        cnt = cnts[t]
        x,y,w,h = cv2.boundingRect(cnt)
        if(w>Max_Genişlik and h > Max_Uzunluk):
            Max_Uzunluk = h
            Max_Genişlik = w
            Max_Index = t

        cv2.rectangle(Sonuç, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if(len(cnts)>0):
        x,y,w,h = cv2.boundingRect(cnts[Max_Index])
        cv2.rectangle(Sonuç, (x, y), (x+w, y+h), (0, 255, 0) ,2)
        El_Resim = Renk_Filtresi_Sonucu[y:y+h, x:x+w]
        cv2.imshow("El Resim", El_Resim)



    #cv2.imshow("Kare", Kare)
   # cv2.imshow("Kesilmiş Kare",Kesilmiş_Kare)
    #cv2.imshow("Renk Filtresi", Renk_Filtresi_Sonucu)
    cv2.imshow("Sonuc",Sonuç)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.imwrite("Veri/"+isim+".jpg",El_Resim)

Kamera.release()
cv2.destroyAllWindows()
