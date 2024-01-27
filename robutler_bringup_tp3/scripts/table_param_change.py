#!/usr/bin/env python3
import rospy
from std_srvs.srv import Empty
import argparse

def update_local_planner_params(new_value):
    rospy.wait_for_service('/move_base/set_parameters')
    try:
        set_params = rospy.ServiceProxy('/move_base/set_parameters', Empty)
        set_params()
        rospy.loginfo("Parameter updated successfully.")
    except rospy.ServiceException as e:
        rospy.logerr("Failed to update parameter: %s", e)

if __name__ == '__main__':
    
    rospy.init_node('my_navigation_script_node')
    parser = argparse.ArgumentParser(description='Script')
    parser.add_argument('-v', '--value', type=float, help='', required=False,
                        default='0.50')
    args = vars(parser.parse_args())  # creates a dictionary
    print(args)


    # Perform other actions or movements

    # Dynamically set a parameter during a specific action
    update_local_planner_params(args["value"])
    print("I updated the parameter to: ",args['value'])
