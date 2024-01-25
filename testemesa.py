#!/usr/bin/env python3

import cv2
import numpy as np


A = cv2.imread("/home/mestre/Desktop/Image1.jpg")

B = cv2.imread("/home/mestre/Desktop/Image2.jpg")
dimensions = A.shape
print(dimensions)
height = 480
width = 640

errorL2 = cv2.norm(A, B, cv2.NORM_L2)
similarity = 1 - errorL2 / (height * width)
print("Similarity = ", similarity)

cv2.imshow("A", A)
cv2.imshow("B", B)
cv2.waitKey(0)
