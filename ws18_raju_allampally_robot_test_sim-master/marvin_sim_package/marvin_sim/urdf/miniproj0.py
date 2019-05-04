#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def callback(msg):
    print msg.ranges[180]
    if msg.ranges[180]>1:
        print "reached if condition"
        move.linear.x=1
    else:
        print "reached else condition"
        move.linear.x=0
    pub.publish(move)

if __name__ == '__main__':
    rospy.init_node('vel_subscriber')
    pub = rospy.Publisher('/kate/cmd_vel',Twist,queue_size=10)
    move=Twist()
    rospy.Subscriber('/kate/laser/scan', LaserScan, callback)


    rospy.spin()
