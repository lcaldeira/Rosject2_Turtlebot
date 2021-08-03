#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class RepeatTeleop():

    def __init__(self, target_list=[]):
        rospy.init_node("intercept_teleop", anonymous=False)
        rospy.Subscriber("cmd_vel", Twist, self.intercept)
        self.pub = []
        self.target = []
        self.cmd_vel = Twist()
        self.addTarget(target_list)

    def addTarget(self, target_list):
        new_target = list(set(target_list) - set(self.target))
        self.target = self.target + new_target
        for robot in new_target:
            self.pub.append(rospy.Publisher(robot + "/cmd_vel", Twist, queue_size=1))

    def intercept(self, msg):
        print(f'Command vel = {msg}')
        self.cmd_vel.linear = msg.linear
        self.cmd_vel.angular = msg.angular
        self.broadcast()

    def broadcast(self):
        for p in self.pub:
            p.publish(self.cmd_vel)

    def run(self):
        while not rospy.is_shutdown():
            rospy.spin()

if __name__ == "__main__":
    try:
        repeater = RepeatTeleop()
        repeater.addTarget(["tb3_0","tb3_1"])
        repeater.run()
    except rospy.ROSInterruptException:
        pass