#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from Lab_2.srv import AddTwoInts,AddTwoIntsResponse
def turtle():
    rospy.init_node('turtle', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/turtle1/pose',Pose, pose_callback)
    s = rospy.Service('add_two_ints', AddTwoInts,handle_add_two_ints)
    rate = rospy.Rate(10) # 10hz
    vel = Twist()
    while not rospy.is_shutdown():
        vel.linear.x = 0.2
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0.1
        pub.publish(vel)
        rate.sleep()
def pose_callback(pose):
    print(pose.x, pose.y,pose.theta)
def handle_add_two_ints(req):
    return AddTwoIntsResponse(req.a + req.b)
if __name__ == '__main__':
    try:
        turtle()
    except rospy.ROSInterruptException:
        pass