#! /usr/bin/env python

import roslib
roslib.load_manifest('marvin_testcases')
import rospy
import actionlib
from std_msgs.msg  import Float64

from marvin_manipulation.msg import linearActuatorAction

class linearServer:
    def __init__(self):
        self.pub   = rospy.Publisher('/marvin/linear_actuator_controller/command', Float64 ,queue_size=10)
        self.server = actionlib.SimpleActionServer('linear_move', linearActuatorAction, self.execute, False)
        self.server.start()

    def execute(self, goal):


        self.pub.publish(goal.input)
        self.server.set_succeeded()

if __name__ == '__main__':
    rospy.init_node('linear_server')
    server = linearServer()
    rospy.spin()
