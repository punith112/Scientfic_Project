## marvin_testcases

# Scripts

This package contains the Automated Test Cases for Marvin Basic Functionality Test_Cases



**To Run the Test Case Run the Server Node and Run the Test Cases**:

**Scripts**:

*1.Distance Test Case :*

To move the robot to a predefined distance and test if the movement of the robot is achieved

`rosrun test_distancenew.py`

After running the folllowing above script the bot moves in the simulation and Testcase Pass sucessfully


*2.Kinect Test :*

To Run Test_case of Kinect_Test

`rosrun testcaseforkinect.py`

To spawn the model for laser and kinect testing spwan the Model which appears in front of Marvin

rosrun gazebo_ros spawn_model -file /home/rakesh/catkin_ws/src/ws18_raju_allampally_robot_test_sim/marvin_testcases/scripts/laser_test/my_sdf.sdf -sdf -model marvin_testcases



*3.Laser Test :*

To Run Test_case of Laser Hukoyu Laser 

`rosrun test_forlaser.py`


*4.linear actuator_Kinect Test :*

To Start the Server of linear_actuator with kinect

`rosrun linear_server.py`

To Run Test_case of linear_actuator with kinect

`rosrun linear_guide_kinect_test.py`


*5.linear actuator_test :*

To Start the Server of linear_actuator

`rosrun linear_server.py`

To Run Test_case of linear_actuator

`rosrun linear_guide_test.py`


*6.pan_test :*

To Start the Server of PTU Panning for left and right movement(-45 and +45)

`rosrun panserver.py`

To Run Test_case of pan_test

`rosrun pan_test.py`



*7.tilt test :*

To Start the Server of PTU tilt for Up and Down movement(-45 and +45)

`rosrun tiltserver.py`

To Run Test_case of pan_test

`rosrun testfortilt.py`




