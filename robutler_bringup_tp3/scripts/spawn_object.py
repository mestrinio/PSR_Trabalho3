#!/usr/bin/env python3

import random

import rospy
import rospkg
from gazebo_msgs.srv import SpawnModel
from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import quaternion_from_euler
import uuid
import argparse


def main():

    # -------------------------------
    # Initialization
    # -------------------------------
    parser = argparse.ArgumentParser(description='Script to compute perfect numbers.')
    parser.add_argument('-l', '--location', type=str, help='', required=False,
                        default='on_bed')
    parser.add_argument('-o', '--object', type=str, help='', required=False,
                        default='person_standing')

 ################################### FAZER MODO RANDOM POSITION ######################
    args = vars(parser.parse_args())  # creates a dictionary
    print(args)

    rospack = rospkg.RosPack()
    package_path = rospack.get_path('robutler_description_tp3') + '/models/'

    ################# Defines poses where to put objects   #############
    poses = {}

    # on bed pose
    p = Pose()
    p.position = Point(x=-6.033466, y=1.971232, z=0.644345)
    q = quaternion_from_euler(0, 0, 0)  # From euler angles (rpy) to quaternion
    p.orientation = Quaternion(x=q[0], y=q[1], z=q[2], w=q[3])
    poses['on_bed'] = {'pose': p}

    # on bed-side-table pose
    p = Pose()
    p.position = Point(x=-4.489786, y=2.867268, z=0.679033)
    q = quaternion_from_euler(0, 0, 0)  # From euler angles (rpy) to quaternion
    p.orientation = Quaternion(x=q[0], y=q[1], z=q[2], w=q[3])
    poses['on_bed_side_table'] = {'pose': p}
    
    # on kitchen floor
    p = Pose()
    p.position = Point(x=6.994423, y=-2.998756, z=0.130587)
    q = quaternion_from_euler(0, 0, 0)  # From euler angles (rpy) to quaternion
    p.orientation = Quaternion(x=q[0], y=q[1], z=q[2], w=q[3])
    poses['on_kitchen'] = {'pose': p}

    # on living room
    p = Pose()
    p.position = Point(x=0.757308, y=-0.087025, z=0.130587)
    q = quaternion_from_euler(0, 0, 0)  # From euler angles (rpy) to quaternion
    p.orientation = Quaternion(x=q[0], y=q[1], z=q[2], w=q[3])
    poses['on_living_room'] = {'pose': p}

    # on playground
    p = Pose()
    p.position = Point(x=-7.570393, y=-2.799362, z=0.130587)
    q = quaternion_from_euler(0, 0, 0)  # From euler angles (rpy) to quaternion
    p.orientation = Quaternion(x=q[0], y=q[1], z=q[2], w=q[3])
    poses['on_playground'] = {'pose': p}

    # on living room table
    p = Pose()
    p.position = Point(x=1.891458, y=-1.630400, z=0.389908)
    q = quaternion_from_euler(0, 0, 0)  # From euler angles (rpy) to quaternion
    p.orientation = Quaternion(x=q[0], y=q[1], z=q[2], w=q[3])
    poses['on_living_room_table'] = {'pose': p}

    # on living room table 2
    p = Pose()
    p.position = Point(x=1.141329, y=-1.720264, z=0.365747)
    q = quaternion_from_euler(0, 0, 0)  # From euler angles (rpy) to quaternion
    p.orientation = Quaternion(x=q[0], y=q[1], z=q[2], w=q[3])
    poses['on_living_room_table2'] = {'pose': p}


    # on bedroom table
    p = Pose()
    p.position = Point(x=-8.900804, y=1.541628, z=0.743650)
    q = quaternion_from_euler(0, 0, 1.562233)  # From euler angles (rpy) to quaternion
    p.orientation = Quaternion(x=q[0], y=q[1], z=q[2], w=q[3])
    poses['on_bedroom_table'] = {'pose': p}
    


    ###################### Define objects ########################
    objects = {}

    # add object sphere_v (Violet Sphere)
    f = open(package_path + 'sphere_v/model.sdf', 'r')
    objects['sphere_v'] = {'name': 'sphere_v', 'sdf': f.read()}

    # add object sphere_r (Red Sphere)
    f = open(package_path + 'sphere_r/model.sdf', 'r')
    objects['sphere_r'] = {'name': 'sphere_r', 'sdf': f.read()}

    # add object sphere_g (Green Sphere)
    f = open(package_path + 'sphere_g/model.sdf', 'r')
    objects['sphere_g'] = {'name': 'sphere_g', 'sdf': f.read()}

    # add object sphere_org (Orange Sphere)
    f = open(package_path + 'sphere_org/model.sdf', 'r')
    objects['sphere_o'] = {'name': 'sphere_org', 'sdf': f.read()}
    
    # add object sphere_Y (Yellow Sphere)
    f = open(package_path + 'sphere_y/model.sdf', 'r')
    objects['sphere_y'] = {'name': 'sphere_y', 'sdf': f.read()}

    # add object person_standing
    f = open(package_path + 'person_standing/model.sdf', 'r')
    objects['person_standing'] = {'name': 'person_standing', 'sdf': f.read()}

    #add laptop
    f = open(package_path + 'labtop_mac_1/model.sdf', 'r')
    objects['laptop'] = {'name': 'labtop_mac_1', 'sdf': f.read()}

    #add can_coke
    f = open(package_path + 'can_coke/model.sdf', 'r')
    objects['coke'] = {'name': 'can_coke', 'sdf': f.read()}

    #add can_coke
    f = open(package_path + 'cube/model.sdf', 'r')
    objects['cube'] = {'name': 'cube', 'sdf': f.read()}


    # Check if given object and location are valid

    if not args['location'] in poses.keys():
        print('Location ' + args['location'] +
              ' is unknown. Available locations are ' + str(list(poses.keys())))

    if not args['object'] in objects.keys():
        print('Object ' + args['object'] +
              ' is unknown. Available objects are ' + str(list(objects.keys())))

    # -------------------------------
    # ROS
    # -------------------------------

    rospy.init_node('insert_object', log_level=rospy.INFO)

    service_name = 'gazebo/spawn_sdf_model'
    print('waiting for service ' + service_name + ' ... ', end='')
    rospy.wait_for_service(service_name)
    print('Found')

    service_client = rospy.ServiceProxy(service_name, SpawnModel)

    print('Spawning an object ...')
    uuid_str = str(uuid.uuid4())
    object_name = args['object']
    pose_name = args['location']

    service_client(objects[object_name]['name'] + '_' + uuid_str,
                objects[object_name]['sdf'],
                objects[object_name]['name'] + '_' + uuid_str,
                poses[pose_name]['pose'],
                'world')

    print(f"I spawned : {args['object']} in the {args['location']}")


if __name__ == '__main__':
    main()
