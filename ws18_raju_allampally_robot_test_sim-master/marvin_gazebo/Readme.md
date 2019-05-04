# marvin_gazebo

This package contains the world files,marvin to apper in the gazebo_predefined_world.

**To launch the package (with both Rviz and Gazebo launching Head_Less Mode)**:

`roslaunch marvin_gazebo marvin_world.launch`

Add the Robot_Model to view in rviz

`rosrun rviz rviz`

**To launch the package (Merges Front Laser and Rear Laser Scan into Single)**:

`roslaunch ira_laser_tools laserscan_multi_merger.launch`

Marvin Simluation Gazebo Model.

![marvin_sim](marvin_gazebo/marvin_image.jpg)
