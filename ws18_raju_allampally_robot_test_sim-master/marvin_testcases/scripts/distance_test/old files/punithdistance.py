#!/usr/bin/env python

import rospy
import unittest
import rospy
from time import sleep
from geometry_msgs.msg import Twist
from gazebo_msgs.msg import ModelStates
from std_msgs.msg import Int32
from math import sqrt

global distance
global total_dist
pos_x = 0
pos_y = 0
init_pos_x = 0
init_pos_y = 0
distance = 5

# it Travels to the distance of 5 meters with Values of distance = 1 and speed = 1

def callback(msg):
    global position
    global pos_x
    global pos_y
    x = msg.name.index("kate")
    pos_x = msg.pose[x].position.x
    pos_y = msg.pose[x].position.y

def move():
    # Starts a new node
    global position
    global pos_x
    global pos_y
    pos_x = 0
    pos_y = 0

    rospy.init_node('new_distance_file', anonymous=True)
    velocity_publisher = rospy.Publisher('/kate/cmd_vel', Twist, queue_size=10)
    odometry = "/gazebo/model_states"
    rospy.Subscriber("/gazebo/model_states", ModelStates, callback)
    vel_msg = Twist()
    #Receiveing the user's input
    print("Let's move your robot")
    speed = input("input speed of robot = ")
    isForward = input("Foward? =  ")#True or False
    #Checking if the movement is forward or backwards
    if(isForward):
        vel_msg.linear.x = abs(speed)
    else:
        vel_msg.linear.x = -abs(speed)
    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    rospy.sleep(2)

    init_pos_x = pos_x
    init_pos_y = pos_y
    total_dist = 0

    while not rospy.is_shutdown():
        total_dist = total_dist + ((pos_x - init_pos_x)**2 + (pos_y - init_pos_y)**2)**0.5
        init_pos_x = pos_x
        init_pos_y = pos_y
        if(total_dist<distance):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            print total_dist
	else:
		vel_msg.linear.x = 0
		velocity_publisher.publish(vel_msg)
        #
        # velocity_publisher.publish(vel_msg)
        rospy.sleep(0.2)
    return total_dist


if __name__ == '__main__':
    try:
        move()
        # rostest.rosrun('new_distance_file','new_distance_file', ForDistance)
    except rospy.ROSInterruptException:
        pass
