#! /usr/bin/env python

import roslib
roslib.load_manifest('marvin_testcases')
import rospy
import actionlib
from std_msgs.msg  import Float64

from marvin_testcases.msg import tiltAction

class Tilt_PTUServer:

    def __init__(self):
        self.pub   = rospy.Publisher('/marvin/ptu_tilt_controller/command', Float64 ,queue_size=10)
        self.server = actionlib.SimpleActionServer('tilt_ptu', tiltAction, self.execute, False)
        self.server.start()

    def execute(self, goal):
        self.pub.publish(goal.input)
        self.server.set_succeeded()

if __name__ == '__main__':
    rospy.init_node('tiltserver')
    server = Tilt_PTUServer()
    rospy.spin()
