# Author:   coneypo
# Mail:     coneypo@foxmail.com

# Updated at 2019-07-26

import dlib  # 人脸处理的库 Dlib
import cv2  # 图像处理的库 OpenCv


def show_face_rectangle(img_rd, key_size):

    # Dlib 正向人脸检测器 / frontal face detector
    detector = dlib.get_frontal_face_detector()

    img_rd = cv2.imread(img_rd)

    # 人脸数 faces
    faces = detector(img_rd, 1)

    # 检测到人脸
    if len(faces) != 0:
        # 矩形框
        for k, d in enumerate(faces):
            # 计算矩形框大小
            height = (d.bottom() - d.top())
            width = (d.right() - d.left())

            cv2.rectangle(img_rd,
                          tuple([d.left() - int(width / key_size), d.top() - int(height / key_size)]),
                          tuple([d.right() + int(width / key_size), d.bottom() + int(height / key_size)]),
                          (255, 255, 255), 2)

    cv2.imshow("camera", img_rd)
    cv2.waitKey(0)


show_face_rectangle("2008_002506.jpg", 5)