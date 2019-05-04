# marvin_navigation

This is the mega package that launches the modules configured for Marvins's navigation. Before using this package,
the following packages must be installed:

[gmapping] (http://wiki.ros.org/gmapping): `sudo apt-get install ros-kinetic-gmapping`

[map_server] (http://wiki.ros.org/map_server): `sudo apt-get install ros-kinetic-map-server`

[amcl] (http://wiki.ros.org/amcl): `sudo apt-get install ros-kinetic-amcl`

[move_base] (http://wiki.ros.org/move_base): `sudo apt-get install ros-kinetic-move-base`

**To map a room (launches preconfigured Rviz):**

*In simulation:*  `roslaunch marvin_navigation gmapping_sim.launch`

**To move robot to simple goals defined by 2D_Nav_goal(launches preconfigured Rviz):**

*In simulation:* `roslaunch marvin_navigation gmapping_sim.launch`

On Sucessfully Launching the gmapping package configured.

![mavin_gmapping](marvin_navigation/RVIZ_gmapping.png)

Once you create a map, you need to save it if you want to use it later, using:

`rosrun map_server map_saver -f name.yaml`

Here standard maps can be used playground.yaml (other Maps iki_lab.yaml, iki_arena.yaml)

**To localise the robot (launches preconfigured Rviz):**

*In simulation:* `roslaunch marvin_navigation amcl_sim.launch`

**To launch autonomous navigation of the robot (launches preconfigured Rviz):**

*In simulation:* `roslaunch marvin_navigation move_base_sim.launch`

The default map file is the `playground.yaml` file stored in this package.

## move_base Parameters

This package currently implements the TrajectoryPlannerROS (http://wiki.ros.org/base_local_planner) as the local planner for the navigation.
All parameters (which are mostly unchanged from the navigation tutorials) are stored in the `params` directory.

On Sucessfully Launching the marvin_navigation move_base.The Robot is Ready for navigating to Simple Goals.


![move_base](marvin_navigation/robot_pose_navigation_move_base.png)

