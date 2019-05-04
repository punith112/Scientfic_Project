#!/usr/bin/env python
import unittest
import rospy
from time import sleep
import rostest
from gazebo_msgs.msg import ModelStates
from new_file import *
print total_dist

# class ForDistance(unittest.TestCase):
#
#     Destination_ok=False
#     def test_destination_check(self):
#         rospy.init_node('new_testfordistance')
#
#         counter=0
#
#         while not rospy.is_shutdown() and counter<5  and (not self.Destination_ok):
#             sleep(1)
#             counter +=1
#             if(total_dist==5):
#                 print total_dist
#                 self.Destination_ok=True
#             else:
#                 self.Destination_ok=False
#
#         self.assertTrue(self.Destination_ok)
#
# if __name__ == '__main__':
#     rostest.rosrun('distance_test','new_testfordistance', ForDistance)
