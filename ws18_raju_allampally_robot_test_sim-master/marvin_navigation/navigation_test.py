#!/usr/bin/env python
import rospy
import actionlib
import unittest
import rospy
from time import sleep
import rostest
from gazebo_msgs.msg import ModelStates
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

class TestManipulation(unittest.TestCase):

    # talker_ok=False
    def setUp(self):
        rospy.init_node('Navigation_test_case')
        rospy.Subscriber("/gazebo/model_states", ModelStates, self.callback)
        self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)

    def callback(self,msg):
        x = msg.name.index("robot")
        self.pos_x = msg.pose[x].position.x

        # self.pos_w = msg.pose[x].orientation.w
    def test_navigation(self):



        self.client.wait_for_server()

        goal = MoveBaseGoal()

        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = 1.0
        #goal.target_pose.pose.position.y = 0.5
        goal.target_pose.pose.orientation.w = 0.1

        self.client.send_goal(goal)


        counter=0

        while not rospy.is_shutdown() and counter<5:
            sleep(10)
            counter +=1



        self.assertEqual(round(self.pos_x,1),(goal.target_pose.pose.position.x-0.1))

if __name__ == '__main__':
    rostest.rosrun('marvin_manipulation','Navigation_test_case', TestManipulation)






# def movebase_client():
#
#     client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
#     client.wait_for_server()
#
#     goal = MoveBaseGoal()
#     goal.target_pose.header.frame_id = "map"
#     goal.target_pose.header.stamp = rospy.Time.now()
#     goal.target_pose.pose.position.x = 2.5
#     goal.target_pose.pose.orientation.w = 2.0
#
#     client.send_goal(goal)
#     wait = client.wait_for_result()
#     if not wait:
#         rospy.logerr("Action server not available!")
#         rospy.signal_shutdown("Action server not available!")
#     else:
#         return client.get_result()
#
# if __name__ == '__main__':
#     try:
#         rospy.init_node('movebase_client_py')
#         result = movebase_client()
#         if result:
#             rospy.loginfo("Goal execution done!")
#     except rospy.ROSInterruptException:
#         rospy.loginfo("Navigation test finished.")
