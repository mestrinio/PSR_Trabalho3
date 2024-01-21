#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np

class ObjectDetectionNode:
    def __init__(self):
        rospy.init_node('object_detection_node', anonymous=True)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber('/camera/image_raw', Image, self.image_callback)
        self.object_count = 0

    def image_callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, 'bgr8')
        except CvBridgeError as e:
            rospy.logerr(e)
            return

        # Convert BGR to HSV
        hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)

        # Define the range for the color you want to detect (adjust these values)
        lower_color = np.array([10, 100, 100])
        upper_color = np.array([25, 255, 255])

        # Threshold the image to get only the desired color
        mask = cv2.inRange(hsv_image, lower_color, upper_color)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw bounding boxes around detected objects and count only objects in the current frame
        self.object_count = 0
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 100:  # adjust this threshold based on your needs
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(cv_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                self.object_count += 1

        # Display the result (you can remove this in the final version)
        cv2.putText(cv_image, f'Objects in Frame: {self.object_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow("Object Detection", cv_image)
        cv2.waitKey(1)

def main():
    object_detection_node = ObjectDetectionNode()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
