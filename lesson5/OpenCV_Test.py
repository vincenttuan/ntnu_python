# -*- coding=utf-8 -*-
'''
安裝 py-opencv, 安裝指令如下 :
pip install opencv-python
pip uninstall opencv-contrib-python
pip install opencv-contrib-python
'''
import cv2

# 設定攝像鏡頭
cap = cv2.VideoCapture(0)

# 判斷攝像鏡頭是否啟動 ?
if not cap.isOpened():
    cap.open()

# 設定捕捉區域
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    # 捕捉 frame-by-frame
    ret, frame = cap.read()  # ret : 讀到的 frame 是正確的化會回傳 true
    print(frame)

    # 將 frame 顯示
    cv2.imshow('Video', frame)

    # 按下 q 離開迴圈 (「1」表示停 1ms 來偵測是否使用者有按下q。若設定為「0」就表示持續等待至使用者按下按鍵為止)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()

