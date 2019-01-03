import cv2

file_src = 'src.png'

cv2.namedWindow('src', cv2.WINDOW_NORMAL)
cv2.namedWindow('dst_weightedave', cv2.WINDOW_NORMAL)
cv2.namedWindow('dst_gaussian', cv2.WINDOW_NORMAL)
cv2.namedWindow('dst_laplacian', cv2.WINDOW_NORMAL)

img_src = cv2.imread(file_src, 1)

# フィルタ処理
img_dst_weightedave = cv2.blur(img_src, (3, 3))
img_dst_gaussian    = cv2.GaussianBlur(img_src, (11, 11), 1)
img_dst_laplacian   = cv2.Laplacian(img_src, cv2.CV_32F, 3)

cv2.imshow('src', img_src)
cv2.imshow('dst_weightedave', img_dst_weightedave)
cv2.imshow('dst_gaussian',    img_dst_gaussian)
cv2.imshow('dst_laplacian',   img_dst_laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()
