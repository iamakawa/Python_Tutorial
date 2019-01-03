
import cv2
import numpy as np
import random

LUT_GAMMA = 1.5

file_src = 'src.png'

cv2.namedWindow('gray', cv2.WINDOW_NORMAL)
cv2.namedWindow('dst_2', cv2.WINDOW_NORMAL)
cv2.namedWindow('dst_random', cv2.WINDOW_NORMAL)
cv2.namedWindow('dst_errdiffusion', cv2.WINDOW_NORMAL)
cv2.namedWindow('dst_bayer', cv2.WINDOW_NORMAL)

img_src = cv2.imread(file_src, 1)
img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)

# 二値変換
THRESH    = 100
MAX_PIXEL = 255
_, img_dst_2 = cv2.threshold(img_gray,THRESH,MAX_PIXEL,cv2.THRESH_BINARY)

# ディザリング
SIZE_IMAGE = 512, 512, 1
img_dst_random = np.zeros(SIZE_IMAGE, dtype=np.uint8)
img_dst_errdiffusion = np.zeros(SIZE_IMAGE, dtype=np.uint8)
img_dst_bayer = np.zeros(SIZE_IMAGE, dtype=np.uint8)

# ランダムディザリング
for y in range(SIZE_IMAGE[0]):
    for x in range(SIZE_IMAGE[1]):
        rand = random.random()*MAX_PIXEL
        if img_gray[y][x] > rand:
            img_dst_random[y][x] = MAX_PIXEL
        else:
            img_dst_random[y][x] = 0

# 誤差拡散ディザリング
THRESH_ERRDIFFUSION = 128
errval_errfissufion = 0
for y in range(SIZE_IMAGE[0]):
    for x in range(SIZE_IMAGE[1]):
        if (img_gray[y][x] + errval_errfissufion) < THRESH_ERRDIFFUSION:
            img_dst_errdiffusion[y][x] = 0
            errval_errfissufion = img_gray[y][x]
        else:
            img_dst_errdiffusion[y][x] = MAX_PIXEL
            errval_errfissufion = img_gray[y][x] - MAX_PIXEL

# 組織的ディザリング(Bayer)
N_BAYER = 4
matrix_bayer = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]
magnification_bayer = (MAX_PIXEL+1)/(N_BAYER*N_BAYER)
for x in range(N_BAYER):
    for y in range(N_BAYER):
        matrix_bayer[y][x] *= magnification_bayer

for y in range(SIZE_IMAGE[0]):
    for x in range(SIZE_IMAGE[1]):
        if img_gray[y][x] < matrix_bayer[y % N_BAYER][x % N_BAYER]:
            img_dst_bayer[y][x] = 0
        else:
            img_dst_bayer[y][x] = MAX_PIXEL

# 表示
cv2.imshow('dst_2', img_dst_2)
cv2.imshow('dst_random', img_dst_random)
cv2.imshow('dst_errdiffusion', img_dst_errdiffusion)
cv2.imshow('dst_bayer', img_dst_bayer)
cv2.waitKey(0)
cv2.destroyAllWindows()
