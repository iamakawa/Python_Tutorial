import cv2

file_src = 'src.png'

cv2.namedWindow('src', cv2.WINDOW_NORMAL)
cv2.namedWindow('dst_hsv', cv2.WINDOW_NORMAL)
cv2.namedWindow('dst_gray', cv2.WINDOW_NORMAL)

img_src      = cv2.imread(file_src, 1)
img_dst_hsv  = cv2.cvtColor(img_src, cv2.COLOR_BGR2HSV)
img_dst_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)

cv2.imshow('src', img_src)
cv2.imshow('dst_hsv', img_dst_hsv)
cv2.imshow('dst_gray', img_dst_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
