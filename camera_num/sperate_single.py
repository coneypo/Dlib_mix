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

Vshow = cv2.imread("test2.jpg")
img_gray = cv2.cvtColor(Vshow, cv2.COLOR_BGR2GRAY)

# 反转颜色
# ret, img_inv = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)


# method = cv2.CHAIN_APPROX_NONE  # 存储所有边界点
method = cv2.CHAIN_APPROX_SIMPLE  # 压缩垂直、水平、对角方向，只保留端点
# method = cv2.CHAIN_APPROX_TX89_L1  # 使用teh-Chini近似算法
# #method = cv2.CHAIN_APPROX_TC89_KCOS  # 使用teh-Chini近似算法

# 返回三个值，图像，轮廓，轮廓的层析结构
image, contours, hierarchy = cv2.findContours(img_gray, cv2.RETR_EXTERNAL, method)

print("Nums of contours:", len(contours), "\n")
contours_list = []

# ii = 0,1,2,3
for ii in range(len(contours)):
    contours_list.append(contours[3 - ii])

# 外矩阵
# cv2.boundingRect 计算轮廓的垂直边界最小矩形

rectangle_list = []

for i in range(len(contours)):
    x, y, w, h = cv2.boundingRect(contours_list[i])
    # print("Number:", i + 1)
    # print("Position:(", x, ",", y, ')\t', "(", x + w, ",", y + h, ")")
    rectangle_tmp = [x, y, w, h]
    if w > 20 and h > 20:
        if w<100 and h<100:
            # print(rectangle_tmp)
            rectangle_list.append(rectangle_tmp)
    # print('\n')
# print('\n')


for rectangle in rectangle_list:
    print(rectangle)
    cv2.rectangle(Vshow, (rectangle[0], rectangle[1]), (rectangle[0] + rectangle[2], rectangle[1] + rectangle[3]),
                  (0, 255, 0), 1)

cv2.imshow("camera", Vshow)
cv2.waitKey(0)
