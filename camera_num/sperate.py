# created at 2018-09-28

# Author:   coneypo
# Blog:     http://www.cnblogs.com/AdaminXie
# GitHub:   https://github.com/coneypo/Vericode_decoder

# show bounding rectangles of image

import cv2
import numpy as np

path_test_image = "../data/images/for_test/vericode_2.jpg"


cap = cv2.VideoCapture(1)

# cap.set(propId, value)
# 设置视频参数，propId设置的视频参数，value设置的参数值
cap.set(3, 480)

while cap.isOpened():
    ret_flag, Vshow = cap.read()
    img_gray = cv2.cvtColor(Vshow, cv2.COLOR_BGR2GRAY)

    # 反转颜色
    ret, img_inv = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

    # 返回三个值，图像，轮廓，轮廓的层析结构
    image, contours, hierarchy = cv2.findContours(img_inv, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    print("Nums of contours:", len(contours), "\n")
    contours_list = []

    # ii = 0,1,2,3
    for ii in range(len(contours)):
        contours_list.append(contours[3 - ii])

    # 外矩阵
    # cv2.boundingRect 计算轮廓的垂直边界最小矩形
    for i in range(len(contours)):
        x, y, w, h = cv2.boundingRect(contours_list[i])
        print("Number:", i+1)
        print("Position:(", x, ",", y, ')\t', "(", x + w, ",", y + h, ")")
        cv2.rectangle(Vshow, (x, y), (x + w, y + h), (0, 255, 0), 1)

        print('\n')
    print('\n')

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