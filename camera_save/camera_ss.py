import cv2
import time
import os
import sys


path_screenshots = sys.path[0]+'/'
cap = cv2.VideoCapture(0)
cap.set(3, 960)

ss_cnt = 0

while cap.isOpened():
    flag, img_rd = cap.read()
    k = cv2.waitKey(1)
    img_gray = cv2.cvtColor(img_rd, cv2.COLOR_RGB2GRAY)
    font = cv2.FONT_HERSHEY_SIMPLEX

    if k == ord('q'):
        break
    else:
        cv2.putText(img_rd, "Press 'S': Screen shot", (20, 400), font, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(img_rd, "Press 'Q': Quit", (20, 450), font, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
    if k == ord('s'):
        ss_cnt += 1
        print(path_screenshots + "screenshot" + "_" + str(ss_cnt) + "_" + time.strftime("%Y-%m-%d-%H-%M-%S",
                                                                                        time.localtime()) + ".jpg")
        cv2.imwrite(path_screenshots + "screenshot" + "_" + str(ss_cnt) + "_" + time.strftime("%Y-%m-%d-%H-%M-%S",
                                                                                              time.localtime()) + ".jpg",
                    img_rd)

    cv2.namedWindow("camera", 1)
    cv2.imshow("camera", img_rd)

cap.release()
cv2.destroyAllWindows()