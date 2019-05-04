#!/usr/bin/env python
import unittest
import rospy
from time import sleep
import rostest
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class Test_kinect(unittest.TestCase):

    def callback(self,msg):
        print msg.ranges[180]
        self.r=msg.ranges[180]



    def test_for_kinect(self):
        rospy.init_node('kinect_test')
        rospy.Subscriber('/scan', LaserScan, self.callback)

        counter=0

        while not rospy.is_shutdown() and counter<5:
            sleep(1)
            counter +=1

            self.assertEqual(round(self.r,1),1.3)

if __name__ == '__main__':
    rostest.rosrun('proof_of_concept','kinect_test', Test_kinect)
