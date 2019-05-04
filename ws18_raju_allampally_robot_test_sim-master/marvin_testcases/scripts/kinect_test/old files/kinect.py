#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
    print msg.ranges[180]


if __name__== '__main__':
    rospy.init_node('scan_values')
    sub = rospy.Subscriber('/scan', LaserScan, callback)
    rospy.spin()
