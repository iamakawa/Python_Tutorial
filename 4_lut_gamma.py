import cv2
import numpy as np

LUT_GAMMA = 1.5

file_src = 'src.png'

cv2.namedWindow('src', cv2.WINDOW_NORMAL)
cv2.namedWindow('dst', cv2.WINDOW_NORMAL)

img_src = cv2.imread(file_src, 1)
lkup_tbl = np.zeros((256, 1), dtype='uint8')

for i in range(256):
    lkup_tbl[i][0] = 255 * pow(float(i) / 255, 1.0 / LUT_GAMMA)

img_dst = cv2.LUT(img_src, lkup_tbl)

cv2.imshow('src', img_src)
cv2.imshow('dst', img_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
