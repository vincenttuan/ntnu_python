# -*- coding=utf-8 -*-
# 安裝 py-opencv
import cv2

# 人臉偵測器
face_cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_alt2.xml')
# 眼睛偵測器
eye_cascade = cv2.CascadeClassifier('./xml/haarcascade_eye_tree_eyeglasses.xml')

# 設定攝像鏡頭
cap = cv2.VideoCapture(0)

# 設定捕捉區域
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    # 捕捉 frame-by-frame
    ret, frame = cap.read()  # ret : 讀到的 frame 是正確的化會回傳 true

    # 定義灰度圖像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 監測人臉
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # 找到的人臉個數
    print("Found {0} faces!".format(len(faces)))

    # 在臉部周圍畫矩形框
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 5)  # 注意：(0, 255, 0) 是 BGR
        # 繪文字
        cv2.putText(frame, 'Vincent', (x, y - 7), 16, 1.2, (0, 255, 0), 2)

        # 眼睛辨識程序
        # -----------------------------------------------------------------------
        # 獲取該人臉矩形框的感興趣區域 ROI(region of interest), 淺複製(子圖像區域)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        # 進行眼睛辨識
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        # -----------------------------------------------------------------------


    # 將 frame 顯示
    cv2.imshow('Detect Face and eyes', frame)

    # 按下 q 離開迴圈
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 釋放資源與關閉視窗
cap.release()
cv2.destroyAllWindows()

