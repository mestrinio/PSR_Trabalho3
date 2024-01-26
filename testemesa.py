#!/usr/bin/env python3

import cv2
import numpy as np


A = cv2.imread("/home/mestre/Desktop/Image1.jpg")

B = cv2.imread("/home/mestre/Desktop/Image2.jpg")
dimensions = A.shape
print(dimensions)
height = dimensions(1)
width = dimensions(2)


errorL2 = cv2.norm(A, B, cv2.NORM_L2)
similarity = 1 - errorL2 / (height * width)
print("Similarity = ", similarity)

if similarity >= 0.90:
    table_message = "There isn't any object on the table"
    updateMissionDescription(table_message)
    
else:
    table_message = "There are objects on the table...\nIt needs cleaning!!!"

rospy.sleep(3)

imshow_message = "I'm going to show you the photos so you can check for yourself."
updateMissionDescription(imshow_message)

rospy.sleep(3)
cv2.imshow("A", A)
cv2.imshow("B", B)
cv2.waitKey(0)

finished_message = "Task completed, what do you want me to do next, Master?"
updateMissionDescription(finished_message)

