#!/usr/bin/env python

import unittest
import rospy
from time import sleep
import rostest
from std_msgs.msg import String
from geometry_msgs.msg import Twist

from gazebo_msgs.msg import ModelStates

global msg
msg = 0

class TestTalkerListener(unittest.TestCase):

    talker_ok=False
    global l
    global m
    def callback(self, msg):
        # print(rospy.get_caller_id(), "I heard %s"%data.data)
        # self.success = data.data and data.data.startswith('hello world')
        self.talker_ok=False
        print msg.pose.pose.position.x

        l = msg.pose.pose.position.x
        m = msg.pose.pose.position.y

        if abs(l) > 15:
            self.talker_ok=True
        elif abs(m) > 15:
            self.talker_ok=True

    def test_talker_listener(self):
        rospy.init_node('test_basic')
        rospy.Subscriber('/gazebo/model_states', ModelStates, self.callback)
        counter=0

        while not rospy.is_shutdown() and counter<5  and (not self.talker_ok):
            sleep(1)
            counter +=1

        self.assertTrue(self.talker_ok)

if __name__ == '__main__':
    rostest.rosrun('mini_project','talker_listener_test', TestTalkerListener)
