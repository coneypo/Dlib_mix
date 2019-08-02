import cv2
import os
import sys

path_screenshots = sys.path[0]+'/'
cap = cv2.VideoCapture(0)
cap.set(3, 960)

file_list=os.listdir(sys.path[0])

img_list=[]
img_cnt_max=0
for file in file_list:
    if '.jpg' in file:
        img_list.append(file)
        img_cnt=str(file).split('.')[0].split('_')[-1]
        img_cnt=int(img_cnt)
        if img_cnt>img_cnt_max:
            img_cnt_max=img_cnt
        else:
            img_cnt_max=img_cnt_max

print('Existing images:', img_list)

cnt='2'

flag, img_rd = cap.read()
k = cv2.waitKey(1)
img_gray = cv2.cvtColor(img_rd, cv2.COLOR_RGB2GRAY)
cv2.imwrite(path_screenshots +"acrn_test_"+str(img_cnt_max+1)+".jpg",img_rd)
print('Saving into:    ', path_screenshots +"acrn_test_"+str(img_cnt_max+1)+".jpg")
