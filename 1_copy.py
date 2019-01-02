import cv2

file_src = 'src.png'
file_dst = 'dst.png'

cv2.namedWindow('src', cv2.WINDOW_NORMAL)
cv2.namedWindow('dst', cv2.WINDOW_NORMAL)

img_src = cv2.imread(file_src, 1)
img_dst = cv2.flip(img_src, flipCode = 0)

cv2.imshow('src', img_src)
cv2.imshow('dst', img_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
