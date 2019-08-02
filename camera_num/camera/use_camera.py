# 调用摄像头

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# cap.set(propId, value)
# 设置视频参数，propId设置的视频参数，value设置的参数值
cap.set(3, 480)

# cap.isOpened（） 返回true/false 检查初始化是否成功
print(cap.isOpened())

# cap.read()
""" 返回两个值
          先返回一个布尔值，如果视频读取正确，则为 True，如果错误，则为 False，也可用来判断是否到视频末尾
          再返回一个值，为每一帧的图像，该值是一个三维矩阵
          通用接收方法为：
          ret,frame = cap.read();
          这样 ret 存储布尔值，frame 存储图像
          若使用一个变量来接收两个值，如
          frame = cap.read()
          则 frame 为一个元组，原来使用 frame 处需更改为 frame[1]
   返回值：R1：布尔值
          R2：图像的三维矩阵
"""
while cap.isOpened():
    ret_flag, Vshow = cap.read()
    cv2.imshow("camera", Vshow)

    gray = cv2.cvtColor(Vshow, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    # 输入图像必须是 float32，最后一个参数在 0.04 到 0.05 之间
    dst = cv2.cornerHarris(gray, 2, 3, 0.04)
    # result is dilated for marking the corners, not important
    dst = cv2.dilate(dst, None)
    # Threshold for an optimal value, it may vary depending on the image.
    Vshow[dst > 0.01 * dst.max()] = [0, 0, 255]
#    cv2.imshow('dst', Vshow)
#    if cv2.waitKey(0) & 0xff == 27:
 #       cv2.destroyAllWindows()

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