#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np

####################################### This script is for individual use, not paired with mission_maneger ##########################################

class ObjectDetectionNode:
    
    def __init__(self):
        #self.object_contours = {}        
        rospy.init_node('object_detection_node', anonymous=True)
        self.bridge = CvBridge()
        #Aqui posso fazer um switch de camara se for useful, para a camara de cima
        self.image_sub = rospy.Subscriber('/camera/rgb/image_raw', Image, self.image_callback)
        print(dir(self.image_sub))



    def create_masks(self,image):
        
        # Define the region of interest (ROI) in order to ignore the orange/yellow collored floor
        roi = image[:7 * image.shape[0] // 12, :]
        
        #DIFFERENT COLORS - NECESSITA ALTERAÇOES EM TDOAS MENOS PURPLE E BLUE
        #Purple
        lower_purple = np.array([120, 50, 50])
        upper_purple = np.array([150, 255, 255])

        #Blue
        lower_blue = np.array([78,158,124])  # Acertos na deteção do blue das bolas 
        upper_blue = np.array([138,255,255])

        #Light blue
        lower_lblue = np.array([100, 100, 100])
        upper_lblue = np.array([130, 255, 255])

        # Orange
        lower_orange = np.array([5, 100, 100])
        upper_orange = np.array([20, 255, 255])

        #Green
        lower_green = np.array([40, 40, 40]) 
        upper_green = np.array([80, 255, 255]) 


        # Yellow
        lower_yellow = np.array([25, 100, 100])
        upper_yellow = np.array([40, 255, 255])
        
        #Red
        lower_red = np.array([0, 100, 100])  
        upper_red = np.array([5, 255, 255]) 

        # Threshold the image to get only the desired color
        masks = {
            "purple" : cv2.inRange(roi, lower_purple, upper_purple),
            "blue" : cv2.inRange(roi, lower_blue, upper_blue),
            "l_blue" : cv2.inRange(roi, lower_lblue, upper_lblue),
            "orange": cv2.inRange(roi, lower_orange, upper_orange),
            "green" : cv2.inRange(roi, lower_green, upper_green),
            "yellow" : cv2.inRange(roi, lower_yellow, upper_yellow),
            "red" : cv2.inRange(roi, lower_red, upper_red), 
        }

        return masks
            
    
    def image_callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, 'bgr8')
        except CvBridgeError as e:
            rospy.logerr(e)
            return

        # Convert BGR to HSV
        hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
        
        color_contours = {}
        masks = self.create_masks(hsv_image)
        for color, mask in masks.items():  # Use items() to iterate through dictionary key-value pairs
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            color_contours[color] = contours

        self.object_contours = {}

        for color, contours in color_contours.items():
            self.object_contours[color] = 0
            for contour in contours:
                area = cv2.contourArea(contour)
                if area > 100:  # adjust this threshold based on your needs
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(cv_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    label = f"{color}"
                    cv2.putText(cv_image, label, (x + 3, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
                    self.object_contours[color] += 1
        
        print(self.object_contours)
        # Display the result (you can remove this in the final version)
        cv2.putText(cv_image, f'Objects in Frame: {self.object_contours}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.40, (0,0,0), 2)   
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

