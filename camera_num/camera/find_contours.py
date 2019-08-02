# 调用摄像头

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

    # 提取轮廓
    image, contours, hierarchy = cv2.findContours(image=img_inv, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

    # 高斯滤波
    img_Gauss = cv2.GaussianBlur(img_gray, (3, 3), 0)

    # 显示轮廓
    cv2.drawContours(Vshow, contours, -1, (255, 0, 0))

    cv2.imshow("camera", Vshow)

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