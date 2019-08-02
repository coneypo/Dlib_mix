# 调用摄像头
# Canny algorithm

import cv2
import numpy as np

cap = cv2.VideoCapture(1)

# cap.set(propId, value)
# 设置视频参数，propId设置的视频参数，value设置的参数值
cap.set(3, 480)

while cap.isOpened():
    ret_flag, Vshow = cap.read()
   # cv2.imshow("camera", Vshow)

    # 二值化
    img_gray = cv2.cvtColor(Vshow, cv2.COLOR_BGR2GRAY)

    # 反转颜色
    ret, img_inv = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

    # find edges
    # cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient ]]])
    # the higher the threshold is, the less the camera show
    edges = cv2.Canny(img_gray, 200, 300, apertureSize=3)

    cv2.imshow("camera", edges)

    # 每帧数据延时1ms，延时为0读取的是静态帧
    k = cv2.waitKey(1)

    # 保存
    if k == ord('s'):
        cv2.imwrite("test.jpg", Vshow)

    # 退出
    if k == ord('q'):
        break

# 释放所有摄像头
cap.release()

# 删除建立的所有窗口
cv2.destroyAllWindows()