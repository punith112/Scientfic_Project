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
from marvin_testcases.msg import tiltAction, tiltGoal

class TestPtuTilt(unittest.TestCase):

    # talker_ok=False
    def setUp(self):
        self.client = actionlib.SimpleActionClient('tilt_ptu', tiltAction)
        rospy.init_node('ptu_tilt')
        rospy.Subscriber('/marvin/joint_states', JointState, self.callback)


    def callback(self,msg):
        x = msg.name.index("ptu_tilt")
        print msg.position[x]
        self.r=msg.position[x]

    def test_max_position(self):


        self.client.wait_for_server()

        # goal = DoDishesGoal()
        goal = marvin_testcases.msg.tiltGoal(input=0.2)

        self.client.send_goal(goal)


    def test_middle_position(self):


        self.client.wait_for_server()

        # goal = DoDishesGoal()
        goal = marvin_testcases.msg.tiltGoal(input=-0.4)

        self.client.send_goal(goal)

    def test_min_position(self):


        self.client.wait_for_server()

        # goal = DoDishesGoal()
        goal = marvin_testcases.msg.tiltGoal(input=-0.3)

        self.client.send_goal(goal)

    def test_diagonal_position(self):

        self.client.wait_for_server()

        # goal = DoDishesGoal()
        goal = marvin_testcases.msg.tiltGoal(input=-0.8)

        self.client.send_goal(goal)

        counter=0

        while not rospy.is_shutdown() and counter<5 :
            sleep(2)
            counter +=1

        self.assertEqual(round(self.r,1),goal.input)

if __name__ == '__main__':
    rostest.rosrun('marvin_testcases','ptu_tilt_test', TestPtuTilt)
