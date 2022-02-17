# box_spawn   
## content   
A) Briefing   
B) Explanation of the code   
C) Reference   
## Briefing    
Before you begin this simulation, make sure you have downloaded the **'deepexpress_description'** zip file and extracted on the same workspace with the **'pythonlaunch'** file. Also, make sure you have fully uploaded the gazebo package.    
Missing out one of this code could result in error   
   
1. First open up terminal and type in the code   ```cd your_workspace/src/pythonlaunch/script/```   
2. After finding the correct directory to the python file type in the code ```shortsim.py```   
3. Your gazebo simulation should open up with four boxes spawned in a random position   

## Explanation of the code   
This code uses four separate sdf files that has a model and config file. The location of the sdf files is in workspace/src/deepexpress_description/gazebo_sdf   
The python code starts out with the code   

```python
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
```       

These are required imports needed to spawn four random boxes to a random grid position in the gazebo world.   
Afterward there is a definition to open a *empty_world.launch* from the *gazebo_ros* package.   

```python

def launch_sim():   
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)   
    roslaunch.configure_logging(uuid)   
   
    cli_args = ['gazebo_ros', 'empty_world.launch']   
    roslaunch_args = cli_args[2:]   
    roslaunch_file = [(roslaunch.rlutil.resolve_launch_arguments(cli_args)[0],roslaunch_args)]   
   
    parent = roslaunch.parent.ROSLaunchParent(uuid, roslaunch_file)   
    parent.start()
```   
       
 Now we will spawn 4 different colored and size boxes in a random position.   
 
 ```python
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
                        robot_namespace='/model',  initial_pose = Pose(position = Point(random.uniform(-8.0, 8.0),random.uniform(-8.0, 8.0),0),orientation=Quaternion(0,0,0,random.uniform(0, 3.14))), reference_frame='world')'   
                        
Finally, we must disable the ros_simulation_time in order to avoid the ROS simulation time colliding with the gazebo/clock.   
'def disable_sim_time():
        command = 'rosparam set use_sim_time false'
        print(command)
        os.system(command)
```   
        
   
Now the main code will run the definitions in order.   
```python
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
   ```   
##Reference   
1) https://answers.ros.org/question/337065/what-is-the-correct-way-to-spawn-a-model-to-gazebo-using-a-python-script/
2) https://answers.ros.org/question/337065/what-is-the-correct-way-to-spawn-a-model-to-gazebo-using-a-python-script/
