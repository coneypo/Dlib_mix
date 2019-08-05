# created at 2018-09-28

# Author:   coneypo
# Blog:     http://www.cnblogs.com/AdaminXie
# GitHub:   https://github.com/coneypo/Vericode_decoder

# show bounding rectangles of image

import cv2

Vshow = cv2.imread("test_rec.jpg")
img_gray = cv2.cvtColor(Vshow, cv2.COLOR_BGR2GRAY)

method = cv2.CHAIN_APPROX_SIMPLE  # 压缩垂直、水平、对角方向，只保留端点

# 返回三个值，图像，轮廓，轮廓的层析结构
image, contours, hierarchy = cv2.findContours(img_gray, cv2.RETR_EXTERNAL, method)

print("Nums of contours:", len(contours), "\n")
contours_list = []

# ii = 0,1,2,3
# for ii in range(len(contours)):
contours_list.append(contours[0])

# print(len(contours))
# print(contours_list)
# 外矩阵
# cv2.boundingRect 计算轮廓的垂直边界最小矩形

rectangle_list = []

print(Vshow.shape)

# for i in range(len(contours)):
x, y, w, h = cv2.boundingRect(contours_list[0])
# print("Number:", i + 1)
# print("Position:(", x, ",", y, ')\t', "(", x + w, ",", y + h, ")")
print(x,y,w,h)
rectangle_tmp = [x, y, w, h]
if w > 20 and h > 20:
    if w < 100 and h < 100:
        # print(rectangle_tmp)
        rectangle_list.append(rectangle_tmp)
    # print('\n')
# print('\n')


for rectangle in rectangle_list:
    print(rectangle)
    Vshow = cv2.rectangle(Vshow, (rectangle[0], rectangle[1]),
                          (rectangle[0] + rectangle[2], rectangle[1] + rectangle[3]),
                          (0, 255, 0), 1)

cv2.imshow("camera", Vshow)
cv2.waitKey(0)

cv2.imwrite("img_rec_new.jpg", Vshow)
