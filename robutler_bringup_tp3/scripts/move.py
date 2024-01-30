#!/usr/bin/env python3
import rospy
import rospy
import cv2
import numpy as np
from geometry_msgs.msg import PoseStamped, Point, Quaternion, Twist
from std_msgs.msg import Header
from tf.transformations import quaternion_from_euler
from move_base_msgs.msg import MoveBaseActionGoal

# Assuming you have a publisher for the /cmd_vel topic
cmd_vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

# Create a Twist message to control robot velocity
cmd_vel_msg = Twist()
cmd_vel_msg.linear.x = 0.1  # Move forward with a linear velocity of 1.0 m/s
cmd_vel_publisher.publish(cmd_vel_msg)

# Wait for some time to let the robot move (you can adjust the duration)
rospy.sleep(5.0)  # 5 seconds as an example

# Stop the robot by publishing a new Twist message with zero linear velocity
cmd_vel_msg.linear.x = 0.0
cmd_vel_publisher.publish(cmd_vel_msg)
