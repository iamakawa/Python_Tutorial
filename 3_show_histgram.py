import cv2
import numpy as np

file_src = 'src.png'

cv2.namedWindow('src', cv2.WINDOW_NORMAL)
cv2.namedWindow('gray', cv2.WINDOW_NORMAL)
cv2.namedWindow('hst', cv2.WINDOW_NORMAL)

img_src = cv2.imread(file_src, 1)
img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)

img_hst = np.zeros([100, 256]).astype('uint8')
rows, cols = img_hst.shape[:2]

hdims = [256]
hranges = [0, 256]
hist = cv2.calcHist([img_gray], [0], None, hdims, hranges)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(hist)

for i in range(0, 255):
    v = hist[i]
    cv2.line(img_hst, (i, rows), (i, rows -
                                  rows * (v / max_val)), (255, 255, 255))

cv2.imshow('src', img_src)
cv2.imshow('gray', img_gray)
cv2.imshow('hst', img_hst)
cv2.waitKey(0)
cv2.destroyAllWindows()
