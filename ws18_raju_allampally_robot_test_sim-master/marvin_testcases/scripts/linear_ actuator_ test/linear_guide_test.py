#!/usr/bin/env python
import unittest
import rospy
from time import sleep
import rostest
from std_msgs.msg import String
from sensor_msgs.msg import JointState
import roslib
roslib.load_manifest('marvin_testcases')
import rospy
import actionlib
import marvin_testcases.msg
from marvin_testcases.msg import linearActuatorAction, linearActuatorGoal

class Testtestcases(unittest.TestCase):

    # talker_ok=False
    def setUp(self):
        rospy.init_node('testcases_test_case')
        rospy.Subscriber('/marvin/joint_states', JointState, self.callback)
        self.client = actionlib.SimpleActionClient('linear_move', linearActuatorAction)

    def callback(self,msg):
        print msg.position[12]
        self.r=msg.position[12]

    def test_zero_position(self):



        self.client.wait_for_server()

        # goal = DoDishesGoal()
        goal = marvin_testcases.msg.linearActuatorGoal(input=0.0)

        self.client.send_goal(goal)


    def test_two_position(self):



        self.client.wait_for_server()

        # goal = DoDishesGoal()
        goal = marvin_testcases.msg.linearActuatorGoal(input=0.2)

        self.client.send_goal(goal)






    def test_five_position(self):



        self.client.wait_for_server()

        # goal = DoDishesGoal()
        goal = marvin_testcases.msg.linearActuatorGoal(input=0.5)

        self.client.send_goal(goal)

    def test_eight_position(self):



        self.client.wait_for_server()

        # goal = DoDishesGoal()
        goal = marvin_testcases.msg.linearActuatorGoal(input=1.0)

        self.client.send_goal(goal)



        counter=0

        while not rospy.is_shutdown() and counter<5:
            sleep(3)
            counter +=1



        self.assertEqual(round(self.r,1),goal.input)

if __name__ == '__main__':
    rostest.rosrun('marvin_testcases','testcases_test_case', Testtestcases)
