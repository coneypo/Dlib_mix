# 调用摄像头

import cv2
import numpy as np
cap = cv2.VideoCapture(1)

# cap.set(propId, value)
# 设置视频参数，propId设置的视频参数，value设置的参数值
cap.set(3, 480)

line_key = 2

while cap.isOpened():
    ret_flag, Vshow = cap.read()

    # 二值化
    img_gray = cv2.cvtColor(Vshow, cv2.COLOR_BGR2GRAY)

    # 反转颜色
    ret, img_inv = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

    # Gauss filter
    img_gauss = cv2.GaussianBlur(img_gray, (3, 3), 0)

    # find edges
    # cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient ]]])
    edges = cv2.Canny(img_gray, 50, 150, apertureSize=3)

    # cv2.HoughLines
    # a way to find lines
    #  这里对最后一个参数使用了经验型的值
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 10)
    # lines = cv2.HoughLines(edges, 1, np.pi / 180, 118)

    img_cp = img_gray.copy()

    if lines[0].size == 2:
        for line in lines[0]:
            rho = line[0]  # 第一个元素是距离rho
            theta = line[1]  # 第二个元素是角度theta
            # print('rho:   ', rho)
            # print('theta: ', theta)
            if (theta < (np.pi / line_key)) or (theta > (3. * np.pi / line_key)):  # 垂直直线
                # print('ve')
                # 该直线与第一行的交点
                pt1 = (int(rho / np.cos(theta)), 0)
                # 该直线与最后一行的焦点
                pt2 = (int((rho - img_cp.shape[0] * np.sin(theta)) / np.cos(theta)), img_cp.shape[0])
                # 绘制一条白线
                cv2.line(img_cp, pt1, pt2, (255))
            else:  # 水平直线
                # print("hor")
                # 该直线与第一列的交点
                pt1 = (0, int(rho / np.sin(theta)))
                # 该直线与最后一列的交点
                pt2 = (img_cp.shape[1], int((rho - img_cp.shape[1] * np.cos(theta)) / np.sin(theta)))
                # 绘制一条直线
                cv2.line(img_cp, pt1, pt2, (255), 1)
            # print('\n')

    k = cv2.waitKey(1)

    # 闭操作：闭操作可以将目标区域连成一个整体，便于后续轮廓的提取。
    kernelX = cv2.getStructuringElement(cv2.MORPH_RECT, (17, 5))
    edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernelX)

    # 膨胀腐蚀(形态学处理)
    kernelX = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 1))
    kernelY = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 19))

    edges = cv2.dilate(edges, kernelX)
    edges = cv2.erode(edges, kernelX)

    edges = cv2.erode(edges, kernelY)
    edges = cv2.dilate(edges, kernelY)

    # 平滑处理，中值滤波
    edges = cv2.medianBlur(edges, 15)

    # 查找轮廓
    method = cv2.CHAIN_APPROX_SIMPLE  # 压缩垂直、水平、对角方向，只保留端点
    image, contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, method)

    for item in contours:
        rect = cv2.boundingRect(item)
        x = rect[0]
        y = rect[1]
        weight = rect[2]
        height = rect[3]
        if weight > (height * 2):
            image_rec = Vshow[y:y + height, x:x + weight]
            cv2.imshow('image', image_rec)

            # # 保存
            # if k == ord('s'):
            cv2.imwrite("test_rec.jpg", image_rec)

    #
    #   退 出
    if k == ord('q'):
        break

# 释放所有摄像头
cap.release()

# 删除建立的所有窗口
cv2.destroyAllWindows()
