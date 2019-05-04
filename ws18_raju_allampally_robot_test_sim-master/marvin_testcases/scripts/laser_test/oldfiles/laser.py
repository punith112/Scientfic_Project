#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
    print msg.ranges[60]


if __name__== '__main__':
    rospy.init_node('scan_values')
    sub = rospy.Subscriber('/scan_front_raw', LaserScan, callback)
    rospy.spin()
