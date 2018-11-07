#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

def move():
    pub = rospy.Publisher('/mobile_base/commands/velocity',Twist,queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(2)
    move=Twist()
    while not rospy.is_shutdown():
        move.linear.x= 5
        move.linear.y=0.0
        move.linear.z=0.0
        rospy.loginfo('move')

        pub.publish(move)
        rate.sleep()

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
