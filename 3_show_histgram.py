import cv2
import numpy as np

file_src = 'src.png'

cv2.namedWindow('src', cv2.WINDOW_NORMAL)
cv2.namedWindow('gray_original', cv2.WINDOW_NORMAL)
cv2.namedWindow('gray_equalize', cv2.WINDOW_NORMAL)
cv2.namedWindow('hst_original', cv2.WINDOW_NORMAL)
cv2.namedWindow('hst_equalize', cv2.WINDOW_NORMAL)

img_src = cv2.imread(file_src, 1)
img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
img_gray_equalize = cv2.equalizeHist(img_gray)

img_hst_original = np.zeros([100, 256]).astype('uint8')
img_hst_equalize = np.zeros([100, 256]).astype('uint8')
rows, cols = img_hst_original.shape[:2]

hdims = [256]
hranges = [0, 256]
hist_original = cv2.calcHist([img_gray], [0], None, hdims, hranges)
hist_equalize = cv2.calcHist([img_gray_equalize], [0], None, hdims, hranges)
min_val_original, max_val_original, min_loc_original, max_loc_original = cv2.minMaxLoc(
    hist_original)
min_val_equalize, max_val_equalize, min_loc_equalize, max_loc_equalize = cv2.minMaxLoc(
    hist_equalize)

for i in range(0, 255):
    v = hist_original[i]
    cv2.line(img_hst_original, (i, rows), (i, rows -
                                           rows * (v / max_val_original)), (255, 255, 255))

    s = hist_equalize[i]
    cv2.line(img_hst_equalize, (i, rows), (i, rows -
                                           rows * (s / max_val_equalize)), (255, 255, 255))

cv2.imshow('src', img_src)
cv2.imshow('gray_original', img_gray)
cv2.imshow('gray_equalize', img_gray_equalize)
cv2.imshow('hst_original', img_hst_original)
cv2.imshow('hst_equalize', img_hst_equalize)
cv2.waitKey(0)
cv2.destroyAllWindows()
