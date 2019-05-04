# marvin_sim_package

This package contains the URDF files,MeshFiles that define the simulation model of Marvin.

This is the Depedent Package for the Other Package marvin_gazebo

**To launch the package (with both Rviz and Gazebo launching)**:

`roslaunch marvin_gazebo marvin_world.launch`

**To launch the package (Merges Front Laser and Rear Laser Scan into Single)**:

`roslaunch ira_laser_tools laserscan_multi_merger.launch`
