#! /usr/bin/env python

import roslib
roslib.load_manifest('marvin_testcases')
import rospy
import actionlib
from std_msgs.msg  import Float64

from marvin_testcases.msg import panAction

class PanServer:

    def __init__(self):
        self.pub   = rospy.Publisher('/marvin/ptu_pan_controller/command', Float64 ,queue_size=10)

        self.server = actionlib.SimpleActionServer('paning',panAction, self.execute, False)

        self.server.start()

    def execute(self, goal):

        self.pub.publish(goal.input)
        self.server.set_succeeded()

if __name__ == '__main__':
    rospy.init_node('paning_server')
    server = PanServer()
    rospy.spin()
