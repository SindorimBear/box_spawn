#!/usr/bin/env python
import roslaunch
import rospy
import sys
import subprocess
import rosservice
import os
import random

from gazebo_msgs.msg import *
from gazebo_msgs.srv import *
from geometry_msgs.msg import *

state = True
name = 0

class Node:
    def launch(self):
        self._launch.start()
        self._process = self._launch.launch(self._node)
    def status(self):
        if self._process_is_alive():
            return "Active"
        else:
            return "Deactivated"

def launch_sim():
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)

    cli_args = ['gazebo_ros', 'empty_world.launch']
    roslaunch_args = cli_args[2:]
    roslaunch_file = [(roslaunch.rlutil.resolve_launch_arguments(cli_args)[0],roslaunch_args)]

    parent = roslaunch.parent.ROSLaunchParent(uuid, roslaunch_file)
    parent.start()

def spawn_box1():
    rospy.wait_for_service("/gazebo/spawn_sdf_model")
    spawn_model_client = rospy.ServiceProxy("/gazebo/spawn_sdf_model", SpawnModel)
    spawn_model_client(model_name = 'box1', model_xml=open('/home/cmmoon98/workspace/src/deepexpress_description/gazebo_sdf/box1/model.sdf','r').read(),
                        robot_namespace='/model',  initial_pose = Pose(position = Point(random.uniform(-8.0, 8.0),random.uniform(-8.0, 8.0),0),orientation=Quaternion(0,0,0,random.uniform(0, 3.14))), reference_frame='world')


def spawn_box2():
    rospy.wait_for_service("/gazebo/spawn_sdf_model")
    spawn_model_client = rospy.ServiceProxy("/gazebo/spawn_sdf_model", SpawnModel)
    spawn_model_client(model_name = 'box2', model_xml=open('/home/cmmoon98/workspace/src/deepexpress_description/gazebo_sdf/box2/model.sdf','r').read(),
                        robot_namespace='/model',  initial_pose = Pose(position = Point(random.uniform(-8.0, 8.0),random.uniform(-8.0, 8.0),0),orientation=Quaternion(0,0,0,random.uniform(0, 3.14))), reference_frame='world')

def spawn_box3():
    rospy.wait_for_service("/gazebo/spawn_sdf_model")
    spawn_model_client = rospy.ServiceProxy("/gazebo/spawn_sdf_model", SpawnModel)
    spawn_model_client(model_name = 'box3', model_xml=open('/home/cmmoon98/workspace/src/deepexpress_description/gazebo_sdf/box3/model.sdf','r').read(),
                        robot_namespace='/model',  initial_pose = Pose(position = Point(random.uniform(-8.0, 8.0),random.uniform(-8.0, 8.0),0),orientation=Quaternion(0,0,0,random.uniform(0, 3.14))), reference_frame='world')

def spawn_box4():
    rospy.wait_for_service("/gazebo/spawn_sdf_model")
    spawn_model_client = rospy.ServiceProxy("/gazebo/spawn_sdf_model", SpawnModel)
    spawn_model_client(model_name = 'box4', model_xml=open('/home/cmmoon98/workspace/src/deepexpress_description/gazebo_sdf/box4/model.sdf','r').read(),
                        robot_namespace='/model',  initial_pose = Pose(position = Point(random.uniform(-8.0, 8.0),random.uniform(-8.0, 8.0),0),orientation=Quaternion(0,0,0,random.uniform(0, 3.14))), reference_frame='world')

def disable_sim_time():
        command = 'rosparam set use_sim_time false'
        print(command)
        os.system(command)


def main():
    try:
        global state
        launch_sim()
        spawn_box1()
        spawn_box2()
        spawn_box3()
        spawn_box4()
        rospy.set_param('/activity_status', 1)
        disable_sim_time()


        while True:
            status = rospy.get_param('/activity_status')

            if status != 1:
                break
            else:
                pass
    except KeyboardInterrupt:
        state = True
        print("Keyboard Interrupt", stat)

    except Exception as e:
        print(e)

    finally:
        exit()

if __name__ == '__main__':
    main()