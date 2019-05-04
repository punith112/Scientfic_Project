#!/usr/bin/env python
import unittest
import rospy
from time import sleep
from geometry_msgs.msg import Twist
import rostest
from gazebo_msgs.msg import ModelStates
from std_msgs.msg import Int32
from math import sqrt

global distance
distance = 5



class ForDistance(unittest.TestCase):


    def setUp(self):
        self.velocity_publisher = rospy.Publisher('/kate/cmd_vel', Twist, queue_size=10)

    def callback(self,msg):
        global position
        global pos_x
        global pos_y
        x = msg.name.index("kate")
        self.r= msg.pose[x].position.x
        self.pos_x = msg.pose[x].position.x
        self.pos_y = msg.pose[x].position.y

    def test_move(self):
        # Starts a new node
        rospy.init_node('testfordistance', anonymous=True)

        rospy.Subscriber("/gazebo/model_states", ModelStates, self.callback)
        vel_msg = Twist()

        rospy.sleep(2)

        init_pos_x = self.pos_x
        init_pos_y = self.pos_y
        total_dist = 0

        while not rospy.is_shutdown():
            total_dist = total_dist + ((self.pos_x - init_pos_x)**2 + (self.pos_y - init_pos_y)**2)**0.5
            init_pos_x = self.pos_x
            init_pos_y = self.pos_y
            if(total_dist<distance):
                #Publish the velocity
                vel_msg.linear.x = 0.5
                self.velocity_publisher.publish(vel_msg)
                print total_dist

            elif(round(total_dist,1)==distance):
                print total_dist
                vel_msg.linear.x = 0
                self.velocity_publisher.publish(vel_msg)
                self.assertGreaterEqual(total_dist,distance)
                break
            # rospy.sleep(0.2)


if __name__ == '__main__':
    rostest.rosrun('distance_test','testfordistance', ForDistance)
