#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
def talker():
    num = 1
    pub = rospy.Publisher('p1', String, queue_size=10)
    rospy.init_node('p1', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        hello_str = "Month " + str(num)
        pub.publish(hello_str)
        num = num + 1
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass