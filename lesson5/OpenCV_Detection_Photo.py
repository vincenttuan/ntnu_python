# -*- coding=utf-8 -*-
import cv2

facePath = "./xml/haarcascade_frontalface_alt2.xml"
faceCascade = cv2.CascadeClassifier(facePath)

img = cv2.imread("./image/what.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=8,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)

# 畫出每一個臉
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow('Face', img)
# 儲存檔案 (請自己建立 image_out 資料夾)
cv2.imwrite("./image_out/face.jpg",img)
# 任意鍵離開(若設定為 0 就表示持續等待至使用者按下按鍵為止)
c = cv2.waitKey(0)

