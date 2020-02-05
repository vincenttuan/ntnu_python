# -*- coding=utf-8 -*-
import cv2

# 人臉偵測器
face_cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_alt2.xml')

# 微笑偵測器
smile_cascade = cv2.CascadeClassifier('./xml/haarcascade_smile.xml')

img = cv2.imread("./image/test.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
isSmile = False

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=8,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
)

# 畫出每一個臉
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = gray[y:y + h, x:x + w]

    # 微笑偵測辨識程序
    # -----------------------------------------------------------------------
    smile = smile_cascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.1,
        minNeighbors=100,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # 打上 Smile 標籤
    for (sx, sy, sw, sh) in smile:
        isSmile = True
        cv2.putText(img, 'Smile', (x + sx, y + sy - 7), 3, 1, (0, 255, 0), 2)
    # -----------------------------------------------------------------------

cv2.imshow('Face and Smile', img)

# 儲存檔案 (請自己建立 image_out 資料夾)
if isSmile:
    cv2.imwrite("./image_out/smile.jpg", img)

# 任意鍵離開(若設定為 0 就表示持續等待至使用者按下按鍵為止)
c = cv2.waitKey(0)

