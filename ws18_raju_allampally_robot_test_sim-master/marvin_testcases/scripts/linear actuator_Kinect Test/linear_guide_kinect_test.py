#!/usr/bin/env python
import unittest
import rospy
from time import sleep
import rostest
from std_msgs.msg import String
from sensor_msgs.msg import JointState
import roslib
roslib.load_manifest('marvin_manipulation')
import rospy
import actionlib
import marvin_manipulation.msg
from marvin_manipulation.msg import linearActuatorAction, linearActuatorGoal

class TestManipulation(unittest.TestCase):

    # talker_ok=False
    def setUp(self):
        self.client = actionlib.SimpleActionClient('linear_move', linearActuatorAction)

    def callback(self,msg):
        print msg.position[12]
        self.r=msg.position[12]

    def test_zero_position(self):
        rospy.init_node('linear_guide_test')
        rospy.Subscriber('/marvin/joint_states', JointState, self.callback)

        self.client.wait_for_server()

        # goal = DoDishesGoal()
        goal = marvin_manipulation.msg.linearActuatorGoal(input=0.0)

        self.client.send_goal(goal)


    def test_two_position(self):
        rospy.init_node('linear_guide_test')
        rospy.Subscriber('/marvin/joint_states', JointState, self.callback)

        self.client.wait_for_server()

        # goal = DoDishesGoal()
        goal = marvin_manipulation.msg.linearActuatorGoal(input=0.2)

        self.client.send_goal(goal)






    def test_five_position(self):
        rospy.init_node('linear_guide_test')
        rospy.Subscriber('/marvin/joint_states', JointState, self.callback)

        self.client.wait_for_server()

        # goal = DoDishesGoal()
        goal = marvin_manipulation.msg.linearActuatorGoal(input=0.5)

        self.client.send_goal(goal)

    def test_eight_position(self):
        rospy.init_node('linear_guide_test')
        rospy.Subscriber('/marvin/joint_states', JointState, self.callback)

        self.client.wait_for_server()

        # goal = DoDishesGoal()
        goal = marvin_manipulation.msg.linearActuatorGoal(input=1.0)

        self.client.send_goal(goal)

        counter=0

        while not rospy.is_shutdown() and counter<5 :
            sleep(4)
            counter +=1

        self.assertEqual(round(self.r,2),goal.input)

if __name__ == '__main__':
    rostest.rosrun('marvin_manipulation','linear_guide_test', TestManipulation)
