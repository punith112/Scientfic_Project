#!/usr/bin/env python
import unittest
import rospy
from time import sleep
import rostest
from gazebo_msgs.msg import ModelStates
from distancemoved import *

class ForDistance(unittest.TestCase):

    def callback(self,msg):
        print msg.pose[1].position.x
        self.r= msg.pose[1].position.x


    def test_destination_check(self):
        rospy.init_node('testfordistance')

        rospy.Subscriber("/gazebo/model_states", ModelStates, self.callback)
        counter=0

        while not rospy.is_shutdown() and counter<5:
            sleep(1)
            counter +=1
        self.assertEqual(round(self.r,1),distance+0.3)

if __name__ == '__main__':
    rostest.rosrun('distance_test','testfordistance', ForDistance)
